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
#define N 100
int a[N];
int n;


bool f(int freq){
    for(int i=0;i<n;++i){
        if(freq%a[i]!=0&&a[i]%freq!=0)return false;
    }
    return true;
}

int doit(){
    int lo,hi;
    scanf("%d%d%d",&n,&lo,&hi);
    for(int i=0;i<n;++i)scanf("%d",a+i);
    for(int i=lo;i<=hi;++i){
        if(f(i))return i;
    }
    return -1;
}
int main(){
    int T;
    scanf("%d",&T);
    for(int i=1;i<=T;++i){
        printf("Case #%d: ",i);
        int temp=doit();
        if(temp!=-1)printf("%d\n",temp);
        else puts("NO");
    }
}
