#include <cstdio>
#include <cmath>
using namespace std;
const int a10[10] = {1, 10, 100, 1000, 10000, 100000, 1000000};
int cases, t, A, B, ans;
int reverse(int num, int dig, int l)
{
    int a = num % a10[dig];
    num /= a10[dig];
    num += a*a10[l-dig+1];
    return num;
}
void solve()
{
     int aa[20], na;
     ans = 0;
     for (int i = A; i <= B; ++i)
     {
          int l = (int)log10(i+0.1);
          na = 0;
          for (int j = 1; j <= l; ++j)
          {
              int rn = reverse(i, j, l);
              bool f = false;
              for (int k = 1; k <= na; ++k)
                  if(rn == aa[k])
                  {
                        f = true;
                        break;
                  }
              if(!f && rn >= A && rn <= B && rn > i)
              {
                    aa[++na] = rn;
                    ++ans;
              }
          }
     }
}
int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    scanf("%d", &cases);
    for (t = 1; t <= cases; ++t)
    {
        scanf("%d%d", &A, &B);
        solve();
        printf("Case #%d: %d\n", t, ans);
    }
    return 0;
}
