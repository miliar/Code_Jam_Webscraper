#include <cstdio>
#include <vector>

int main()
{
  int T;
  scanf("%d", &T);
  for(int t=1; t<=T; ++t) {
    int R, k, N;
    scanf("%d%d%d", &R, &k, &N);
    std::vector<int> v(N);
    for(int i=0; i<N; ++i)
      scanf("%d", &v[i]);
    std::vector<std::pair<int, long long> > step(N), nextstep(N);
    for(int i=0; i<N; ++i) {
      int pos = i;
      long long rev = 0;
      for(;;) {
	if(rev + v[pos] > k)
	  break;
	rev += v[pos];
	if(i == (pos = (pos + 1)%N))
	  break;
      }
      step[i] = std::make_pair(pos, rev);
    }
    int tpos = 0;
    long long trev = 0;
    for(;;) {
      if(R&1) {
	trev += step[tpos].second;
	tpos = step[tpos].first;
      }
      R >>= 1;
      if(!R) break;
      for(int j=0; j<N; ++j) {
	nextstep[j].first = step[step[j].first].first;
	nextstep[j].second = step[j].second + step[step[j].first].second;
      }
      step = nextstep;
    }
    printf("Case #%d: %lld\n", t, trev);
  }
  return 0;
}
