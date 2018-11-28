
  #include <cstdio>
  #include <cstring>
  #include <cmath>
  #include <algorithm>
  
  using namespace std;
  
  int R, K, N;
  int a[1005], next[1005];
  int yes[1005];
  long long T[1005], b[1005];
  
  void init()
  {
		scanf("%d%d%d", &R, &K, &N);
		for (int i = 0; i < N; ++ i) scanf("%d", &a[i]);
  }
  
  void work()
  {
		for (int i = 0; i < N; ++ i)
		{
			int j = i;
			long long sum = a[i];
			int len = 1;
			while (1)
			{
				j = (j + 1) % N;
				++ len;
				if (sum + a[j] > K || len > N) break;
				sum += a[j]; 
			}
			next[i] = j;
			b[i] = sum;
		}
	
		
		
		memset(yes, 0, sizeof(yes));
		memset(T, 0, sizeof(T));
		int k = 0;
		int len = 0;
		long long ret = 0;
		
		while (!yes[k])
		{
			yes[k] = ++ len;
			T[len] = T[len - 1] + b[k];
			k = next[k];
		}
		
		int pre = yes[k];
		R -= pre - 1;
		ret = (T[len] - T[pre - 1]) * (R / (len - pre + 1)) + T[pre - 1];
		R = R % (len - pre + 1);
		
		while (R > 0)
		{
			ret += b[k];
			k = next[k];
			-- R;
		}
		
		printf("%I64d\n", ret);
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
 