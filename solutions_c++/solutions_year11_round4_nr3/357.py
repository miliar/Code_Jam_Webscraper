#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstring>
using namespace std;

#define maxn 1000007

int cases;
long long n;
long long ans;
long long w;

bool a[maxn];
int p[maxn];

void prepar()
{
    memset(a,false,sizeof(a));
    int z; p[0] = 0;
    for (int i = 2; i <= 1000000; ++i) if (!a[i]) {
      p[++p[0]] = i;
      z = i;
      while (z <= 1000000) {
        a[z] = true;
        z += i;
      }
    }
}


int main()
{
    freopen("C1.in","r",stdin);
    freopen("C.out","w",stdout);
    
    prepar();
    
    scanf("%d",&cases);
    for (int k = 1; k <= cases; ++k) {
      printf("Case #%d: ",k);
      scanf("%lld",&n);
      ans = 0;
      if (n > 1) {
      for (int i = 1; i <= p[0]; ++i) {
        w = p[i];
        if (w*w > n) break;
        w = n;
        while (w/p[i]) {
          ++ans;
          w /= p[i];
        }
        --ans;
      }
      ++ans;
      }
      printf("%lld\n",ans);
    }
}
