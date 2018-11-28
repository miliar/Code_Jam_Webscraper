#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <string>
#include <memory.h>

#define oo 1000000005
#define eps 1e-11

#define REP(i,n) for(int i = 0, _n = (n); i < _n; i++)
#define REPD(i,n) for(int i = (n) - 1; i >= 0; i--)
#define FOR(i,a,b) for (int i = (a), _b = (b); i < _b; i++)
#define FORD(i,a,b) for (int i = (a), _b = (b); i > _b; i--)
#define RESET(c,x) memset (c, x, sizeof (c))

#define PB push_back
#define MP make_pair
#define F first
#define S second

using namespace std;

int ntest,n;
vector< pair<double, double> > vt;
double X,S,R,t,E,B,w;
int N;
int main () {
    freopen("A-large.in","r",stdin);
    freopen("test.out","w",stdout);
    scanf("%d",&ntest);
    REP(test,ntest){
        printf("Case #%d: ",test+1);   
        scanf("%lf %lf %lf %lf %d", &X, &S,&R,&t,&N);
        R-=S;
        vt.clear();        
        REP(i,N){
            scanf("%lf %lf %lf",&B,&E,&w);
            X-= (E-B) ;
            vt.PB(MP(w+S,E-B));            
        }
        vt.PB(MP(S,X));
        sort(vt.begin(),vt.end());
        int c=0, n=vt.size();
        double r=0;
        while(c<n){
            double sp = vt[c].F, l = vt[c].S;
            c++;
            if( t*(sp+R) > l ){ 
                t-= 1.0*l/(sp+R); 
                r+= l/(sp+R);
            }
            else{
                double temp = t*(sp+R);                
                l-=temp;               
                r+= t + l/sp; 
                break;
            }            
        }        
        FOR(i,c,n) r+= vt[i].S/vt[i].F;
        printf("%.9lf\n",r);
    }
    return 0;
}
