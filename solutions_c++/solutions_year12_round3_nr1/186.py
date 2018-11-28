#include <cstdio>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <utility>
#include <queue>
#include <cstring>

using namespace std;

vector <int> adj[1005];
bool seen[1005];

bool dfs(int start){
    if  (seen[start]){
        return true;
    }
    seen[start] = true;
   // for (vector <int>::iterator it = adj[start].begin(); it != adj[start].end(); it++){
   for (int j = 0; j < adj[start].size(); j++){
        if (dfs(adj[start][j])){
            return true;
        }
    }
    return false;
}

int main(){
    int cases;
    int siz;
    bool diamond;
    int to;
    int coun;
    scanf("%d", &cases);
    for (int i = 1; i <= cases; i++){
        scanf("%d", &siz);
        for (int j = 0; j <= siz; j++){
            adj[j].clear();
            seen[j] = false;
        }
        diamond = false;
        for (int j = 1; j <= siz; j++){
            scanf("%d", &coun);
            for (int k = 0; k < coun; k++){
                scanf("%d", &to);
                adj[to].push_back(j);
            } 
        }
        for (int j = 1; j <= siz; j++){
            memset(seen, 0, siz+1);
            diamond = diamond || dfs(j);
        }
        printf ("Case #%d: ", i);
        if (diamond){
            printf("Yes\n");
        } else {
            printf("No\n");
        }
    }
    return 0;
}
