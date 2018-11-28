#include <stdio.h>
#include <string.h>
#include <stack>
#include <algorithm>
#include <vector>
#define MAX 100000
using namespace std;


short int visited[MAX];

vector <vector <int> > edges(MAX);

int dfs(int x,int parent){
    visited[x] = 1;
    for (unsigned int i=0;i<edges[x].size();i++){
        if ( edges[x][i] == parent ) continue;
        if (!visited[edges[x][i]]) { int kl = dfs(edges[x][i],x); if ( kl ) return 1 ; }
        else  return 1;
    }
    return 0;
}

int static inline depth_fs(int x,int n){
    memset(visited,0x00,n*sizeof(short int));
    return dfs(x,-1);
}




void solve(){
    int n;
    scanf("%d",&n);
    for (int i=0;i<n;i++) {
        int m;
        scanf("%d",&m);
        for (int j=0;j<m;j++) {
            int d;
            scanf("%d",&d);
            --d;
            edges[i].push_back(d);
        }
    }
    
    for (int i=0;i<n;i++){
        int x = depth_fs(i,n);
        if ( x ) { 
            
               for (int i=0;i<n;i++)
        while ( !edges[i].empty() ) edges[i].pop_back();
            
            printf("Yes"); return; }
    }
    printf("No");
   
    for (int i=0;i<n;i++) edges[i].clear(); 
    for (int i=0;i<n;i++){
        while ( !edges[i].empty() ) edges[i].pop_back();
  //      if ( edges[i].empty() ) printf("marmota\n");
    //    else printf("<-----\n");
    }
    

}

int main(){
    int t;
    scanf("%d",&t);
    for (int i=1;i<=t;i++){
        printf("Case #%d: ",i);
        solve();
        putchar('\n');
    }
    return 0;
}
