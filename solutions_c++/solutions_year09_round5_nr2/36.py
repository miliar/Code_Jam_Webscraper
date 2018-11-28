
  #include <cstdio>
  #include <cstring>
  #include <cmath>
  #include <map>
  #include <algorithm>

  using namespace std;

  const int modo = 10009;

  int res[11];
  int tot, K;
  int grp[5][26], cnt[105][26];

  map <long long, int> T;
  long long que[2][100005];
  int ans[2][100005];
  char str[1000];
  int N;

  void init()
  {
	  memset(grp, 0, sizeof(grp));
	  scanf("%s", str);
	  tot = 0;
	  int len = strlen(str);
	  for (int i = 0, j = 0; i <= len; ++ i)
		  if (i == len || str[i] == '+')
			{
				for (int k = j; k < i; ++ k)
					grp[tot][str[k] - 'a'] ++;
				tot += 1;
				j = i + 1;
			}
	  scanf("%d", &K);
	  scanf("%d", &N);
	  memset(cnt, 0, sizeof(cnt));
	  for (int i = 0; i < N; ++ i) 
	  {
		  scanf("%s", str);
		  int len = strlen(str);
		  for (int j = 0; j < len; ++ j)
			  ++ cnt[i][str[j] - 'a'];
	  }
  }
  
  void work()
  {
	  int save[4];
	  int nowcnt[4];
	  int o;

      memset(res, 0, sizeof(res));
	  for (int num = 0; num < tot; ++ num)
	  {
		  int sz = 1;
		  int cur = 0;
		  que[cur][1] = 0;
		  ans[cur][1] = 1;

		  o = 0;
		  for (int j = 0; j < 26; ++ j)
			  if (grp[num][j] > 0)
				{
			        save[o] = j;
					nowcnt[o] = grp[num][j];
					++ o;
			    }

		  for (int d = 1; d <= K + 1; ++ d)
		  {
			  cur = 1 - cur;
			  int last = sz;
			  sz = 0;
			  T.clear();

			  for (int j = 1; j <= last; ++ j)
              {
				  int list[4];
				  long long x = que[1 - cur][j];
				  int w = ans[1 - cur][j];
				  for (int k = 0; k < o; ++ k)
				  {
					  list[k] = x & 511;
					  x >>= 9;
					  for (int Cc = 0; Cc < nowcnt[k]; ++ Cc)
						 w = (w * list[k]) % modo;
				  }
				  if (d > 1)
					  res[d - 1] = (res[d - 1] + w) % modo;
					  
				  if (d > K) continue;

				  for (int k = 0; k < N; ++ k)
				  {
					  long long x = 0;
					  for (int tmp = o - 1; tmp >= 0; -- tmp)
					  {
						  x = x * 512 + (list[tmp] + cnt[k][save[tmp]]);
					  }

					  if (T.find(x) == T.end())
					  {
						  que[cur][++sz] = x;
						  ans[cur][sz] = ans[1 - cur][j];
						  T[x] = sz;
					  } else
					  {
						  int ww = T[x];
						  ans[cur][ww] += ans[1 - cur][j];
						  if (ans[cur][ww] >= modo) ans[cur][ww] -= modo;
					  }
				  }
			  }
		  }
	  }

	  for (int d = 1; d <= K; ++ d)
	  {
		  printf("%d", res[d]);
		  if (d == K) printf("\n"); else printf(" ");
	  }
	  
  }
  
  int main()
    {
       freopen("B-small-attempt0.in", "r", stdin);
 
         int caseNo;
         scanf("%d", &caseNo);

         for (int t = 1; t <= caseNo; ++ t)
           {
              printf("Case #%d: ", t);
              init();
              work();
           }
       return 0;
    }
