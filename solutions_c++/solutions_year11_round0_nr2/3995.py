#include <iostream>
#include <string>
#include <vector>
using namespace std;

string playMagicks(vector<string> cmbList, vector<string> opposeList, string inputStr)
{
    int pc = 0, fc = 0;
    // invoking first char here
    string fstr;
    fstr += inputStr[pc++];
    fc++;
    bool needcontinue = false;

    while (pc < inputStr.size()) {
        char in = inputStr[pc];

        // search for combination
        for (int c = 0; c < cmbList.size(); c++) {
            int indx = cmbList[c].find(in);
            if (indx != -1) {
                if ((indx == 1  && cmbList[c][0] == fstr[fc -1])
                    || (indx == 0 && cmbList[c][1] == fstr[fc -1])) {
                    fstr[fc -1] = cmbList[c][2];
                    needcontinue = true;
                    break;
                }
            }
        }

        if (needcontinue) {
            pc++;
            needcontinue = false;
            continue;
        }

        // search for opposing
        bool bNeedToClear = false;
        for (int op = 0; (op < opposeList.size()) && !bNeedToClear; op++) {
            int indx = opposeList[op].find(in);

            switch(indx) {
            case 1:
                if (fstr.find(opposeList[op][0]) != -1)
                    bNeedToClear = true;
                break;
            case 0:
                if (fstr.find(opposeList[op][1]) != -1)
                    bNeedToClear = true;
                break;
            }
         }
        if (!bNeedToClear) {
            fstr += inputStr[pc];
            pc++;
            fc++;
        } else {
            fstr.clear();
            pc++;
            // check for last char
            if (pc < inputStr.length()) {
                fstr = inputStr[pc];
                pc++;
                fc = 1;
            }
        }
    }
    return fstr;
}

string play(vector<string> cmbList, vector<string> opposeList, string inputStr)
{
    string output;
    string temp = playMagicks(cmbList, opposeList, inputStr);
    output += "[";
    for (int i = 0; i < temp.length(); i++) {
        output += temp[i];
        if(i == temp.length() - 1)
            break;
        output +=", ";
    }
    output += "]";
    return output;
}


int main(int argc, char** argv)
{
    int tcases, cmbListCount, opposeListCount, givenListCount;
    vector<string> cmbList, opposeList;
    string inputStr, tmpStr;
    cin>>tcases;

    for (int t = 0; t < tcases; t++) {
        // cmblist
        cin>>cmbListCount;
        for (int c = 0; c < cmbListCount; c++) {
            cin>>tmpStr;
            cmbList.push_back(tmpStr);
            tmpStr.clear();
        }

        // opposelist
        cin>>opposeListCount;
        for (int op = 0; op < opposeListCount; op++) {
            cin>>tmpStr;
            opposeList.push_back(tmpStr);
            tmpStr.clear();
        }

        // input String
        cin>>givenListCount;
        cin>>inputStr;

        cout<<"Case #"<<t + 1<<": "<<play(cmbList, opposeList, inputStr)<<endl;
        cmbList.clear();
        opposeList.clear();
        inputStr.clear();
    }
    return 0;
}