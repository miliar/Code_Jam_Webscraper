#include <iostream>
#include <cstring>
using namespace std;
typedef long long ll;
int r, k, n;
int g[1007];
ll ai[1007];
int bi[1007];
ll ans;
void init()
{
     cin >> r >> k >> n;
     for (int i=0; i<n; i++)
          cin >> g[i];
     ans = 0;
}
void calc()
{
     int start = 0;
     int now = 0;
     long long on = 0;
     long long one = 0;
     int times = 0;
     memset(ai, -1, sizeof(ai));
     memset(bi, 0, sizeof(bi));
     do
     {
          ai[now] = one;
          bi[now] = times;
          on = 0;
          do
          {
               if (on + g[now] <= k)
                    on += g[now++];
               else
                    break;
               if (now >= n)
                    now = 0;
          } while (now != start && on <= k);
          start = now;
          one += on;
          times++;
     } while (ai[now] == -1);
     if (r < bi[now])
     {
          for (int i=0; i<n; i++)
          {
               if (r == bi[i])
                    ans = ai[i];
          }
     }
     else
     {
          // if (r - bi[now] >= times - bi[now])
          ans += ai[now];
          ans += (r-bi[now]) / (times-bi[now]) * (one-ai[now]);
          int remain = (r-bi[now]) % (times-bi[now]);
          if (remain == 0)
               return;
          for (int i=0; i<n; i++)
          {
               if (bi[i] - bi[now] == remain)
               {
                    ans += ai[i] - ai[now];
                    return;
               }
          }
          // now = 0;
          // for (int i= (r-bi[now]) % (times-bi[now]); i>0; i--)
          // {
          //      on = 0;
          //      do
          //      {
          //           if (on + g[now] <= k)
          //                on += g[now++];
          //           else
          //                break;
          //           if (now >= n)
          //                now = 0;
          //      } while (now != start && on <= k);
          //      ans += on;
          // }
     }
}
int main(int argc, char *argv[])
{
     int t;
     cin >> t;
     for (int i=1; i<=t; i++)
     {
          init();
          calc();
          cout << "Case #" << i << ": " << ans << endl;;
     }
     return 0;
}
