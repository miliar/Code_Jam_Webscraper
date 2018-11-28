#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <map>
using namespace std;

#define maxn 1024
#define inf 0x7fffffff

int n,m;
map<string,int> Map;
int A[maxn],dp[maxn][maxn];

void input(){ 
     string in;
     Map.clear();
     scanf("%d",&n);
     getchar();
     for(int i=0;i<n;i++){
         getline(cin,in);
         Map[in]=i;
     }
     scanf("%d",&m);
     getchar();
     for(int i=0;i<m;i++){
         getline(cin,in);
         A[i]=Map[in];       
     }
}

int work(){
     for(int i=0;i<m;i++)
        for(int j=0;j<n;j++)dp[i][j]=inf;
     for(int i=0;i<n;i++)if(A[0]!=i)dp[0][i]=0;
     for(int i=1;i<m;i++){
         for(int j=0;j<n;j++)if(A[i]!=j){
              for(int k=0;k<n;k++)if(dp[i-1][k]<inf){
                   if(j==k)dp[i][j]=min(dp[i][j],dp[i-1][k]);
                   else if(j!=k)dp[i][j]=min(dp[i][j],dp[i-1][k]+1);
              }        
         }        
     }
     int res=inf;
     for(int i=0;i<n;i++)res=min(res,dp[m-1][i]);     
     return res;
}

int main(){
    int cases;
    //freopen("a-small.in","r",stdin);
    //freopen("a-small.out","w",stdout);
    //freopen("a-large.in","r",stdin);
    //freopen("a-large.out","w",stdout);
    scanf("%d",&cases);
    for(int i=1;i<=cases;i++){
        input();
        printf("Case #%d: %d\n",i,work());
    }
    return 0;   
}
