#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <set>
#include <vector>
#include <algorithm>
using namespace std;
#define REP(i, n) for(int i = 0; i <(n); i++)

#define SORT(x) sort(x.begin(), x.end())

typedef long long LL;

char comb[1000][1000];
char opp[1000][1000];

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    scanf("%d", &t);

    for(int tcase = 1; tcase <= t; tcase++) {


        int c;
        scanf("%d", &c);

        REP(i, 1000) {
            REP(j, 1000) {
                comb[i][j]=0;
                opp[i][j]=0;
            }
        }
        REP(i, c) {
            string s;
            cin>>s;
            comb[s[0]][s[1]] = s[2];
            comb[s[1]][s[0]] = s[2];
        }

        int d;
        scanf("%d", &d);
        REP(i, d) {
            string s;
            cin>>s;
            opp[s[0]][s[1]] = opp[s[1]][s[0]] =1;
        }

        int n;
        scanf("%d", &n);
        string s;
        cin>>s;

        vector<char> ans;
        REP(i, n) {
            if(!ans.empty()) {
                char lastchar = *ans.rbegin();
                if(comb[lastchar][s[i]]) {
                    ans.pop_back();
                    ans.push_back(comb[lastchar][s[i]]);
                } else
                {
                    bool ok = true;
                    REP(j, ans.size()) {
                        if(opp[ans[j]][s[i]]) {
                            ok = false;
                            break;
                        }
                    }
                    if(!ok)
                    ans.clear();
                    else {
                        ans.push_back(s[i]);
                    }
                    continue;
                }
            } else {
                ans.push_back(s[i]);
            }
        }

        cout<<"Case #"<<tcase<<": [";
        for(int i = 0, _n=ans.size(); i < _n; i++) {
            if(i==0) printf("%c", ans[i]);
            else printf(", %c", ans[i]);
        }
        printf("]\n");

    }
}


