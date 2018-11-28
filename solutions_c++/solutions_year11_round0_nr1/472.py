#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

int Tc;
int n;
char c[105];
int a[105];
int pb,po;
int F[105];

void solve(){
    pb=0; po=0;
    F[0]=0;
    a[0]=1;
    for (int i=1;i<=n;i++)
      if (c[i]=='O'){
          F[i]=max(F[i-1]+1,abs(a[po]-a[i])+1+F[po]);
          po=i;
      }
      else{
          F[i]=max(F[i-1]+1,abs(a[pb]-a[i])+1+F[pb]);
          pb=i;
      }
    cout << F[n] << "\n";
}

int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&Tc);
    for (int T=1;T<=Tc;T++){
        printf("Case #%d: ",T);
        cin >> n;
        for (int i=1;i<=n;i++)
          cin >> c[i] >> a[i];
        solve();
    }
}
