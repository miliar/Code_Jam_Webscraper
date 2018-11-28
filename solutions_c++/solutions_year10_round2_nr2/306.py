#include <cstdio>
#include <cstring>

int x[100], v[100];

int main() {
    int nt;
    
    scanf(" %d",&nt);
    for (int ct=1; ct<=nt; ct++) {
        int n,k,b,t;
        scanf(" %d %d %d %d", &n, &k, &b, &t);
        
        for (int i=0; i<n; i++)
            scanf(" %d",&x[i]);
        
        for (int i=0; i<n; i++)
            scanf(" %d",&v[i]);
            
        int acc=0, res=0;
        int dont=0;
        for (int i=n-1; i>=0; i--) {
            if (b-x[i]<=t*v[i]) {
                res+=dont;
                acc++;
                if (acc == k) break;
            }
            else dont++;
        }
        
        if (acc == k)
            printf("Case #%d: %d\n",ct,res);
        else printf("Case #%d: IMPOSSIBLE\n",ct);
    }
    
    return 0;
}
