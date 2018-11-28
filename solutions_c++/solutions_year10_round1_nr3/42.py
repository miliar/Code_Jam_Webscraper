#include <iostream>
#include <cstdio>
using namespace std;

int win(int a, int b)
{
  if (a == 0 || b == 0) return false;
  if (a == b) return false;

  if (a < b) swap(a, b);
  bool base = win(a%b, b);
  if (base == false)
    return true;

  return a/b > 1;
}

int mx[1000111];

int isct(int a, int b, int c, int d)
{
  int st = max(a, c);
  int en = min(b, d);
  if (st <= en) return en-st+1;
  return 0;
}

int main()
{
  int T; cin >> T;
  for (int i = 2; i <= 1000000; i++)
  {
    int low = 1, high = i;
    while (low < high) {
      int mid = (low+high+1)/2;
      if (win(i, mid))
        low = mid;
      else
        high = mid-1;
    }

    mx[i] = low;
  }

  for (int tcase = 0; tcase < T; tcase++)
  {
    int a1, a2, b1, b2;
    cin >> a1 >> a2 >> b1 >> b2;
    long long cnt = 0;
    for (int i = a1; i <= a2; i++)
    {
      cnt += isct(1, mx[i], b1, b2);
      cnt += isct(i+mx[i]+1, i+i, b1, b2);
      cnt += isct(i+i+1, 1001001, b1, b2);
    }
    printf("Case #%d: %lld\n", tcase+1, cnt);
  }
}
