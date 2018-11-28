#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <queue>
#include <stack>
#include <cstdio>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <numeric>
#include <sstream>
#include <utility>
#include <iostream>
#include <algorithm>
#include <functional>

using namespace std;

#define EACH(i,c) for(__typeof((c).begin()) i = (c).begin();i!=(c).end();i++)
#define FOR(i,a,b)  for(int i=(a);i<(b);i++)
#define dbg(e)  cout<<(#e)<<" : "<<e<<endl
#define set(v,i) memset(v,i,sizeof(v))
#define all(x) x.begin(),x.end()
#define sz(x) int((x).size())
#define REP(i,n) FOR(i,0,n)
#define pb  push_back
#define mp make_pair

typedef long long LL;

inline int _abs(int a) { if(a < 0) a = -a;return a; }

int main() {
    vector <int> A,B,now;
    int p,n,cnt = 1;
    char ch;

    int test; scanf("%d",&test); while(test--) {
        scanf("%d",&n);
        A.clear();
        B.clear();
        now.clear();
        getchar();

        REP(i,n) {
            ch = getchar();
            scanf("%d",&p);
            getchar();
            if(ch == 'O') A.pb(p), now.pb(0);
            else B.pb(p), now.pb(1);
        }

        int diffA = 0, diffB = 0,timer = 0,ia = 0, ib = 0,curA = 1, curB = 1;
        REP(i,sz(now)) {
            if(now[i] == 0) {
                //orange
                int pos = A[ia++];
                if(diffA >= _abs(pos - curA)) {
                    timer++;
                    diffB++;
                    diffA = 0;
                }
                else {
                    int temp = _abs(pos - curA) - diffA;
                    timer += (temp + 1);
                    diffA = 0;
                    diffB += (temp + 1);
                }
                curA = pos;
            }
            else {
                //blue
                int pos = B[ib++];
                if(diffB >= _abs(pos - curB)) {
                    timer++;
                    diffA++;
                    diffB = 0;
                }
                else {
                    int temp = _abs(pos - curB) - diffB;
                    timer += (temp + 1);
                    diffB = 0;
                    diffA += (temp + 1);
                }
                curB = pos;
            }
        }

        printf("Case #%d: %d\n",cnt++,timer);
    }

}
