#include<iostream>
#include<cstring>
#include<algorithm>
#include<cstdio>
using namespace std;

int n, m, x, sum;
int times;
int ans;

int main()
{
    freopen("C1.in","r",stdin);
    freopen("C.out","w",stdout);
    
    scanf("%d",&times);
    for(int k = 1; k <= times; ++k) {
      printf("Case #%d: ",k);
      scanf("%d",&n);
      m = 1000001; ans = 0; sum = 0;
      for (int i = 1; i <= n; ++i) {
        scanf("%d",&x);
        sum += x;
        if (x < m) m = x;
        ans ^= x;
      }
      if (ans) printf("NO");
      else printf("%d",sum-m);
      printf("\n");
    }
}
