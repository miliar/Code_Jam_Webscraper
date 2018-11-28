
  #include <cstdio>
  #include <cstring>
  #include <cmath>
  #include <string>
  #include <map>
  #include <algorithm>
  
  using namespace std;
  
  int num[100005][105];
  int size[100005];
  string a[100005][105];
  int N, M;
  int tot;
  
  void init()
  {
		memset(num, 255, sizeof(num));
		memset(size, 0, sizeof(size));
		tot = 0;
		
		scanf("%d%d", &N, &M);
		char s[205];
		
		for (int i = 0; i < N; ++ i)
		{
			scanf("%s", &s);
			int cur = 0;
			int len = strlen(s);
			int k = 1;
			for (int j = 1; j < len; ++ j)
				if (j == len - 1 || s[j] == '/')
				{
					string st = "";
					while (k < j || k == len - 1)
					{
						st += s[k]; ++ k;
					}
					++ k;
					int next = -1;
					for (int j = 0; j < size[cur]; ++ j)
						if (a[cur][j] == st)
						{
							next = num[cur][j];
							break;
						}
					if (next < 0)
					{
					num[cur][size[cur]] = ++ tot;
					a[cur][size[cur]] = st;
					++ size[cur];
					next = tot;
					}
					cur = next;
				}
		}
		
		int ret = 0;
		for (int i = 0; i < M; ++ i)
		{
			scanf("%s", &s);
			int cur = 0;
			int len = strlen(s);
			int k = 1;
			for (int j = 1; j < len; ++ j)
				if (j == len - 1 || s[j] == '/')
				{
					string st = "";
					while (k < j || k == len - 1)
					{
						st += s[k]; ++ k;
					}
					++ k;
					int next = -1;
					for (int j = 0; j < size[cur]; ++ j)
						if (a[cur][j] == st)
						{
							next = num[cur][j];
							break;
						}
					if (next < 0)
					{
					num[cur][size[cur]] = ++ tot;
					++ ret;
					a[cur][size[cur]] = st;
					++ size[cur];
					next = tot;
					}
					cur = next;
				}
		}
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
		}
		return 0;
  }