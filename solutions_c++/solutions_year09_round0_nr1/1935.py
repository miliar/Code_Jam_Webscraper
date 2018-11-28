//// AlienLanguage.cc

#include "AlienLanguage.h"


/// insert the word
void
AlienLanguage::insert(std::string word)
{
    std::vector<char> wordVec;

    for (std::string::size_type i = 0; i < word.size(); ++i)
        wordVec.push_back(word[i]);

    allWords_.push_back(wordVec);
}



/// number of matched words
int
AlienLanguage::getNMatch(std::string testcase) const
{
    std::vector<std::string> testcaseVec;
    std::string::size_type idx;

    while (!testcase.empty()) {
        /// group of letters
        if (testcase[0] == '(') {
            idx = testcase.find(')');
            testcaseVec.push_back(testcase.substr(1, (idx - 1)));
            testcase = testcase.substr(++idx);
        }
        /// a letter
        else {
            testcaseVec.push_back(testcase.substr(0, 1));
            testcase = testcase.substr(1);
        }
    }


    /// Match
    int i = 0;
    int nMatch = 0;
    bool matchFlag;

    for (std::vector< std::vector<char> >::const_iterator iWord = allWords_.begin();
         iWord != allWords_.end(); ++iWord) {
        matchFlag = true;

        for (i = 0; i < wordLength_; ++i) {
            idx = testcaseVec[i].find((*iWord)[i]);
            if (idx == std::string::npos) {
                matchFlag = false;
                break;
            }
        }

        if (matchFlag)
            ++nMatch;
    }


    return nMatch;
}
