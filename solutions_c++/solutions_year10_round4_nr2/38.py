
  #include <cstdio>
  #include <cstring>
  #include <cmath>
  #include <string>
  #include <map>
  #include <algorithm>
  
  using namespace std;

  const int maxP = 10;
  const int maxnum = 1000000000;
  
  int M[1 << 10];
  int C[11][1 << 10];
  int f[11][1 << 10][11], g[11][1 << 10][11];
  int N, P;
  
  void init()
  {
		scanf("%d", &P);
		N = 1 << P;
		for (int i = 0; i < N; ++ i)
		{
			scanf("%d", &M[i]);
			M[i] = P - M[i];
		}
			
		int S = N;
		for (int i = 1; i <= P; ++ i)
		{
			S >>= 1;
			for (int j = 0; j < S; ++ j)
				scanf("%d", &C[i][j]);
		}
  }
  
  void work()
  {
		for (int i = 0; i < (1 << P); ++ i)
			for (int j = 0; j <= P; ++ j) 
			{
				if (j < M[i]) f[0][i][j] = maxnum;
					else f[0][i][j] = 0;
				if (j > 0) g[0][i][j] = g[0][i][j - 1]; else g[0][i][j] = maxnum;
				if (f[0][i][j] < g[0][i][j]) g[0][i][j] = f[0][i][j];
			}
		
		for (int i = 1; i <= P; ++ i)
			for (int j = 0; j < (1 << (P - i)); ++ j)
				for (int k = 0; k <= P - i; ++ k)
				{
					f[i][j][k] = g[i - 1][j * 2][k] + g[i - 1][j * 2 + 1][k];
					int tmp = g[i - 1][j * 2][k + 1] + g[i - 1][j * 2 + 1][k + 1] + C[i][j];
					if (tmp < f[i][j][k]) f[i][j][k] = tmp;
					if (k > 0) g[i][j][k] = g[i][j][k - 1]; else g[i][j][k] = maxnum;
					if (f[i][j][k] < g[i][j][k]) g[i][j][k] = f[i][j][k];
				}
		
		printf("%d\n", f[P][0][0]);
  }
  
  int main()
  {
		freopen("B-large.in", "r", stdin);
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