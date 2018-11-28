#include <iostream>
#include <string>
#include <algorithm>
#include <cstdio>
using namespace std;

int main() {
    int T;
    string s;

    cin >> T;
    for(int cc=1;cc<=T;cc++) {
        cin >> s;

        if(next_permutation(s.begin(), s.end())==false) {
            s+='0';
            sort(s.begin(), s.end());

            if(s[0]=='0') {
                int i;
                for(i=0;i<s.size();i++) {
                    if(s[i]!='0') break;
                }
                swap(s[0], s[i]);
            }
            printf("Case #%d: %s\n", cc, s.c_str());
        } else {
            printf("Case #%d: %s\n", cc, s.c_str());
        }
    }

    return 0;
}
