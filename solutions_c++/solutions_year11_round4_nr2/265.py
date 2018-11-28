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

int C,R,D;
int b[505][505];
bool f(int r, int c, int x){
    int col=0,row=0;
    for(int i=-x; i<=x; i++)
        for(int j=-x; j<=x; j++){
            col+= i* b[r+i][c+j];
            row+= j* b[r+i][c+j];
        }
    col-= -x* ( b[r-x][c-x] + b[r-x][c+x] ) + x*(b[r+x][c-x] + b[r+x][c+x]);
    row-= -x* ( b[r-x][c-x] + b[r+x][c-x] ) + x*(b[r-x][c+x] + b[r+x][c+x]);
    return col==0 && row==0;
}
int solve(int i, int j){
    int mx = min(i,R-i);
    mx = min(mx, min(j,C-j));
    if(!mx) return 0;
    for(int x=mx; x>0; x--){
        if ( f(i,j,x) ) return x;
    }    
    return 0;
}
bool fe(int r, int c, int x){    
    double rc = (x-1)/2.0;
    double cc = (x-1)/2.0;
    double col=0,row=0;
    REP(i,x){
        REP(j,x){
            row += (i-rc)*b[r+i][c+j];
            col += (j-cc)*b[r+i][c+j];            
        }    
    }
    x--;
    row-= -rc*(b[r][c]+b[r][c+x]) + rc*(b[r+x][c]+b[r+x][c+x]);    
    col-= -cc*(b[r][c]+b[r+x][c]) + cc*(b[r+x][c+x]+b[r][c+x]);    
    return abs(row)<1e-4 && abs(col)<1e-4;
}
int solvee(int i, int j){
    int mx = min(R-i,C-j);    
    if(mx<4) return 0;    
    for(int x=mx; x>3; x--){
        if ( fe(i,j,x) ) return x;                
    }        
    return 0;
}

int ntest;
string s;
int main () {
    freopen("B-small-attempt1.in","r",stdin);
    freopen("test.out","w",stdout);
    scanf("%d",&ntest);
    REP(test,ntest){
        printf("Case #%d: ",test+1);  
        scanf("%d %d %d\n",&R,&C,&D);
        memset(b,0,sizeof b);
        REP(i,R){
            getline(cin,s);            
            REP(j,C) b[i][j]=D+ (s[j]-'0');
        }        
        //REP(i,R){ REP(j,C) cout << b[i][j] << " "; cout << endl;}
        int res=0;
        REP(i,R)
            REP(j,C){
                res = max(res,solve(i,j));                                
            }
        if(res) res=res*2+1;
        REP(i,R)
            REP(j,C){                
                res = max(res,solvee(i,j));          
                //cout << i << " "<<j << " "<< res << endl;
            }
        if(res) printf("%d\n",res);
        else printf("IMPOSSIBLE\n");
    }
    return 0;
}
