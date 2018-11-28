#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <set>
#include <cstdio>
using namespace std;

int main(void)
{
    string line;
    getline(cin, line);
    int T;
    istringstream(line) >> T;
    for (int caseNo = 1; caseNo <= T; caseNo++) {
        getline(cin, line);
        const int len = line.length();
        set<char> kinds;
        map<char,int> num;
        for (int i = 0; i < len; i++) {
            if (kinds.find(line[i]) == kinds.end()) {
                if (kinds.size() == 0) num[line[i]] = 1;
                else if (kinds.size() == 1) num[line[i]] = 0;
                else num[line[i]] = kinds.size();
                kinds.insert(line[i]);
            }
        }
        int base = (kinds.size()==1) ? 2 : kinds.size();
        long long ans = 0;
        for (int i = 0; i < len; i++) {
            ans *= base;
            ans += num[line[i]];
        }
        printf("Case #%d: %lld\n", caseNo, ans);
    }

    return 0;
}

