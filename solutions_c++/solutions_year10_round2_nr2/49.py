
  #include <cstdio>
  #include <cstring>
  #include <cmath>
  #include <algorithm>
  
  using namespace std;
  
  int n, K, B, T;
  int pos[55], vel[55];
  
  void init()
  {
		scanf("%d%d%d%d", &n, &K, &B, &T);
		for (int k = 0; k < n; ++ k) scanf("%d", &pos[k]);
		for (int k = 0; k < n; ++ k) scanf("%d", &vel[k]);
  }
  
  void work()
  {
		int sum = 0;
		int ret = 0;
		for (int k = n - 1; k >= 0; -- k)
		{
			if (K == 0) break;
			if (pos[k] + vel[k] * T >= B)
			{
				ret += sum;
				-- K;
				continue;
			}
			++ sum;
		}
		if (K > 0)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n", ret);
  }
  
  int main()
  {
		int T;
		scanf("%d", &T);
		for (int k = 1; k <= T; ++ k)
		{
			printf("Case #%d: ", k);
			init();
			work();
		}
		return 0;
  }
  