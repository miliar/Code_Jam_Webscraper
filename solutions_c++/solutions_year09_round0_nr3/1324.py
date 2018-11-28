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
 
template<class T>
inline int size(const T&t){return t.size();}
 
typedef vector<string> vs;

#define INF 1000000000
#define PB push_back
 
//////////////////////////////////////////

int T;
char buf[10000];
string s = "welcome to code jam";
int len = size(s);
int tab[1000][39];
int dl;

int main() {
    scanf("%d ",&T);
    REP(t, T) {
        fgets(buf, 10000, stdin);
        dl = strlen(buf);
        if (buf[dl-1]=='\n') --dl;
        REP(a, dl+1) REP(b, len+1) tab[a][b] = 0;
        tab[0][0] = 1;
        REP(a, dl) {
            REP(b, len+1)
                tab[a+1][b] = tab[a][b];
            REP(b, len)
                if (buf[a]==s[b])
                    tab[a+1][b+1] = (tab[a+1][b+1]+tab[a][b])%10000;
        }
        printf("Case #%d: %.4d\n", t+1, tab[dl][len]);
    }
}