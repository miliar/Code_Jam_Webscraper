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
char t[50][51];
int R,C;
bool doit(){
    scanf("%d%d",&R,&C);
    for(int i=0;i<R;++i)scanf("%s",t+i);
    for(int i=0;i<R;++i){
        for(int j=0;j<C;++j){
            if(t[i][j]=='#'&&j+1<C&&i+1<R&&t[i][j+1]=='#'&&t[i+1][j]=='#'&&t[i+1][j+1]=='#'){
                t[i][j]=t[i+1][j+1]='/';
                t[i][j+1]=t[i+1][j]='\\';
                /*for(int i=0;i<R;++i)puts(t[i]);
                puts("");*/
            }
        }
    }
    for(int i=0;i<R;++i){
        for(int j=0;j<C;++j){
            if(t[i][j]=='#')return false;
        }
    }
    return true;
}
int main(){
    int T;
    scanf("%d",&T);
    for(int i=1;i<=T;++i){
        printf("Case #%d:\n",i);
        if(!doit())puts("Impossible");
        else{
            for(int i=0;i<R;++i)puts(t[i]);
        }
    }
}
