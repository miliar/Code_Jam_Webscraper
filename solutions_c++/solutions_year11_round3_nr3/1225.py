#include <iostream>
#include <algorithm>
using namespace std;

typedef long long LL;

int gcd(int a, int b){
    if(b==0) return a;
    return gcd(b,a%b);
}

int main()
{
    int tc; scanf("%d",&tc);
    for(int t=1;t<=tc;t++){
        LL N,L,H; cin>>N>>L>>H;
        LL a[N]; for(int i=0;i<N;i++) cin>>a[i];
        LL n = L;
        while(n<=H){
            int yes=1;
            for(int i=0;i<N;i++){
                if(n%a[i]!=0 && a[i]%n!=0){ yes=0; break; }
            }
            if(yes) break;
            n++;
        }
        
        printf("Case #%d: ",t);
        if(n<=H) printf("%lld\n",n);
        else printf("NO\n");
    }
}
