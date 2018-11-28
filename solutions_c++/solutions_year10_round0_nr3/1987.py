#include <cstdio>
#include <cstring>

long long v[1100];
long long us[1100], ui[1100];

int main() {
    long long r,k,n,nt;
    
    scanf(" %lld",&nt);
    for (long long ct=1; ct<=nt; ct++) {
        scanf(" %lld %lld %lld",&r,&k,&n);
        
        for (long long i=0; i<n; i++) scanf(" %lld",&v[i]);
        
        memset(us, -1, sizeof(us));
        long long res = 0;
        
        long long off=0, tim;
        for (tim=0; tim<r; tim++) {
            if (us[off]!=-1) break;
            us[off]=res;
            ui[off]=tim;
            
            long long acc=0;
            for (long long i=0; i<n && acc+v[off]<=k; i++) {
                acc+=v[off];
                off=(off+1)%n;
            }
            
            res+=acc;
        }
        
        long long clen = tim - ui[off];
        long long cval = res - us[off];
        if (tim < r) {
            res += ((r-tim)/clen)*cval;
            r = (r-tim) % clen;
            
            for (long long i=0; i<r; i++) {
                long long acc=0;
                for (long long i=0; i<n && acc+v[off]<=k; i++) {
                    acc+=v[off];
                    off=(off+1)%n;
                }
            
                res+=acc;
            }
        }
        printf("Case #%lld: %lld\n", ct, res);
    }
        
    return 0;
}
