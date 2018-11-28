
  #include <cstdio>
  #include <cstring>
  #include <cmath>
  #include <algorithm>

  using namespace std;

  const int modo =  999983;
  const int dx[4] = {-1, 1, 0, 0};
  const int dy[4] = {0, 0, -1, 1};

  int m, n, area, num;
  int hash[modo], wall[12][12], st[12][12], en[12][12];
  long long que[1000005];
  int next[1000005], dist[1000005];
  long long Sou, Tar;
  int qx[5], qy[5], vx[5], vy[5], newq[5];
  int h, t;
  int res, OK;

  void init()
  {
	  scanf("%d%d", &m, &n);
	  area = m * n;
	  for (int i = 0; i < m; ++ i)
		  for (int j = 0; j < n; ++ j)
			{
				char c;
				while (1)
			    {
					c = getchar();
					if (c == '.' || c == '#' || c == 'x' || c == 'o' || c == 'w') break;
			    }
				wall[i][j] = c == '#';
				st[i][j] = c == 'o' || c == 'w';
				en[i][j] = c == 'x' || c == 'w';
			}

      Sou = Tar = 0;
	  num = 0;
	  for (int i = 0; i < m; ++ i)
		  for (int j = 0; j < n; ++ j)
			  {
				  if (st[i][j]) { Sou = Sou * area + i * n + j; num ++; }
				  if (en[i][j]) Tar = Tar * area + i * n + j;
		      }
	  memset(hash, 0, sizeof(hash));
  }
  
  void put(long long S, int w)
  {
	  int idx = S % modo;
	  int tmp = hash[idx];
	  while (tmp > 0)
	  {
		  if (que[tmp] == S) return;
		  tmp = next[tmp];
	  }
	  que[++t] = S;
	  next[t] = hash[idx];
	  hash[idx] = t;
	  dist[t] = w;
	  if (S == Tar) res = w;
  }

  int isBox(int x, int y)
  {
	  for (int i = 0; i < num; ++ i)
		  if (qx[i] == x && qy[i] == y) return 1;
	  return 0;
  }

  #define abs(x) (((x) > 0) ? (x) : (-(x)))

  void dfs(int pos)
  {
	  if (OK & ((1 << pos))) return;
	  OK += (1 << pos);
	  for (int i = 0; i < num; ++ i)
		if (abs(vx[i] - vx[pos]) + abs(vy[i] - vy[pos]) == 1) dfs(i);				
  }

  int IfConnected(long long S)
  {
	  for (int i = num - 1; i >= 0; -- i)
		  {
			  int x = S % area;
			  vx[i] = x / n;
			  vy[i] = x - vx[i] * n;
			  S /= area;
		  }
	  OK = 0;
	  dfs(0);
	  return (OK == (1 << num) - 1);
  }

  void work()
  {
	  res = -1;
	  h = t = 0;
	  put(Sou, 0);
	  while (h < t && res < 0)
	  {
		  long long state = que[++h];
		  int connected = IfConnected(state);
		  for (int i = num - 1; i >= 0; -- i)
		  {
			  int x = state % area;
			  qx[i] = x / n;
			  qy[i] = x % n;
			  state /= area;
		  }
		  //printf("*****************************************\n");
		  //printf("%d %d %d %d %d %d %d\n", qx[0], qy[0], qx[1], qy[1], qx[2], qy[2], connected);
		  for (int i = 0; i < num; ++ i)
			  for (int j = 0; j < 4; ++ j)
				{
					int x = qx[i] + dx[j];
					int y = qy[i] + dy[j];
					int x2 = qx[i] - dx[j];
					int y2 = qy[i] - dy[j];
					if (x < 0 || x >= m || y < 0 || y >= n || wall[x][y]) continue;
					if (x2 < 0 || x2 >= m || y2 < 0 || y2 >= n || wall[x2][y2]) continue;
					if (isBox(x, y) || isBox(x2, y2)) continue;


					for (int k = 0; k < num; ++ k)
					   if (k == i) newq[k] = x * n + y; else newq[k] = qx[k] * n + qy[k];

					int pos = i;
					while (pos > 0 && newq[pos] < newq[pos - 1]) { swap(newq[pos], newq[pos - 1]); -- pos; }
					while (pos + 1 < num && newq[pos] > newq[pos + 1]) { swap(newq[pos], newq[pos + 1]); ++ pos; }

					long long newS = 0;
					for (int k = 0; k < num; ++ k)
						newS = newS * area + newq[k];

					if (connected == 0 && IfConnected(newS) == 0) continue;
					put(newS, dist[h] + 1);
			    }
	  }
	  printf("%d\n", res);
  }
  
  int main()
    {
       freopen("A-large.in", "r", stdin);
 
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
