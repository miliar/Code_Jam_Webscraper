
  #include <cstdio>
  #include <cstring>
  #include <cmath>
  #include <algorithm>
  
  using namespace std;
  
  const int MODO = 100003;
  
  int n;
  int f[505][505];
  int C[505][505];
  int sum[505];
  
  void work()
  {
		memset(C, 0, sizeof(C));
		for (int i = 0; i <= n; ++ i)
			for (int j = 0; j <= i; ++ j)
				if (j == 0) C[i][j] = 1;
				else
				{
					C[i][j] = C[i - 1][j] + C[i - 1][j - 1];
					if (C[i][j] >= MODO) C[i][j] -= MODO;
				}
				
		memset(f, 0, sizeof(f));
		memset(sum, 0, sizeof(sum));
		sum[1] = 1;
		for (int i = 2; i <= n; ++ i)
			for (int j = 1; j <= i - 1; ++ j)
			{
				if (j == 1)
				{
					f[i][j] = 1;
				} else
				{
					for (int k = 1; k <= j - 1; ++ k)
					{
						int tmp = ((long long)f[j][k] * C[i - j - 1][j - k - 1]) % MODO;
						f[i][j] += tmp;
						if (f[i][j] >= MODO) f[i][j] -= MODO;
					}
				}
				sum[i] += f[i][j];
				if (sum[i] >= MODO) sum[i] -= MODO;
			}
		printf("%d\n", sum[n]);
  }
  
  int main()
  {
		int cases;
		scanf("%d", &cases);
		for (int k = 1; k <= cases; ++ k)
		{
			printf("Case #%d: ", k);
			scanf("%d", &n);
			work();
		}
		return 0;
  }