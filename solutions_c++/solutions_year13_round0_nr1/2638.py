#include<stdio.h>
#include<string.h>
#include<math.h>
#include<ctype.h>
#include<stdlib.h>
#include<iostream>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<stack>
 
using namespace std;
#define rep(i,n) for(i=0;i<(n);i++)

inline void _min(int &a,int b)
{
        if(a>b)
                a=b;
}
inline void _max(int &a,int b)
{
        if(a<b)
                a=b;
}
 

 


int checker_coler(string A[]){
    int i,j,X,O,T;
    rep(j,4){
        X=O=T=0;
        rep(i,4){
        if(A[i][j]=='X')
            X++;
        else if(A[i][j]=='O')
            O++;
        else if(A[i][j]=='T')
            T++;
        }
        if((X==3 && T==1)|| (X==4))
            return 1;
        else if((O==3 && T==1)|| (O==4))
            return 2;
    }
    return 0;
}
int checker_rower(string A[]){
    int i,j,X,O,T;
    rep(i,4){
        X=O=T=0;
        rep(j,4){
        if(A[i][j]=='X')
            X++;
        else if(A[i][j]=='O')
            O++;
        else if(A[i][j]=='T')
            T++;
        }
        if((X==3 && T==1)|| (X==4))
            return 1;
        else if((O==3 && T==1)|| (O==4))
            return 2;
    }
    return 0;
}
int XX[2][4]={{0,1,2,3},{0,1,2,3}};
int YY[2][4]={{0,1,2,3},{3,2,1,0}};
int checker_diaer(string A[]){
        int i,j,X,T,O;
        rep(i,2){
        X=O=T=0;
        rep(j,4){
        if(A[XX[i][j]][YY[i][j]]=='X')
            X++;
        else if(A[XX[i][j]][YY[i][j]]=='O')
            O++;
        else if(A[XX[i][j]][YY[i][j]]=='T')
            T++;
        }
        if((X==3 && T==1)|| (X==4))
            return 1;
        else if((O==3 && T==1)|| (O==4))
            return 2;
    }
    return 0;
}
int main(){
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t,ans,p,q,i,j,d,c;
    scanf("%d", &t);
    string A[4];
    for(q=0;q<t;q++){
        rep(i,4) cin>>A[i];
    p=checker_rower(A);
    if(p==1){
        printf("Case #%d: X won\n",q+1);
    }
    else if(p==2){
        printf("Case #%d: O won\n",q+1);
    }
    else {
        c=checker_coler(A);
        if(c==1){
        printf("Case #%d: X won\n",q+1);
    }
    else if(c==2){
        printf("Case #%d: O won\n",q+1);
    }
    else {
        d=checker_diaer(A);
        if(d==1){
        printf("Case #%d: X won\n",q+1);
    }
    else if(d==2){
        printf("Case #%d: O won\n",q+1);
    }
    else {
        ans=1;
        rep(i,4)
            rep(j,4)
                ans= ans & (A[i][j]=='.'?0:1);
        if(!ans){
            printf("Case #%d: Game has not completed\n",q+1);
        }
        else
             printf("Case #%d: Draw\n",q+1);
    }
    }
    }
    }
    return 0;
}
