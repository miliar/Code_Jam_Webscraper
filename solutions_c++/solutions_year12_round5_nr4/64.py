#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string.h>
#include <math.h>
using namespace std;

int a[120][120];
char s[1200];
int id[400];
bool bi[120];
int rd[120],cd[120];
int n,m,k,nn,ans,p1;

char ch(char c){
    if (c=='o') return '0';
    if (c=='i') return '1';
    if (c=='e') return '3';
    if (c=='a') return '4';
    if (c=='s') return '5';
    if (c=='t') return '7';
    if (c=='b') return '8';
    if (c=='g') return '9';
    return c;
}

void add(char c1,char c2){
    if (id[c1]==0) id[c1]=(++nn);
    if (id[c2]==0) id[c2]=(++nn);
    if (a[id[c1]][id[c2]]==0){
        ++rd[id[c2]];
        ++cd[id[c1]];
        a[id[c1]][id[c2]]=1;
//        printf("%d %d\n",id[c1],id[c2]);
        ans++;
    }
}

void gao(char c1,char c2){
    add(c1,c2);
    add(ch(c1),c2);
    add(c1,ch(c2));
    add(ch(c1),ch(c2));
}

int p2;

void dfs(int k){
    bi[k]=false;
    if (rd[k]!=cd[k]) p2=0;
    p1+=abs(rd[k]-cd[k]);
    for (int i=1;i<=nn;++i)
        if (a[k][i] && bi[i]) dfs(i);
}
    
int main(){
    int _,cas=0;
    scanf("%d",&_);
    while (_--){
        nn=0;
        ans=0;
        memset(a,0,sizeof(a));
        memset(id,0,sizeof(id));
        memset(rd,0,sizeof(rd));
        memset(cd,0,sizeof(cd));
        memset(bi,true,sizeof(bi));
        
        scanf("%d",&k);
        scanf("%s",s);
        for (int i=1;i<strlen(s);++i)
            gao(s[i-1],s[i]);
        
        p1=0;
        for (int i=1;i<=nn;++i)
            if (bi[i]){ 
                p2=2;
                dfs(i);
                p1+=p2;
            }
        ans+=p1/2;
        printf("Case #%d: %d\n",++cas,ans);
    }
    return 0;
}
        
