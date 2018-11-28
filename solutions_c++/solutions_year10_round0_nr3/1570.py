#include <iostream>
using namespace std;
const int MAXN = 10010;
int a[MAXN];
long long sum[MAXN];
bool v[MAXN];
int Can[MAXN];
int main()
{
freopen("C-large.in","r",stdin);
freopen("C-large.out","w",stdout);
  int T,r,k,n;
  scanf("%d",&T);
  for (int t = 1;t <= T;t++)
  {
    cin >> r >> k >> n;
    for (int i = 0;i < n;i++)
      cin >> a[i];
    memset(Can,0,sizeof(Can));
    int l = 0,x = 0,h = 0;
    long long TMP;
    for (int i = 1;i <= r;i++)
    {
      Can[l] = i;
      TMP = 0;
      memset(v,0,sizeof(v));
      while (TMP + a[l] <= k)
      {
        if (v[l]) break;
        v[l] = true;
        TMP += a[l];
        l++;
        l %= n;
      }
      sum[i] = TMP;
      x++;
      if (Can[l]){h = Can[l];break;}
    }
    long long out = 0;
    TMP = 0;
    for (int i = 1;i < h;i++)
      out += sum[i];
    for (int i = h;i <= x;i++)
      TMP += sum[i];
    int a = (r-h+1),b = (x-h+1);
    out += a/b * TMP;
    for (int i = 0;i < (a%b);i++)
        out += sum[h+i];
    cout << "Case #" << t << ": " << out << endl;
  }
}
