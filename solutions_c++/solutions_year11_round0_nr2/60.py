#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cassert>
#include <set>
#include <map>
#include <queue>
#include <iostream>
#include <fstream>
using namespace std;
#define pb push_back 
#define REP(i,n) for(int i=0;i<(n);i++ )
typedef long long LL;
typedef pair<int, int> pii;

int main(){
    int caseNumber;
    scanf("%d", &caseNumber);
    //cin>>caseNumber;
    REP(caseN, caseNumber) {
        vector<string> t1, t2;
        int t; string s;
        cin>>t;
        while (t--) {
            cin>>s;
            t1.push_back(s);
        }
        cin>>t;
        while (t--) {
            cin>>s;
            t2.push_back(s);
        }
        int l;
        cin>>l>>s;
        vector<char> r;
        REP(i, l) {
            r.push_back(s[i]);
            if (r.size() >= 2) {
                char c1 = r[r.size() - 1], c2 = r[r.size() - 2];
                REP(j, t1.size()) {
                    if (t1[j][0] == c1 && t1[j][1] == c2) {
                        r.pop_back();
                        r.pop_back();
                        r.push_back(t1[j][2]);
                        break;
                    }
                    if (t1[j][0] == c2 && t1[j][1] == c1) {
                        r.pop_back();
                        r.pop_back();
                        r.push_back(t1[j][2]);
                        break;
                    }                    
                }
            }
            REP(j, t2.size())
                REP(k1, r.size())
                    REP(k2, r.size())
                        if (r[k1] == t2[j][0] && r[k2] == t2[j][1]) {
                            r.clear();
                            goto next;
                        }
            next:;
        }
        printf("Case #%d: ", caseN + 1);
        REP(i, r.size())
            printf("%s%c", i ? ",  " : "[", r[i]);
        if (!r.size())
            printf("[");
        puts("]");
    }
    return 0;
}
