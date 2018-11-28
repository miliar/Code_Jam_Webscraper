#include <cstdio>
#include <vector>

int main()
{
  std::vector<int> forbidden(1024);
  int C;
  char m[20][20];
  scanf("%d", &C);
  for(int nc=1; nc<=C; ++nc) {
    int M, N;
    scanf("%d%d", &M, &N);
    std::vector<int> v1(1<<N);
    for(int i=0; i<M; ++i)
      scanf("%s", m[i]);
    for(int i=0; i<1024; ++i) {
      if(i&1)
	forbidden[i] = 2;
      for(int j=1; j<10; ++j)
	if(i&(1<<j))
	  forbidden[i] |= 5<<(j-1);
    }
    for(int k=0; k<M; ++k) {
      std::vector<int> v2(1<<N);
      for(int i=0; i<(1<<N); ++i) {
	int n=0;
	for(int j=0; j<N; ++j) {
	  if(i&(1<<j)) {
	    if((i&(2<<j)) || (m[M-k-1][j]=='x')) goto cont;
	    ++n;
	  }
	}
	for(int j=0; j<(1<<N); ++j)
	  if(0 == (j & forbidden[i])) {
	    v2[j] >?= v1[i] + n;
	  }
      cont:{}
      }
      v1 = v2;
    }
    int mx = 0;
    for(int i=0; i<(1<<N); ++i)
      mx >?= v1[i];
    printf("Case #%d: %d\n", nc, mx);
  }
  return 0;
}
