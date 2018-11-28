#include<fstream>
#include<iostream>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;
long long tc,n,tmp,res,ans;
long long ar[1005],no;
bool code,lho[1005];
ifstream ii("C-small-attempt1.in");
ofstream oo("C-small-attempt1.out");

int dfs(long long x, long long tot, long long z, long long zz) {
    lho[z]=1;
    res=0;
    long long cek=0;
    for (int j=0;j<n;j++) {
        if (lho[j]==0) {
           res=res^ar[j];
           cek++;
        }
    }
    if (res==tot && cek!=0) {
       code=1; 
       if (x > ans) {
          ans=x;
       }
    }
    for (int j=z-1;j>=0;j--) {
        dfs(x+ar[j],tot^ar[j],j,zz+1);
    }
    lho[z]=0;
}
int main() {
    ii >> tc;
    while (ii >> n) {
          tmp=0;
          code=0;
          ans=0;
          for (int i=0;i<n;i++) {
              ii >> ar[i];
              tmp+=ar[i];
          }
          sort(ar,ar+n);
          for (int i=n-1;i>=0;i--) {
              if (!code) dfs(ar[i],ar[i],i,0);
          }
          no++;
          oo << "Case #" << no << ": ";
          if (code) oo << ans << endl; else
          oo << "NO" << endl;
    }
    
}
