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
int t[1001];
char v[1001];
int caso;
bool doit(){
    int n;
    scanf("%d",&n);
    for(int i=1;i<=n;++i){
        v[i]=0;
        scanf("%d",t+i);
    }
    int res=0;
    for(int i=1;i<=n;++i)if(!v[i]){
        int ct=1;
        v[i]=1;
        int j=t[i];
        while(j!=i){
            ct++;
            v[j]=1;
            j=t[j];
        }
        if(ct>1)res+=ct;
    }
    printf("Case #%d: %d\n",++caso,res);
}
int main(){
    int n;
    scanf("%d",&n);
    while(n--)doit();
}
