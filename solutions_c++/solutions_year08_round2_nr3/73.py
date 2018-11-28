#include <stdio.h>
#include <deque>
using namespace std;

int res [1000100];
int main(){
    int ntc,ttc=0;
    scanf("%d", &ntc);
    while (ntc--){
        int n,q;        
        scanf("%d%d", &n,&q);
        
        deque<int> frepos;
        for (int i=1;i<=n;i++){
            frepos.push_back(i);
        }
        
        for (int i=1;i<=n;i++){
            for (int j=1;j<i;j++){
                int x = frepos.front();
                frepos.pop_front();
                frepos.push_back(x);                
            }
            int y = frepos.front();
            frepos.pop_front();
            res[y] = i;
        }
        
        printf("Case #%d:", ++ttc);
                
        for (int i=0; i<q;i++){
            int x;
            scanf("%d", &x);
            printf(" %d", res[x]);            
        }
        puts("");
    }
    
    return 0;
}
