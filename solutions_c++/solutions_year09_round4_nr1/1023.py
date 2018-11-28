#include <cstdio>
#include <vector>
#include <algorithm>

int bubble(std::vector<int> &v)
{
  int swps=0;
  for(int i=0; i<v.size(); ++i)
    if(v[i] > i) {
      int j;
      for(j=i+1; j<v.size(); ++j)
	if(v[j] <= i) break;
      for(int k=j; k>i; --k) {
	std::swap(v[k-1], v[k]);
	++swps;
      }
    }
  return swps;
}

int main()
{
  int T;
  scanf("%d", &T);
  for(int T_=1; T_<=T; ++T_) {
    int N;
    scanf("%d ", &N);
    char str[100];
    std::vector<int> v;
    for(int i=0; i<N; ++i) {
      gets(str);
      int j=0;
      while(str[j]) ++j;
      for(--j; j>0; --j)
	if(str[j]!='0') break;
      v.push_back(j);
    }
    printf("Case #%d: %d\n", T_, bubble(v));
  }
  return 0;
}
