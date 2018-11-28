#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<vector>
using namespace std;
const int maxn = 100*1024;
int a[maxn];
vector<int> g[maxn];
bool u[maxn];
bool dfs(int v){
     u[v]=1;
     unsigned j;
     for(j=0;j<(int)g[v].size();j++)
         if(u[g[v][j]])
             return 1;
        else
             if(dfs(g[v][j]))
                     return 1;
   return 0;
}
bool solve(){
    int n;
    scanf("%d",&n);
       int i;
       for(i=0;i<n;i++)
           g[i].clear();
    for(i=0;i<n;i++)
    {int v,k;
        scanf("%d",&k);
        a[i]=k;
        for(int j=0;j<k;j++){
            scanf("%d",&v);
            v--;
            g[v].push_back(i);
        }
    }
    for(i=0;i<n;i++)
        if(a[i]==0){
            memset(u,0,sizeof(bool)*n);
            if(dfs(i) )
                return 1;
        }
    return 0 ;
}
int main(){
#ifdef _DEBUG
        freopen("in.txt","r",stdin);
        freopen("out.txt","w",stdout);
#endif

        int v,i,min;
        int n;
        int t;
        scanf("%d",&t);
        for(int I=1;I<=t;I++){
            printf("Case #%d: ",I);
            if(solve())
                puts("Yes");
            else puts("No");

        }
}
