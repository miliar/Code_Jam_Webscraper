#include "file.h"

File::File()
{
    mLength = 0;
}

File::~File()
{
    for(unsigned int i = 0; i < mCaseData.size(); i++)
        delete mCaseData[i];

    mCaseData.clear();
    mCaseResult.clear();
}

bool File::load(const std::string& file)
{
    FILE *fp = fopen(file.c_str(), "r");
    if(fp) {
        //fscanf(fp, "%d", &mLength);
        mLength = 1;
        for(int i = 0; i < mLength; i++) {
            CaseData *caseData = new CaseData();

            // CHANGES.
            fscanf(fp, "%d", &caseData->letters);
            fscanf(fp, "%d", &caseData->words);
            fscanf(fp, "%d", &caseData->testCases);

            int j;
            char tmp[8192];

            for(j = 0; j < caseData->words; j++) {
                fscanf(fp, "%s", tmp);
                caseData->wordsVector.push_back(tmp);
            }
            for(j = 0; j < caseData->testCases; j++) {
                fscanf(fp, "%s", tmp);
                caseData->testCasesVector.push_back(tmp);
            }

            mCaseData.push_back(caseData);
        }

        fclose(fp);
        return true;
    }
    else {
        std::cout << "Coult not open " << file.c_str() << std::endl;
        return false;
    }
}

bool File::save(const std::string& file)
{
    FILE *fp = fopen(file.c_str(), "w");
    if(fp) {
        for(unsigned int i = 0; i < mCaseResult.size(); i++)
            fprintf(fp, "Case #%d: %s\n", i+1, mCaseResult[i].c_str());

        fclose(fp);
        return true;
    }
    else {
        std::cout << "Coult not save " << file.c_str() << std::endl;
        return false;
    }
}

bool File::compare()
{
    // CHANGES.
    // Check if the examples provided are ok.

    bool ok = true;
    if(strncmp(mCaseResult[0].c_str(), "2", 1) != 0)
        ok = false;
    else if(strncmp(mCaseResult[1].c_str(), "1", 1) != 0)
        ok = false;
    else if(strncmp(mCaseResult[2].c_str(), "3", 1) != 0)
        ok = false;
    else if(strncmp(mCaseResult[3].c_str(), "0", 1) != 0)
        ok = false;

    if(!ok)
        std::cout << "Failed comparing with examples." << std::endl;

    return ok;
}

void File::analyze()
{
    // CHANGES.
    int i, k;
    unsigned int l, m;
    for(i = 0; i < mLength; i++) {
        for(k = 0; k < mCaseData[i]->testCases; k++) {
            bool *eliminated = new bool[mCaseData[i]->words];
            int valid = 0;
            memset(eliminated, false, mCaseData[i]->words);

            int currentLetter = 0;
            for(l = 0; l < mCaseData[i]->testCasesVector[k].length(); l++) {
                if(mCaseData[i]->testCasesVector[k][l] == '(') {
                    l++;
                    bool *found = new bool[mCaseData[i]->words];
                    memset(found, false, mCaseData[i]->words);

                    while(mCaseData[i]->testCasesVector[k][l] != ')') {
                        for(m = 0; m < mCaseData[i]->wordsVector.size(); m++) {
                            if(mCaseData[i]->wordsVector[m][currentLetter] == mCaseData[i]->testCasesVector[k][l]) {
                                found[m] = true;
                            }
                        }
                        l++;
                    }

                    for(m = 0; m < mCaseData[i]->wordsVector.size(); m++) {
                        if(!found[m])
                            eliminated[m] = true;
                    }
                    delete []found;
                }
                else {
                    for(m = 0; m < mCaseData[i]->wordsVector.size(); m++) {
                        if(mCaseData[i]->wordsVector[m][currentLetter] != mCaseData[i]->testCasesVector[k][l])
                            eliminated[m] = true;
                    }
                }
                currentLetter++;
            }

            for(l = 0; l < mCaseData[i]->wordsVector.size(); l++) {
                if(eliminated[l] == 0) {
                    valid++;
                }
            }

            char result[8];
            sprintf(result, "%d", valid);
            mCaseResult.push_back(result);
            delete []eliminated;
        }
    }
}
