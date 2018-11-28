#include <cstdio>
#include <algorithm>
#include <vector>

bool test(long long step, long long D, const std::vector<long long> &pos)
{
  long long lastpos = pos[0]-step;
  for(int i=1; i<pos.size(); ++i) {
    long long newpos = std::max(lastpos+D, pos[i]-step);
    if(newpos-pos[i] > step)
      return false;
    lastpos = newpos;
  }
  return true;
}

void solve()
{
  int C, D;
  scanf("%d%d", &C, &D);
  std::vector<long long> pos;
  for(int i=0; i<C; ++i) {
    int V;
    long long P;
    scanf("%lld%d", &P, &V);
    for(int j=0; j<V; ++j)
      pos.push_back(P*2LL);
  }
  std::sort(pos.begin(), pos.end());
  long long min = 0LL;
  long long max = 100000000000000LL;
  while(max>min) {
    long long mid=(max+min)/2LL;
    if(test(mid, D*2LL, pos))
      max=mid;
    else
      min=mid+1LL;
  }
  printf("%.1f\n", ((float)min)/2.0);
}

int main()
{
  int T;
  scanf("%d", &T);
  for(int Ts=1; Ts<=T; ++Ts) {
    printf("Case #%d: ", Ts);
    solve();
  }
  return 0;
}
