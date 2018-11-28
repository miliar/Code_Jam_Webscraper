#include <string>
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
 
template<class T>
inline int size(const T&t){return t.size();}
 
typedef vector<string> vs;

#define PB push_back
 
//////////////////////////////////////////

int L,D,N;

vs words;

bool jest[15][256];

int main() {
    char buf[100000];
    scanf("%d%d%d",&L,&D,&N);
    REP(a, D) {
        scanf("%s", buf);
        words.PB(buf);
    }
    REP(t, N) {
        scanf("%s", buf);
        REP(a, L) REP(b, 256) jest[a][b] = 0;
        int p = 0;
        REP(a, L) {
            if (buf[p]!='(') {
                jest[a][buf[p++]] = 1;
                continue;
            }
            while (buf[++p]!=')')
                jest[a][buf[p]] = 1;
            ++p;
        }
        int ile = 0;
        REP(a, D) {
            REP(b, L)
                if (!jest[b][words[a][b]])
                    goto nie;
            ++ile;
          nie:;
        }
        printf("Case #%d: %d\n", t+1, ile);
    }
}