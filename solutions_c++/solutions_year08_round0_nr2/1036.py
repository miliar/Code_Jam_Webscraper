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

int main() {
    int tcase;
    int ttime;
    int a,b,c,d;
    
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);    
    
    cin >> tcase;
    REP(xx, tcase) {
        cin >> ttime;
        struct { int n, ntrain[1600], depart[1600]; VI arr[1600]; } left, right;
       
        CLEAR( left.depart ); CLEAR( right.depart );
        REP(i,1600) left.arr[i].clear(), right.arr[i].clear();
        
        // main input routine
        cin >> left.n  >> right.n;
        REP(i, left.n) {
            scanf("%d:%d %d:%d",&a, &b, &c, &d);
            int departingt = a*60 + b;
            int arrivingt = c*60 + d;
            
            left.depart[ departingt ]++;
            left.arr[ departingt ].pb(arrivingt);            
        }
        
        
        REP(i, right.n) {
            scanf("%d:%d %d:%d",&a, &b, &c, &d);
            int departingt = a*60 + b;
            int arrivingt = c*60 + d;
            
            right.depart[ departingt ]++;
            right.arr[ departingt ].pb(arrivingt);            
        }
        
        // now checking
        REP(sum,500) {
            bool possible = false;
            REP(na,sum+1) {
                int nb = sum - na;
                CLEAR( left.ntrain ); CLEAR( right.ntrain );
                
                possible = true;
                left.ntrain[0] = na;
                right.ntrain[0] = nb;
                
                REP(time,1440) {
                    if( time != 0 ) {
                        left.ntrain[ time ] += left.ntrain[ time-1 ];
                        right.ntrain[ time ] += right.ntrain[ time-1 ];                      
                    }
                    
                    if( left.depart[ time ] ) {
                        REP(i, left.arr[ time ].sz ) {
                            int x = left.arr[ time ][i];
                            right.ntrain[ x + ttime ]++;
                            left.ntrain[ time ]--;
                        }
                        if( left.ntrain[ time ] < 0 ) {
                            possible = false;
                            break;
                        } 
                    }
                    
                    if( right.depart[ time ] ) {
                        REP(i, right.arr[ time ].sz ) {
                            int x = right.arr[ time ][i];
                            left.ntrain[ x + ttime ]++;
                            right.ntrain[ time ]--;
                        }
                        if( right.ntrain[ time ] < 0 ) {
                            possible = false;
                            break;
                        } 
                    }
                }
                
                if( possible ) {
                    printf("Case #%d: %d %d\n",xx+1,na,nb);
                    break;
                }
            }
            if( possible ) break;
        }
        
    }

    //system("pause");
    
    return 0;
}
