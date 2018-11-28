#include <stdio.h>
#include <math.h>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

int adj[101][101];

int main(){
    int ntc, ttc=0;
    scanf("%d", &ntc);
    while (ntc--){
        int n;
        memset(adj,0,sizeof(adj));
        scanf("%d", &n);
        
        for (int i=1;i<n;i++){
            int a,b;
            scanf("%d%d", &a,&b);
            a--;b--;
            adj[a][b]=1;
            adj[b][a]=1;
        }
        vector<int> order;
        
        for (int i=0;i<n;i++){
            order.push_back(i);    
        }
        
        vector<pair<int,int> > el;
        int m;
        scanf("%d", &m);
        while (--m){
            int a,b;
            a--;b--;
            scanf("%d%d", &a,&b);
            el.push_back(make_pair(a,b));
        }
        
        int found = 0;
        do {
            int valid=1;
            for (int i=0;i<el.size();i++){
                if (!adj[order[el[i].first]][order[el[i].second]]){
                    valid=0;
                    break;}
            }
            if (valid){
                found = 1 ;
                break;
            }
        } while (next_permutation(order.begin(), order.end()));
        
        if (found)
          printf("Case #%d: YES\n",++ttc);
        else
          printf("Case #%d: NO\n",++ttc);
        
    }
    return 0;
}
