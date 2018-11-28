#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int main() {
    int t;
    scanf("%d",&t);
    for(int i = 1;i <= t;i++) {    
            int n,l,h;
            scanf("%d %d %d",&n,&l,&h);
            int f[110];
            for(int j = 0;j < n;j++) 
                    scanf("%d",&f[j]);
            int aux = 0;
            int freq;
            for(int k = l;k <= h;k++) {
                    if(aux) break;        
                    for(int j = 0;j < n;j++) {
                            if(max(k,f[j])%min(k,f[j]) != 0) break;
                            if(j == n-1) {
                                    freq = k;
                                    aux = 1;
                                    break;
                            }
                    }
            }
            if(!aux) printf("Case #%d: NO\n",i);
            else printf("Case #%d: %d\n",i,freq);
    }
    return 0;
}
