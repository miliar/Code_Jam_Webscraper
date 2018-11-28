#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>

#include<cmath>
#include<iostream>
#include<fstream>
#include<numeric>

#include<string>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<set>
#include<sstream>
#include<stack>
#include<list>
#include<iterator>
using namespace std;

#define REP(i,n) for(__typeof(n) i=0; i<(n); i++)
#define FOR(i,a,b) for(__typeof(b) i=(a); i<=(b); i++)
#define CLEAR(t) memset((t), 0, sizeof(t))

#define sz size()
#define pb push_back
#define pf push_front

#define VI vector<int>
#define VS vector<string>
#define LL long long

struct point {
    LL x, y;
};

point p[1000];

int main() {
    LL N;
    LL n, A, B, C, D, x0, y0, M;
    int ncase = 0;
    
    freopen("A3.in","r",stdin);
    freopen("A3.out","w",stdout);
    
    cin >> N;
    while( N-- ) {
        cin >> n >> A >> B >> C >> D >>  x0 >> y0 >> M;
        int X,Y; 
        
        
        X = x0, Y = y0;
        p[0].x = X, p[0].y = Y;
        FOR(i,1,n-1) {
            X = (A * X + B) % M;
            Y = (C * Y + D) % M;
            p[i].x = X, p[i].y = Y;
        }
        
        LL count = 0;
        FOR(i,0,n-1)
        FOR(j,i+1,n-1) 
        FOR(k,j+1,n-1) {
            X = (p[i].x + p[j].x + p[k].x );
            Y = (p[i].y + p[j].y + p[k].y );
            if( X % 3 == 0 && Y % 3 == 0 ) count++;
        }
        
        printf("Case #%d: %lld\n",++ncase,count);
        
    }
    
    //system("pause");
    return 0;
}
