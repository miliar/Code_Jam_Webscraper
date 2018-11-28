
  #include <cstdio>
  #include <cstring>
  #include <cmath>
  #include <string>
  #include <map>
  #include <algorithm>
  
  using namespace std;

  long long L;
  int N;
  int a[105];
  int f[1000005], que[1000005];
  
  int GCD(int a, int b)
  {
		return b == 0 ? a : GCD(b, a % b);
  }
  
  void init()
  {
		scanf("%I64d%d", &L, &N);
		for (int k = 0; k < N; ++ k)
			scanf("%d", &a[k]);
  }
  
  void work()
  {
		int v = 0;
		for (int k = 0; k < N; ++ k)
			v = GCD(v, a[k]);
		if (L % v > 0)
		{
			printf("IMPOSSIBLE\n");
			return;
		}
		
		L /= v;
		for (int k = 0; k < N; ++ k) a[k] /= v;
		
		memset(f, 255, sizeof(f));
		
		int h, t;
		h = 0; t = 1; que[1] = 0; f[0] = 0;
		while (h < t)
		{
			++ h;
			int x = que[h];
			for (int k = 0; k < N; ++ k)
				if (x + a[k] <= 1000000)
				{
					if (f[x + a[k]] >= 0) continue;
					f[x + a[k]] = f[x] + 1;
					que[++t] = x + a[k];
				}
		}
		
		int maxA = 0;
		for (int k = 0; k < N; ++ k) maxA = max(maxA, a[k]);
		
		long long ret = (L - 1000000) / maxA;
		L = L - (L - 1000000) / maxA * maxA;
		while (L > 1000000)
		{
			L -= maxA; ret ++;
		}
		
		ret += f[L];
		printf("%I64d\n", ret);
  }
  
  int main()
  {
		freopen("B-small-attempt0.in", "r", stdin);
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