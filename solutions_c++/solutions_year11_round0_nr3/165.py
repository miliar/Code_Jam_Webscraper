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
int caso;
bool doit(){
    int n,x;
    scanf("%d",&n);
    int mini=1000001,ac=0,sum=0;
    for(int i=0;i<n;++i){
        scanf("%d",&x);
        ac^=x;
        mini=min(mini,x);
        sum+=x;
    }
    printf("Case #%d: ",++caso);
    if(!ac)printf("%d\n",sum-mini);
    else puts("NO");
}
int main(){
    int n;
    scanf("%d",&n);
    while(n--)doit();
}
