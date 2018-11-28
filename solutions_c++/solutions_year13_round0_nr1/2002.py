#include<stdio.h>
#include<string>
#include<iostream>

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

int check_col(string A[]){
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
int check_row(string A[]){
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
int check_dia(string A[]){
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
    int t,ans,p,q,i,j,d,c;
    scanf("%d",&t);
    string A[4];
    rep(q,t){
        rep(i,4) cin>>A[i];
    p=check_row(A);
    if(p==1){
        printf("Case #%d: X won\n",q+1);
    }
    else if(p==2){
        printf("Case #%d: O won\n",q+1);
    }
    else {
        c=check_col(A);
        if(c==1){
        printf("Case #%d: X won\n",q+1);
    }
    else if(c==2){
        printf("Case #%d: O won\n",q+1);
    }
    else {
        d=check_dia(A);
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