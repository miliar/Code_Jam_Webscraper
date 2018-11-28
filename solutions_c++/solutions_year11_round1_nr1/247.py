#include<cstdio>
#define ll long long int

ll gcd(ll a, ll b){
    if (a<b) return gcd(b,a);
    if ((a%b) == 0) return b;
    return gcd(b, a%b);
}

int t,n;

int main(){
    scanf("%d",&t);
    for (int ca=1;ca<=t;++ca){
        ll n,d,g,ans,div;
        scanf("%I64d%I64d%I64d", &n, &d, &g);

        if (g==0ll){
            if (d==0ll) printf("Case #%d: Possible\n",ca);
            else printf("Case #%d: Broken\n",ca);
        }
        else if (g==100ll){
            if (d==100ll) printf("Case #%d: Possible\n",ca);
            else printf("Case #%d: Broken\n",ca);
        }
        else{
            if (d==0ll){
                printf("Case #%d: Possible\n",ca);
            }
            else{
                div = gcd(d,100ll);
                ans=100ll/div;
                if (ans>n) printf("Case #%d: Broken\n",ca);
                else printf("Case #%d: Possible\n",ca);
            }
        }
    }
    return 0;
}
