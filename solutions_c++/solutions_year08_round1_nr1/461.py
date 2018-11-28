#include    <cstdio>
#include    <algorithm>
using namespace std;
int a[800], b[800];
int main()
{
    int t, n, i, j, ans;
    freopen("A-small-attempt1.in", "r", stdin);
    freopen("A-small-attempt1.out", "w", stdout);
    scanf("%d", &t);
    for (j=1; j<=t; ++j) {
          scanf("%d", &n);
          for (i=0; i<n; ++i) scanf("%d", &a[i]);
          for (i=0; i<n; ++i) scanf("%d", &b[i]);
          ans=0;
          sort(a, a+n);
          sort(b, b+n);
          for (i=0; i<n; ++i) ans+=a[i]*b[n-i-1];
          printf("Case #%d: %d\n", j, ans);
    }
}
