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
char s[2];
int x[100];
char t[100];
int caso;
void doit(){
    int n;
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        scanf("%s%d",s,x+i);
        t[i]=(s[0]=='B'?1:0);
    }
    int res=0;
    int cost[2]={0,0};
    int last[2]={1,1};
    cost[t[0]]+=abs(x[0]-1)+1;
    //printf("%d %d %d\n",0,t[0],cost[t[0]]);
    last[t[0]]=x[0];
    for(int i=1;i<n;++i){
        if(t[i]==t[i-1])cost[t[i]]+=abs(x[i]-x[i-1])+1;
        else{
            cost[t[i]]+=abs(x[i]-last[t[i]])+1;
            //printf("aca=%d %d\n",cost[t[i]],cost[1-t[i]]);
            cost[t[i]]=max(cost[t[i]],cost[1-t[i]]+1);
            //printf("aqui=%d\n",cost[t[i]]);
        }
        last[t[i]]=x[i];
        //printf("%d %d %d\n",i,t[i],cost[t[i]]);
    }
    printf("Case #%d: %d\n",++caso,max(cost[0],cost[1]));
}
int main(){
    int n;
    scanf("%d",&n);
    while(n--)doit();
}
