#include<cstdio>
#include<iostream>
#include<sstream>
#include<cmath>
#include<algorithm>
#include<map>
#include<set>
#include<list>
#include<vector>
#include<stack>
#include<queue>
#include<string>
#include<ctime>
#include<iomanip>
#include<fstream>
using namespace std;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair <int,int> ii;
typedef long long LL;
#define sz(a) int((a).size())
#define pb push_back
const int INF = 2147483647;
const double PI = 3.141592653589793;

int z,p,n,a[20],i,tab[1<<20],res,q,j,temp;

int dodaj (int a, int b) {
    int res=0,i,k;
    for (i=0;i<20;i++) {
        k=0;
        if (a&(1<<i)) k++;
        if (b&(1<<i)) k++;
        k%=2;
        res+=k*(1<<i);
    }
    return res;
}

int main () {
scanf ("%d",&z);
for (q=1;q<=z;q++) {
      scanf ("%d",&n);
      for (i=0;i<n;i++) scanf ("%d",&a[i]);
      p = (1<<n);
      for (i=0;i<p;i++) {
          res=0;
          for (j=0;j<n;j++) if (i&(1<<j)) res=dodaj(res,a[j]);
          tab[i]=res;
      }
      res=-1;
      for (i=1;i<p-1;i++) if (tab[i]==tab[p-1-i]) {
          temp=0;
          for (j=0;j<n;j++) if (i&(1<<j)) temp+=a[j];
          res=max(res,temp);
      }
      printf("Case #%d: ",q);
      if (res==-1) printf("NO\n"); else printf("%d\n",res);
}
return 0;
}
