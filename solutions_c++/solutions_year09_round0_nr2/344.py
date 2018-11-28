
  #include <cstdio>
  #include <cstring>
  #include <cmath>
  #include <algorithm>
  #include <iostream>
  #include <string>
  #include <vector>
  
  using namespace std;

  int dx[4] = {-1, 0, 0, 1};
  int dy[4] = {0, -1, 1, 0};
  
  int m, n;
  int a[105][105], fa[10005];
  int ans[10005];
  
  int getfather(int x)
    {
        if (fa[x] != x) { fa[x] = getfather(fa[x]); }
	return fa[x];
    }
    
  void merge(int x, int y)
    {
        x = getfather(x);
	y = getfather(y);
	if (x > y) swap(x, y);
	fa[y] = x;
    }
    
  void work()
    {
        for (int i = 0; i < m * n; ++ i) fa[i] = i;
	for (int i = 0; i < m; ++ i)
	  for (int j = 0; j < n; ++ j)
	    {
	       int newx = -1, newy = -1;
	       for (int k = 0; k < 4; ++ k)
	         {
		    int x = i + dx[k];
		    int y = j + dy[k];
		    if (x < 0 || x >= m || y < 0 || y >= n || a[x][y] >= a[i][j]) continue;
		    if (newx < 0 || a[x][y] < a[newx][newy])
		      {
		         newx = x; newy = y;
	              }
		 }
	       if (newx < 0) continue;
	       merge(i * n + j, newx * n + newy);
	    }
	
	int cnt = 0;
	for (int i = 0; i < m; ++ i)
	  for (int j = 0; j < n; ++ j)
	    {
	        int w = getfather(i * n + j);
		if (w == i * n + j) ans[i * n + j] = cnt ++; else ans[i * n + j] = ans[w];
		printf("%c", ans[i * n + j] + 'a');
		if (j == n - 1) printf("\n"); else printf(" ");
	    }
    }
    
  int main()
    {
        //freopen("B.in", "r", stdin);
	  int caseNo;
	  scanf("%d", &caseNo);
	  for (int T = 1; T <= caseNo; ++ T)
	    {
	        printf("Case #%d:\n", T);
		scanf("%d%d", &m, &n);
		
		for (int i = 0; i < m; ++ i)
		  for (int j = 0; j < n; ++ j)
		    scanf("%d", &a[i][j]);
		    
		work();
	    }
	return 0;
    }