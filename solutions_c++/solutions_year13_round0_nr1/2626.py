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
 
typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef pair<int,int> II;
typedef vector<II> VII;
typedef vector<VII> VVII;
typedef vector<VI> VVI;
 
#define INF 2000000000
#define INFLL (1LL<<62)
#define FI first
#define SE second
#define PB push_back
#define SS ({int x;scanf("%d", &x);x;})
#define SSL ({LL x;scanf("%lld", &x);x;})
#define rep(i,n) for(i=0;i<(n);i++)
#define SSF getint()
#define _mp make_pair
 
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
 
/********************* FAST IO *********************************/
 
#define BUFSIZE (10000)
 
char inputbuffer[BUFSIZE];
char *ioptr=inputbuffer+BUFSIZE,*ioend=inputbuffer+BUFSIZE;
int input_eof=0;
 
#define getchar() ({if (ioptr >= ioend) init_input(); *ioptr++;})
#define eof() (ioptr>=ioend && input_eof)
#define eoln() ({if(ioptr >= ioend) init_input(); *ioptr == '\n';})
 
void init_input()
{
        if (input_eof)
                return;
        int existing = BUFSIZE - (ioend - inputbuffer);
        memcpy(inputbuffer, ioend, existing);
        int wanted = ioend - inputbuffer;
        int count=fread(inputbuffer + existing, 1, wanted, stdin);
        if (count < wanted)
                input_eof = 1;
        ioend = inputbuffer + BUFSIZE - (wanted - count);
        while (*--ioend > ' ');
        ioend++;
        ioptr=inputbuffer;
}
 
inline void non_whitespace()
{
        for(;;)
        {
                if(ioptr>=ioend)
                        init_input();
                if(*ioptr>' ')
                        return;
                ioptr++;
        }
}
 
inline int getint()
{
        non_whitespace();
        int n=0;
        while(*ioptr>' ')
                n=(n<<3)+(n<<1)+*ioptr++-'0';
        ioptr++;
        return n;
}
 
//******************************** programme code starts here*************************//
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
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t=SS,ans,p,q,i,j,d,c;
    string A[4];
    for(q=0;q<t;q++){
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
