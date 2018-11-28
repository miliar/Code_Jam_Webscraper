#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <set>
#include <queue>
#include <map>
using namespace std;

#define pii pair<int,int>
#define f first
#define s second
#define mk make_pair

int n;
vector< pii > event;


struct state{
    int dxa,dxb,curr;
    state(){};
    state( int p1, int p2, int p3 ):dxa(p1),dxb(p2),curr(p3){};
};

int visi[105][105][105];

int main(){
    freopen("Ulaz.txt","r",stdin);
    freopen("Izlaz.txt","w",stdout);
    int tests; scanf("%d",&tests);

    for( int t = 1; t <= tests; ++t ){
        scanf("%d",&n);

        event.clear();
        memset( visi,0,sizeof(visi));

        for( int i = 0; i < n; ++i ){
            char c; int dx;
            cin >> c >> dx;
            event.push_back( mk(c,dx) );
        }

        queue< state > q;
        q.push( state(1,1,0) );
        visi[1][1][0] = 1;
        int sol = 10000*20000;

        while( !q.empty() ){
            state u = q.front(); q.pop();

            int a = u.dxa, b = u.dxb, c = u.curr;
            if( c >= n ){
                sol = min(sol,visi[a][b][c]);
                continue;
            }

            for( int i = -1; i <= 1; ++i ){
                for( int j = -1; j <= 1; ++j ){

                    if( a + i < 1 || a + i > 100 || b + j < 1 || b + j > 100 ) continue;
                    int xa = a + i, xb = b + j;

                    bool oki = 1, okj = 1;
                    if( i == 0 && (event[c].f != 'B' || event[c].s != xa) ) oki = false;
                    if( j == 0 && (event[c].f != 'O' || event[c].s != xb) ) okj = false;


                    if( !oki && !okj ) continue;
                    int xc = c + (i==0&&oki || j==0&&okj);

                    if( visi[xa][xb][xc] ) continue;
                    visi[xa][xb][xc] = visi[a][b][c] + 1;


                    q.push( state(xa,xb,xc) );
                }
            }
        }
        printf("Case #%d: %d\n",t,sol-1);

    }

    return 0;
}
