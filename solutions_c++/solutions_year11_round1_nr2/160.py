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

char s[10240][16], p[1024];
int l[10240];
int N, M;
int pos[256];
vector<int> S[11];

int main(){
    int caseNumber;
    scanf("%d", &caseNumber);
    //cin>>caseNumber;
    REP(caseN, caseNumber) {
        scanf("%d%d", &N, &M);
        REP(j, 11)
            S[j].clear();
        REP(i, N) {
            scanf("%s", s[i]);
            l[i] = strlen(s[i]);
            S[l[i]].push_back(i);
        }
        printf("Case #%d:", caseN + 1);
        REP(tmp, M) {
            scanf("%s", p);
            REP(i, 26)
                pos[p[i]] = i;
            int maxn = -1, maxp = 0;
            REP(i, N) {
                int now = 0;
                REP(j, l[i])
                    now >?= pos[s[i][j]];
                if (now <= maxn)
                    continue;
                int cur = 0;
                vector<int> S2 = S[l[i]];
                int L = l[i];
                REP(j, 26) {
                    char c = p[j];
                    int fd = 0;
                    REP(x, S2.size())
                        REP(y, L)
                            fd |= s[S2[x]][y] == c;
                    if (!fd) 
                        continue;
                    vector<int> S3;
                    REP(x, S2.size()) {
                        int sm = 1;
                        REP(y, L) {
                            sm &= (s[S2[x]][y] == c) == (s[i][y] == c);
                            if (!sm)
                                break;
                        }
                        //~ cout<<i<<' '<<x<<' '<<sm<<' '<<c<<endl;
                        if (sm)
                            S3.push_back(S2[x]);
                    }
                    S2 = S3;
                    int hv = 0;
                    REP(j, L)
                        hv |= s[i][j] == c;
                    if (!hv)
                        cur++;
                    if (S2.size() == 1)
                        break;
                    //~ cout<<S2.size()<<cur;
                }
                if (cur > maxn) {
                    maxn = cur;
                    maxp = i;
                }
            }
            printf(" %s", s[maxp]);
        }
        puts("");
    }
    return 0;
}
