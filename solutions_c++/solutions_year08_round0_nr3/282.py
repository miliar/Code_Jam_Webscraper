#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <queue> 
#include <iostream>
#include <iterator>
#include <math.h>
#include <cstdio>
#include <cstdlib>
#include <sstream>

#pragma comment(linker, "/STACK:60777216")

using namespace std;

#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++) 
#define REP(i,n) FOR(i,0,n)
#define UNIQUE(v) SORT(c),v.erase(unique(v.begin(),v.end()),v.end())
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define ld long double
#define ll long long
#define pb push_back
#define pii pair<int,int>
#define Y second
#define X first

#define INF 1000000000
#define Pi acosl(-1.0)
#define eps 1e-9

ld sq(ld x){return x*x;}

int N,tc;
ld f,R,t,r,g,st;

ld hor(ld x,ld R){
    return R*R*asinl(x/2/R)-x/2*sqrt(R*R-x*x/4);
}

ld square(ld a,ld b,ld R){
    return a*b/2+hor(hypot(a,b),R);
}


ld square2(ld a,ld b,ld R){
    return a*b/2-hor(hypot(a,b),R);
}

int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>N;
    REP(tc,N){
        cin>>f>>R>>t>>r>>g;
        
        st=R-t-f;           
       
        if(g<2*f+eps){
            printf("Case #%d: %.6lf\n",tc+1,1.);
            continue;
        }
        vector<double> v;
        ld x[2];
        ld y[2];
        ld P=0;
        FOR(i,0,2001)
            FOR(j,0,2001){
                x[0]=i*(2*r+g)+r+f;
                y[0]=j*(2*r+g)+r+f;
                x[1]=i*(2*r+g)+r+g-f;
                y[1]=j*(2*r+g)+r+g-f;
ld R=st;
                if(hypot(x[0],y[0])-eps>st) continue; // empty
                if(hypot(x[1],y[1])+eps<=st) P+=(x[1]-x[0])*(y[1]-y[0]); //full circle
                else if(hypot(x[1],y[0])+eps>=st && hypot(x[0],y[1])+eps>=st)
                    P+=square(sqrt(R*R-x[0]*x[0])-y[0],sqrt(R*R-y[0]*y[0])-x[0],st);
                else if(hypot(x[1],y[0])-eps<=st && hypot(x[0],y[1])-eps<=st) 
                    P+=(x[1]-x[0])*(y[1]-y[0])-square2(y[1]-sqrt(R*R-x[1]*x[1]),x[1]-sqrt(R*R-y[1]*y[1]),st);
                else if(hypot(x[0],y[1])-eps<=st){
                    ld X=sqrt(R*R-y[1]*y[1]);
                    P+=(X-x[0])*(y[1]-y[0])+square(sqrt(R*R-y[0]*y[0])-X,y[1]-y[0],R);
                }else if(hypot(x[1],y[0])-eps<=st){
                    ld aa=sqrt(R*R-x[1]*x[1]);
                    P+=(aa-y[0])*(x[1]-x[0])+square(sqrt(R*R-x[0]*x[0])-aa,x[1]-x[0],R);
                }

            }
        ld TS=Pi*sq(R);
        printf("Case #%d: %.6lf\n",tc+1,1-4*P/TS);
    }
	return 0;
}