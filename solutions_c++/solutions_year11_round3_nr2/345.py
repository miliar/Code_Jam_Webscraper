#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<cmath>
#include<cstring>
#define LL long long
using namespace std;
bool ss(LL a, LL b){
        return a>b;
}
LL a[5000],d[5000],v[5000];
int main(){
        LL t,cnt=1;
        scanf("%lld", &t);
        LL n, t2,c,l,ans = 0;
        while(t--){
                scanf("%lld%lld%lld%lld", &l,&t2,&n,&c);
                memset(v,0,sizeof(v));
                ans = 0;
                for(int i=0; i<c;i++)
                        scanf("%lld", &a[i]);
                for(int i=0;i<n;i++){
                        d[i] = a[i%c];
                        ans += 2*d[i];
                }

                LL sum = 0,index = 1e9;
                for(int i=0; i<n;i++){
                        sum += d[i];
                        if(sum >= t2/2) {index = i; d[index] = sum-(t2/2); break;}
                }


                if(index!=1e9) sort(d+index, d+n,ss);
                for(int j=index; j<min(index+l,n);j++){
                        ans -= d[j];
                }
                printf("Case #%lld: ", cnt++);
                printf("%lld\n", ans);
        }
        return 0;
}
