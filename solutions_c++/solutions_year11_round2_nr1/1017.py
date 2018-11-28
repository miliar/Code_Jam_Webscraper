#include<cstdio>
#include<vector>
#include<iostream>
#include<cstdlib>
#include<cstring>
#include<string>
#include<map>
#include<set>
#include<sstream>
#include<cctype>
#include<cmath>
#include<algorithm>
#include<queue>
#include<deque>
#include<fstream>
using namespace std;
void printArray(int _a[],int _n){
    if(_n==0){
        puts("");
        return;
    }
    printf("%d",_a[0]);
    for(int i=1;i<_n;++i){
        printf(" %d",_a[i]);
    }
    puts("");
}
char t[100][101];

int n;

double wp[100],owp[100],oowp[100];

double f(int x,int banned){
    int won=0,tot=0;
    for(int i=0;i<n;++i)if(t[x][i]!='.'){
        if(i!=banned){
            if(t[x][i]=='1')++won;
            ++tot;
        }
    }
    return won/(double)tot;
}

void doit(){
    scanf("%d",&n);
    gets(t[0]);
    for(int i=0;i<n;++i){
        gets(t[i]);
    }
    for(int i=0;i<n;++i){
        wp[i]=f(i,-1);
        owp[i]=0.0;
        int op=0;
        for(int j=0;j<n;++j)if(t[i][j]!='.'){
            owp[i]+=f(j,i);
            op++;
        }
        owp[i]/=(double)(op);  
    }
    for(int i=0;i<n;++i){
        oowp[i]=0.0;
        int op=0;
        for(int j=0;j<n;++j)if(t[i][j]!='.'){
            oowp[i]+=owp[j];
            ++op;
        }
        oowp[i]/=(double)(op);
    }
    for(int i=0;i<n;++i){
        printf("%.9lf\n",.25*wp[i]+.5*owp[i]+.25*oowp[i]);
    }
}
int main(){
    int T;
    scanf("%d",&T);
    for(int i=1;i<=T;++i){
        printf("Case #%d:\n",i);
        doit();
    }
}
