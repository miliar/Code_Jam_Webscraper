#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <string>
#include <cstring>
#include <cmath>
#include <cctype>
#include <climits>
#include <functional>

#define FOR(i,a,b) for (int i=(a);i<(b);++i)
#define FORQ(i,a,b) for (int i=(a);i<=(b);++i)
#define FORD(i,a,b) for (int i=(a)-1;i>=(b);--i)
#define FORE(i,x) for (__typeof__((x).begin()) i=(x).begin();i!=(x).end();++i)

#define PB push_back
#define MP make_pair
#define F first
#define S second

using namespace std;

typedef pair<int,int> PII;
typedef long long LL;

const int MM = 10009;
const int MT = 12;

int n, m;
string T[MM];
set<int> TD[MT];
vector<int> CD[MT];

int main() {
    int lw;
    scanf("%d",&lw);
    FORQ(z,1,lw) {
        printf("Case #%d:", z);

        scanf("%d%d",&n,&m);
        FOR(i,0,n) {
            char Buf[15];
            scanf("%s",Buf);
            T[i] = Buf;
        }

        FORQ(i,1,10) {
            CD[i] = vector<int>(26, 0);
        }

        FOR(i,0,n) {
            TD[T[i].size()].insert(i);
            FORQ(c,'a','z')
                CD[T[i].size()][c-'a'] += count(T[i].begin(), T[i].end(), c);
        }

        FOR(t,0,m) {
            char Order[30];
            scanf("%s", Order);
            int best = -1;
            string bestGen = "";

            FOR(i,0,n) {
                vector<int> CDAct = CD[T[i].size()];
                set<int> Gut = TD[T[i].size()];

                int actBad = 0;
                FOR(j,0,26) {
                    if (CDAct[Order[j]-'a'] == 0 || Gut.size() <= 1)
                        continue;
                    if (T[i].find(Order[j]) != string::npos) {
                        set<int>::iterator wsk = Gut.begin();
                        while (wsk != Gut.end()) {
                            size_t twsk = -1, tti = -1;
                            do {
                                twsk = T[*wsk].find(Order[j], twsk+1);
                                tti  = T[i].find(Order[j], tti+1);
                            } while (twsk == tti && twsk != string::npos);
                            if (twsk != tti) {
                                FORE(c, T[*wsk])
                                    CDAct[*c-'a']--;
                                set<int>::iterator wskLast = wsk++;
                                Gut.erase(wskLast);
                            } else
                                wsk++;
                        }
                    } else {
                        actBad++;
                        set<int>::iterator wsk = Gut.begin();
                        while (wsk != Gut.end()) {
                            if (T[*wsk].find(Order[j]) != string::npos) {
                                FORE(c, T[*wsk])
                                    CDAct[*c-'a']--;
                                set<int>::iterator wskLast = wsk++;
                                Gut.erase(wskLast);
                            } else
                                wsk++;
                        }
                    }
                }
                if (best < actBad) {
                    best = actBad;
                    bestGen = T[i];
                }
            }

            printf(" %s", bestGen.c_str());
        }

        FOR(i,0,MT) {
            TD[i].clear();
            CD[i].clear();
        }

        printf("\n");
    }
    return 0;
}
