#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <queue>
#include <stack>

using namespace std;

#define SP printf(" ")
#define NL printf("\n")
#define llu long long unsigned int
#define lli long long int

#define SI(i)       scanf("%d",&i)
#define PI(i)       printf("%d",i)
#define SD(i)       scanf("%lf",&i)
#define PD(i)       printf("%lf",i)
#define SF(i)       scanf("%d",&i)
#define PF(i)       printf("%d",i)
#define SL(i)       scanf("%lld",&i)
#define PL(i)       printf("%lld",i)
#define SLU(i)      scanf("%llu",&i)
#define PLU(i)      printf("%llu",i)
#define SC(i)       scanf("%c",&i)
#define PC(i)       printf("%c",i)
#define SS(i)       scanf("%s",&i)
#define PS(i)       printf("%s",i)
#define PT(i)       printf(i)

#define REP(i,n)    for(int i=0;i<n;i++)
#define FOR(i,a,b)  for(int i=a;i<b;i++)
#define FORR(i,n)   for(int i=n-1;i>=0;i--)

int R,C;
char a[60][60];

bool solve(){
    REP(i,R-1){
        REP(j,C-1){
            if(a[i][j] == '#' && a[i][j+1] == '#' && a[i+1][j] == '#' && a[i+1][j+1] == '#'){
                a[i][j] = '/';
                a[i][j+1] = '\\';
                a[i+1][j] = '\\';
                a[i+1][j+1] = '/';
            }
        }
    }
    REP(i,R){
        REP(j,C){
            if(a[i][j] == '#')
                return false;
        }
    }
    return true;
}

int main(){
    //freopen("input.txt","r", stdin);
    //freopen("output.txt","w", stdout);
    int t;
    SI(t);
    REP(cn,t){
        SI(R);SI(C);
        REP(i,R){
            SS(a[i]);
        }
        PT("Case #");PI(cn+1);PT(":");NL;
        if(solve()){
            REP(i,R){
                REP(j,C){
                    PC(a[i][j]);
                }
                NL;
            }
        }
        else{
            PT("Impossible");NL;
        }
    }
}
