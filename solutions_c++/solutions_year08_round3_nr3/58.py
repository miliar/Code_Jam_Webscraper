#include <iostream>
#include <vector>

using namespace std;

const int maxLEN = 500000 + 10;

typedef long long INT;

const INT MOD = 1000000007LL;

int N;
int n, m;
INT X, Y, Z;

INT A[maxLEN];
vector<INT> s;

int rank[maxLEN];

INT sum[maxLEN];

int
findrank(INT x)
{
  int l, r, mid;
  l = 0;
  r = n - 1;
  while (l < r)
  {
    mid = (l + r) / 2;
    if (x > A[mid])
    {
      l = mid + 1;
    }
    else
    {
      r = mid;
    }
  }
  return rank[l];
}

void
insert(int x, INT val)
{
  for (; x <= n; x += (x & (x ^ (x - 1))))
  {
    sum[x] = (sum[x] + val) % MOD;
  }
}

INT
find(int x)
{
  INT result = 0;
  for (; x > 0; x -= (x & (x ^ (x - 1))))
  {
    result = (result + sum[x]) % MOD;
  }
  return result;
}

int main()
{
  INT t, totalsum;
  int pos;
  cin >> N;
  for (int e = 1; e <= N; ++e)
  {
    cout << "Case #" << e << ": ";
    cin >> n >> m >> X >> Y >> Z;
    for (int i = 0; i < m; ++i)
    {
      cin >> A[i];
    }
    s.clear();
    for (int i = 0; i < n; ++i)
    {
      s.push_back(A[i % m]);
      A[i % m] = (X * A[i % m] + Y * (i + 1)) % Z;
    }
    for (int i = 0; i < n; ++i)
    {
      A[i] = s[i];
    }
    sort(A, A + n);
    rank[0] = 1;
    for (int i = 1; i < n; ++i)
    {
      rank[i] = rank[i - 1];
      if (A[i] > A[i - 1])
      {
        ++rank[i];
      }
    }

    /*
    for (int i = 0; i < n; ++i)
    {
      cout << s[i] << ' ' << findrank(s[i]) << endl;
    }
    */

    memset(sum, 0, (n + 1) * sizeof(INT));
    /*
    for (int i = 1; i <= n; ++i)
    {
      insert(i, 1);
    }
    */

    totalsum = 0;
    for (int i = 0; i < n; ++i)
    {
      pos = findrank(s[i]);
      t = find(pos - 1);
      totalsum = (totalsum + t + 1) % MOD;
      insert(pos, t + 1);
    }
    cout << totalsum << endl;
  }
  return 0;
}

