#include <cstdio>
#include <vector>

using std::vector;

long long count(int n, long long coef, int last1, int last2, int last3, int o1, int o2, vector<long long> &v)
{
  long long tot = 0;
  if(n==3) {
    if((o1%3)||(o2%3)) return 0;
    if(last1==last3) {
      if(coef%6)
	printf("fel!\n");
      return coef/6;
    } else if(last1==last2 || last2==last3) {
      if(coef%2)
	printf("fel2!\n");
      return coef/2;
    }
    return coef;
  }
  for(int x = 0; x < 3; ++x)
    for(int y = 0; y < 3; ++y) {
      const int c = x*3+y;
      if(c >= last1 && v[c]) {
	--v[c];
	tot += count(n+1, coef*(v[c]+1), c, last1, last2, o1+x, o2+y, v);
	++v[c];
      }
    }
  return tot;
}

int main()
{
  int N;
  scanf("%d", &N);
  for(int nc=1; nc<=N; ++nc) {
    long long n, A, B, C, D, x0, y0, M;
    scanf("%lld%lld%lld%lld%lld%lld%lld%lld", &n, &A, &B, &C, &D, &x0, &y0, &M);
    vector<long long> v(9);
    do {
      ++v[(x0%3)*3+y0%3];
      x0 = (A * x0 + B) % M;
      y0 = (C * y0 + D) % M;
    } while(--n);
    printf("Case #%d: %lld\n", nc, count(0, 1, -1, -2, -3, 0, 0, v));
  }
  return 0;
}
