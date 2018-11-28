
  #include <cstdio>
  #include <cstring>
  #include <cmath>
  #include <string>
  #include <map>
  #include <algorithm>
  
  using namespace std;

  int A[105][105], B[105][105];
  int N;
  
  void init()
  {
		memset(A, 0, sizeof(A));
		int x1, y1, x2, y2;
		scanf("%d", &N);
		for (int i = 0; i < N; ++ i)
		{
			scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
			for (int j = x1; j <= x2; ++ j)
				for (int k = y1; k <= y2; ++ k)
					A[j][k] = 1;
		}
  }
  
  void work()
  {
		memset(B, 0, sizeof(B));
		int ret = 0;
		while (1)
		{
			int s = 0;
			for (int i = 1; i <= 100; ++ i)
				for (int j = 1; j <= 100; ++ j)
				{
					B[i][j] = A[i][j];
					if (B[i][j] > 0) ++ s;
				}
			if (s == 0) break;
			++ ret;
			for (int i = 1; i <= 100; ++ i)
				for (int j = 1; j <= 100; ++ j)
				{
					if (B[i][j] > 0)
					{
						A[i][j] = B[i - 1][j] + B[i][j - 1] > 0 ? 1 : 0;
					} else
					{
						A[i][j] = B[i - 1][j] + B[i][j - 1] == 2 ? 1 : 0;
					}
				}
		}
		printf("%d\n", ret);
  }
  
  int main()
  {
		freopen("C-small-attempt0.in", "r", stdin);
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