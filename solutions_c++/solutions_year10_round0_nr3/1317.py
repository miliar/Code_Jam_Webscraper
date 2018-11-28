#include <cstdio>
using namespace std;

typedef long long ll;

const char *format = "Case #%d: %lld\n";
const int N = 1000;

ll values[2 * N], sums[2 * N];
int r, k, n;

inline int f(int n) { return n & (n + 1); }
inline int g(int n) { return n | (n + 1); }

void update(int index, ll v)
{
  ll diff = v - values[index];
  values[index] = v;
  while(index < 2 * n) {
    sums[index] += diff;
    index = g(index);
  }
}

ll query(int index)
{
  ll result = 0;
  while(index >= 0) {
    result += sums[index];
    index = f(index) - 1;
  }
  return result;
}

ll query(int from, int to)
{
  return query(to) - query(from - 1);
}

int get_end(int start)
{
  int i = start, j = start + n - 1;
  if(query(i, j) <= k)
    return j;
  while(i + 1 != j) {
    int h = (i + j) / 2;
    if(query(start, h) <= k)
      i = h;
    else
      j = h;
  }
  return i;
}

ll process_test_case(void)
{
  ll result = 0;
  int start = 0;
  for(int i = 0; i < r; ++i) {
    int end = get_end(start);
    result += query(start, end);
    start = end + 1;
    while(start >= n)
      start -= n;
  }
  return result;
}

void process_test_cases(void)
{
  ll v;
  int t;
  scanf("%d", &t);
  for(int i = 1; i <= t; ++i) {
    scanf("%d%d%d", &r, &k, &n);
    for(int j = 0; j < 2 * n; ++j)
      values[j] = sums[j] = 0;
    for(int j = 0; j < n; ++j) {
      scanf("%lld", &v);
      update(j, v);
      update(j + n, v);
    }
    printf(format, i, process_test_case());
  }
}

int main(void)
{
  process_test_cases();
  return 0;
}
