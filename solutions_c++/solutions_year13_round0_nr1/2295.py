#include <cmath>
#include <ctime>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <functional>
#include <algorithm>
#include <iostream>
#include <numeric>
#include <iomanip>
#include <sstream>
#include <bitset>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <list>
#include <set>
#include <map>
using namespace std;

#define debug(args...) fprintf(stderr,args)
#define foreach(_it,_v) for(typeof(_v.begin()) _it = _v.begin(); _it != _v.end(); ++_it)

typedef long long lint;
typedef pair<int,int> pii;
typedef pair<lint,lint> pll;

const int INF = 0x3f3f3f3f;
const lint LINF = 0x3f3f3f3f3f3f3f3fll;

char m[5][5];

int main() {
    int T;
    scanf("%d",&T);
    for(int t=1;t<=T;++t) {
        bool x=0,o=0;
        bool xwon,owon;
        for(int a=0;a<4;++a)
            for(int b=0;b<4;++b)
                scanf(" %c",&m[a][b]);
        for(int a=0;a<4 && !x && !o;++a) {
            xwon = 1, owon = 1;
            for(int b=0;b<4;++b) {
                if(m[a][b] != 'X' && m[a][b] != 'T') xwon = 0;
                if(m[a][b] != 'O' && m[a][b] != 'T') owon = 0;
            }
            if(xwon) x = 1;
            if(owon) o = 1;
        }
        for(int a=0;a<4 && !x && !o;++a) {
            xwon = 1, owon = 1;
            for(int b=0;b<4;++b) {
                if(m[b][a] != 'X' && m[b][a] != 'T') xwon = 0;
                if(m[b][a] != 'O' && m[b][a] != 'T') owon = 0;
            }
            if(xwon) x = 1;
            if(owon) o = 1;
        }
        xwon = 1, owon = 1;
        if(!x && !o) {
            for(int a=0;a<4 && !x && !o;++a) {
                if(m[a][a] != 'X' && m[a][a] != 'T') xwon = 0;
                if(m[a][a] != 'O' && m[a][a] != 'T') owon = 0;
            }
            if(xwon) x = 1;
            if(owon) o = 1;
            xwon = 1, owon = 1;
        }
        if(!x && !o) {
            for(int a=0;a<4 && !x && !o;++a) {
                if(m[a][3-a] != 'X' && m[a][3-a] != 'T') xwon = 0;
                if(m[a][3-a] != 'O' && m[a][3-a] != 'T') owon = 0;
            }
            if(xwon) x = 1;
            if(owon) o = 1;
        }
        printf("Case #%d: ",t);
        if(!x && !o) {
            bool filled = 1;
            for(int a=0;a<4;++a)
                for(int b=0;b<4;++b)
                    if(m[a][b] == '.') filled = 0;
            if(filled) printf("Draw\n");
            else printf("Game has not completed\n");
        }
        else if(x) printf("X won\n");
        else printf("O won\n");
    }
    return 0;
}
