#include <string>
#include <cstring>
#include <vector>
#include <cmath> 
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <utility>
#include <sstream>
#include <iostream>
 
using namespace std;
 
#define REP(a,n) for(int a=0; a<(n); ++a)
#define INIT(a, v) __typeof(v) a = (v)
#define FOREACH(a, v) for (INIT(a, (v).begin()); a!=(v).end(); ++a)
 
template<class T>
inline int size(const T&t){return t.size();}
 
typedef vector<string> vs;
typedef pair<int, int> pii;
typedef long long LL;

#define INF 1000000000
#define PB push_back
#define MP make_pair
 
//////////////////////////////////////////

int N;
int poz[2], kiedy[2];

int main() {
    int TT;
    scanf("%d", &TT);
    REP(tt, TT) {
        scanf("%d", &N);
        poz[0] = poz[1] = 1;
        kiedy[0] = kiedy[1] = 0;
        REP(a, N) {
            char ch;
            int cel;
            scanf(" %c%d", &ch, &cel);
            int nr = ch=='B';
            int odl = abs(cel-poz[nr]);
            kiedy[nr] += odl;
            poz[nr] = cel;
            kiedy[nr] = max(kiedy[!nr], kiedy[nr])+1;
        }
        printf("Case #%d: %d\n", tt+1, max(kiedy[0], kiedy[1]));
    }
}


