#include <string> 
#include <vector> 
#include <map> 
#include <utility> 
#include <cmath> 
#include <cstdlib> 
#include <cstring> 
#include <queue> 
#include <stack> 
#include <set> 
#include <sstream> 
#include <algorithm> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
using namespace std; 
  
#define INF 0x3f3f3f3f
#define ALL(v) v.begin(),v.end() 
typedef pair<char,int> pci;

int adj[1005][15];
int sz[1005];
int n;
bool cyc;
int seen[1005];

bool dfs(int x){
    seen[x]=1;
    for(int i=0;i<sz[x];i++)
        if(!seen[adj[x][i]]){
            if(dfs(adj[x][i]))
                return true;        
        }else
            return true;
    return false;
}

int main(){
    int test;
    scanf("%d",&test);
    
    for(int tt=1;tt<=test;tt++){      
        printf("Case #%d: ",tt);
        scanf("%d",&n);
        for(int i=0;i<n;i++){
            scanf("%d",&sz[i]);
            for(int j=0;j<sz[i];j++){
                scanf("%d",&adj[i][j]);
                adj[i][j]--;            
            }        
        }
        
        bool cyc=false;
        for(int i=0;i<n;i++){
            memset(seen,0,sizeof(seen));            
            if(dfs(i)){
                cyc=true;
                break;            
            }
        }
        
        if(cyc) printf("Yes");
        else printf("No");
        printf("\n");
    }

    return 0;
}
