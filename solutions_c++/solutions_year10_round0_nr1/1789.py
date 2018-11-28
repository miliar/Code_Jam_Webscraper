
  #include <cstdio>
  #include <cstring>
  #include <cmath>
  #include <algorithm>
  
  using namespace std;
  
  int N, K;
  
  void init()
  {
		scanf("%d%d", &N, &K);
  }
  
  void work()
  {
		N = (1 << N);
		if (K % N == N - 1) printf("ON\n"); else printf("OFF\n");
  }
  
  int main()
  {
		int cases;
		scanf("%d", &cases);
		for (int tt = 1; tt <= cases; ++ tt)
		{
			printf("Case #%d: ", tt);
			init();
			work();
		}
		return 0;
  }