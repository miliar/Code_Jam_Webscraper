//+++++++++++++++++++++++++++++//
//      Karan Aggarwal         //
//       IIIT-Hyderabad        //
//+++++++++++++++++++++++++++++//
// Topic: 
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<limits.h>
#include<math.h>
#define si(n) scanf("%d",&n)
#define rep(i,n) for(i=0;i<n;i++)
#define REP(i,a,b) for(i=a;i<b;i++)
#define pn printf("\n")
#define pw printf(" ")
#define pi(n) printf("%d",n)
#define pll(n) printf("%lld",n)
#define sll(n) scanf("%lld",&n)
#define ss(s) scanf("%s",s)
#define ps(s) printf("%s",s)
typedef long long LL;
//inline int readint(){int n=0;char c;while(1){ c=getchar_unlocked();if(c=='\n'||c==' '||c==EOF)break;n=(n<<3) + (n<<1) +c-'0';}return n;}
//inline long long readlonglong(){long long n=0;char c;while(1){ c=getchar_unlocked();if(c=='\n'||c==' '||c==EOF)break;n=(n<<3) + (n<<1) +c-'0';}return n;}
int abs(int a){ if(a<0)return -1*a; return a;}
int big(int a,int b){if(a>b)return a;return b;}
int small(int a,int b){if(a<b)return a;return b;}
int compare(const void *a, const void *b)
{
    int *p1=(int*)a;
    int *p2=(int*)b;
    return *p1-*p2;
}
//++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
int main()
{
    int A,B,isa,isb,ise,te,m,l,T,ans,sum,min,max,n,i,j,k,x,y,t;
    char s[4][5];
    si(t);T=t;
    while(t--)
    {
        rep(i,4)
            ss(s[i]);
        A=B=0;
        te=0;
        rep(i,4)
        {
            if(A || B)break;
            ise=0;isa=0;isb=0;
            rep(j,4)
            {
                if(s[i][j]=='X')isa=1;
                if(s[i][j]=='O')isb=1;
                if(s[i][j]=='.')ise=1;
            }
            if (ise)
            {
                te=1;continue;
            }
            if (!isb && isa)A=1;
            if (isb && !isa)B=1;
        }
        rep(i,4)
        {
            if(A || B)break;
            ise=0;isa=0;isb=0;
            rep(j,4)
            {
                if(s[j][i]=='X')isa=1;
                if(s[j][i]=='O')isb=1;
                if(s[j][i]=='.')ise=1;
            }
            if (ise)
            {
                te=1;continue;
            }
            if (!isb && isa)A=1;
            if (isb && !isa)B=1;
        }
        if(!A && !B)
        {
            ise=0;isa=0;isb=0;
            rep(j,4)
            {
                if(s[j][j]=='X')isa=1;
                if(s[j][j]=='O')isb=1;
                if(s[j][j]=='.')ise=1;
            }
            if (ise)
                te=1;
            else
            {
            if (!isb && isa)A=1;
            if (isb && !isa)B=1;
            }

        }
        if(!A && !B)
        {
            ise=0;isa=0;isb=0;
            rep(j,4)
            {
                if(s[3-j][j]=='X')isa=1;
                if(s[3-j][j]=='O')isb=1;
                if(s[3-j][j]=='.')ise=1;
            }
            if (ise)
                te=1;
            else
            {
            if (!isb && isa)A=1;
            if (isb && !isa)B=1;
            }

        }
        if(A)
            printf("Case #%d: X won\n",T-t);
        else if(B)
            printf("Case #%d: O won\n",T-t);
        else if(te)
            printf("Case #%d: Game has not completed\n",T-t);
        else
            printf("Case #%d: Draw\n",T-t);
    }
    return 0;
}

