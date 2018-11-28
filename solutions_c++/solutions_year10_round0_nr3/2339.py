#include<cstdio>
#include<algorithm>
using namespace std;

int g[10000001];
int root;
int moneyEarned;

int t;
int r,k,n;

int main(){
  freopen("C-small-attempt0.in", "r", stdin);
  freopen("out.out", "w", stdout);
    
    scanf("%d", &t);
    for(int i=1; i<=t; ++i){
        root = 0;
        moneyEarned = 0;
        scanf("%d%d%d", &r, &k, &n);
        for(int j=0; j<n; ++j){
            scanf("%d", &g[root++]);
        }
        root=0;
        
        while(r>0){
            int fixedSize=0;
            int begin=root;

            while(1){
                if(fixedSize+g[root]<=k){
                    fixedSize+=g[root];
                    root = (root+1)%n;
                    if(root==begin)
                        break;
                }else{
                     break;
                }
            }
            moneyEarned+=fixedSize;
            
            r--;
        }
        
        printf("Case #%d: %d\n", i, moneyEarned);
    }
    return 0;
}
