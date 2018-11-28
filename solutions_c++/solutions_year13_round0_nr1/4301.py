#include<cmath>
#include<cstdio>
#include<cctype>
#include<vector>
#include<cstring>
#include<cstdlib>
#include<iostream>
#include<algorithm>
using namespace std;

#define sqr(a) (a)*(a)
#define cub(a) (a)*(a)*(a)
#define for1(i,a,b) for(i=(a);i<(b);i++)
#define for2(i,a,b) for(i=(a);i>(b);i--)
#define same(a) memset((a),0,sizeof(a));
#define ll long long

const int MOD = 1000000009;

int cmpint(const void*a,const void *b)
{
    if(((int*)a)[0]==((int*)b)[0])
      return ((int*)a)[1]-((int*)b)[1];
    return ((int*)a)[0]-((int*)b)[0];
}

int a[100005];
char s[10][10];

int fd(char c)
{
    int i,j;
    if(c=='.'){
        for1(i,0,4)
         for1(j,0,4)
          if(s[i][j]==c) return 1;
    }
    int fg;
    for1(i,0,4){
        fg=1;
        for1(j,0,4)
           if(s[i][j]!=c && s[i][j]!='T')
             fg=0;
        if(fg==1) return 1;
    }
    for1(j,0,4){
        fg=1;
        for1(i,0,4)
           if(s[i][j]!=c && s[i][j]!='T')
             fg=0;
        if(fg==1) return 1;
    }
    fg=1;
    for1(i,0,4)
        if(s[i][i]!=c && s[i][i]!='T') fg=0;
    if(fg==1) return 1;
    fg=1;
    for1(i,0,4)
        if(s[i][3-i]!=c && s[i][3-i]!='T') fg=0;
    return fg;
}
int main()
{
    int i,j,n,m,k,l,o,p;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&p);
    for1(o,1,p+1){
        for1(i,0,4) scanf("%s",s[i]);
        printf("Case #%d: ",o);
        n=fd('X');
        m=fd('O');
        if(n==m) {
            if(fd('.')==1 && n==0) printf("Game has not completed\n");
            else printf("Draw\n");
        }
        else if(n==1) printf("X won\n");
        else printf("O won\n");
    }
    return 0;
}
