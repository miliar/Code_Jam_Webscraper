#include<iostream>
#include<cstdio>
using namespace std;
int gcd(int a,int b){
    if (b==0) return a;
    else return gcd(b,a%b);
}
bool ok(long long n,int p,int pg){
    if (pg==100 && p<100) return false;
    if (pg==0 && p>0) return false;
    int q = 100;
    int k = gcd(p,q);
    p/=k; q/=k;
    if (n>=q)return true;
    for (int i = 1;i<q;i++)
    if ((i*p)%q==0 )return true;
    return false;
}
int main(){
    freopen("A-large.in","r",stdin);
    freopen("Alarge.out","w",stdout);
    int T;cin>>T; int tt=0;
    while (T--){
        long long n;
        int pd,pg;
        cin>>n>>pd>>pg;
       // cout<<n<<endl;
        tt++;
        if (ok(n,pd,pg))  printf("Case #%d: Possible\n",tt);
        else printf("Case #%d: Broken\n",tt);
    }
}
