#include <iostream>
#include <set>
#include <vector>
#include <string>
#include <sstream>
#include <cstdio>
using namespace std;

int main(void)
{
    int L, D, N;
    string line;
    getline(cin, line);
    istringstream iss(line);
    iss >> L >> D >> N;

    set<string> words;
    while (D-- > 0) {
        getline(cin, line);
        words.insert(line);
    }

    for (int caseNo = 1; caseNo <= N; caseNo++) {
        getline(cin, line);
        istringstream iss2(line);
        vector<string> token(L, "");
        bool isInPara = false;
        char c;
        int i = 0;
        while (iss2 >> c) {
            if (c == '(') {
                isInPara = true;
            } else if (c == ')') {
                isInPara = false;
                i++;
            } else if (isInPara) {
                token[i] += string(1,c);
            } else {
                token[i] = string(1,c);
                i++;
            }
        }

        int K = 0;
        for (set<string>::const_iterator wd = words.begin();
                wd != words.end(); wd++) {
            for (int i = 0; i < L; i++) {
                if (token[i].find((*wd)[i]) == string::npos)
                    break;
                if (i == L-1) {
                    K++;
                    break;
                }
            }
        }

        printf("Case #%d: %d\n", caseNo, K);
    }

    return 0;
}

