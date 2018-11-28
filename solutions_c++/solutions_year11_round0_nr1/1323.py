#include<iostream>
#include<cstring>
#include<cmath>
#include<cstdio>
#include<algorithm>
using namespace std;

int getint(){
    char c;
    while (!isdigit(c=getchar())) {}
    int ret=c-'0';
    while (isdigit(c=getchar())) ret=ret*10+c-'0';
    return ret;
}

char getorder(){
     char c;
     while (!isalpha(c=getchar())) {}
     return c;
}

int n,pos[3],t[3];

int solve(){
    n=getint();
    pos[0]=1,pos[1]=1;
    t[0]=0,t[1]=0;
    for (int i=1;i<=n;i++) {
        int temp;
        char tc=getorder();
        int p=getint();
        if (tc=='O') temp=0; else temp=1;
        t[temp]+=abs(pos[temp]-p)+1;
        if (t[temp]<=t[temp^1]) t[temp]=t[temp^1]+1;
        pos[temp]=p;
    }
    return max(t[0],t[1]);
}

int main(){
    
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    
    int test;
    //scanf("%d",&test);
    test=getint();
    for (int i=1;i<=test;i++) {
        int ans=solve();
        printf("Case #%d: %d\n",i,ans);
    }
    
    
    return 0;
}
