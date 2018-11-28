#include<iostream>
#include<cstdio>
using namespace std;
const int N = (int)1e6;
int a[90000];
bool p[N];
long long n;
int m,T;
int solve(long long n){
    if (n==1)return 0;
    int re=1;
    for (int i=1;i<=m;i++){
        if ((long long)a[i]*a[i]>n) break;
        long long b=(long long)a[i];
        while (b<=n){
            re++;b*=a[i];
        }
        re-=1;
    }
    return re;
}
int main (){
    freopen("C-large.in","r",stdin);
    freopen("Clarge.out","w",stdout);
    cin>>T; int tt=0;
    p[2]=false; m=0;
    for (int i=2;i<=N;i++)if (!p[i]){
        a[++m] = i;
        for (int j=i*2;j<=N;j+=i) p[j]=true;
    }
 //   cout<<m<<endl;
  //  for (int i = 1;i<=10;i++)cout<<a[i]<<endl;
    while (T--){
        cin>>n;
        printf("Case #%d: %d\n",++tt,solve(n));
    }

}
