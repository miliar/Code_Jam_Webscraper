
  #include <cstdio>
  #include <cstring>
  #include <cmath>
  #include <string>
  #include <map>
  #include <algorithm>
  
  using namespace std;

  const int maxN = 60;
  
  int N;
  int a[maxN][maxN];
  
  void init()
  {
		scanf("%d", &N);
		for (int i = 1; i <= N * 2 - 1; ++ i)
		{
			int x;
			if (i <= N)
			{
				for (int j = 1; j <= i; ++ j)
				{
					scanf("%d", &x);
					a[j][N - i + j] = x;
				}
			} else
			{
				for (int j = 1; j <= N * 2 - i; ++ j)
				{
					scanf("%d", &x);
					a[i + j - N][j] = x;
				}
			}
		}
  }
  
  int same(int sx, int sy, int x, int y, int v)
  {
		if (x < sx || y < sy || x > sx + N - 1 || y > sy + N - 1) return 1;
		return a[x - sx + 1][y - sy + 1] == v;
  }
  
  void work()
  {
		int len = N;
		while (1)
		{
			for (int i = 1; i <= len - N + 1; ++ i)
				for (int j = 1; j <= len - N + 1; ++ j)
				{
					int OK = 1;
					for (int p = 1; p <= N && OK; ++ p)
						for (int q = 1; q <= N && OK; ++ q)
						{
							int x = i + p - 1;
							int y = j + q - 1;
							if (!same(i, j, y, x, a[p][q])) OK = 0;
							if (!same(i, j, len - y + 1, len - x + 1, a[p][q])) OK = 0;
						}
					if (OK) 
					{
						printf("%d\n", len * len - N * N);
						return;
					}
				}
			++ len;
		}
  }
  
  int main()
  {
		freopen("A-large.in", "r", stdin);
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