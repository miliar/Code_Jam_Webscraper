#include <iostream>
#include <cstdio>

using namespace std;

int ga[10009];
int va[10009][2];
int ch[10009];


int main()
{
	freopen("c:\\1.txt", "r", stdin);
	freopen("c:\\1out.txt", "w", stdout);

	int t;
	scanf("%d", &t);

	for (int te = 1; te <= t; te++)
	{
		memset(va,0,sizeof(va));

		int m,v;
		scanf("%d %d", &m, &v);

		for (int i = 1; i <= m/2; i++)
		{
			scanf("%d %d", &ga[i], &ch[i]);
		}
	
		for (int i = m/2+1; i <= m; i++)
		{
			int val;
			scanf("%d", &val);
			if (val == 0) { va[i][0]=0; va[i][1] = 1E6; } else {va[i][0]=1E6; va[i][1]=0; }

		}

		for (int i = m/2; i >= 1; i--)
		{
			va[i][0]=1E6;
			va[i][1]=1E6;

				if (ga[i]==0)
				{
					//or
					if (va[i*2][0]!=1E6 && va[i*2+1][0] != 1E6)
					{
						va[i][0]=va[i*2][0]+va[i*2+1][0];
					}

					// 1?
					if (va[i*2][0]!=1E6 && va[i*2+1][1] != 1E6)
					{
						va[i][1]=min(va[i][1], va[i*2][0]+va[i*2+1][1]);
					}

					if (va[i*2][1]!=1E6 && va[i*2+1][0] != 1E6)
					{
						va[i][1]=min(va[i][1], va[i*2][1]+va[i*2+1][0]);
					}

					if (va[i*2][1]!=1E6 && va[i*2+1][1] != 1E6)
					{
						va[i][1]=min(va[i][1], va[i*2][1]+va[i*2+1][1]);
					}


				}
				else
				{
					//and
					if (va[i*2][0]!=1E6 && va[i*2+1][0] != 1E6)
					{
						va[i][0]=va[i*2][0]+va[i*2+1][0];
					}

					// 1?
					if (va[i*2][0]!=1E6 && va[i*2+1][1] != 1E6)
					{
						va[i][0]=min(va[i][0], va[i*2][0]+va[i*2+1][1]);
					}

					if (va[i*2][1]!=1E6 && va[i*2+1][0] != 1E6)
					{
						va[i][0]=min(va[i][0], va[i*2][1]+va[i*2+1][0]);
					}

					if (va[i*2][1]!=1E6 && va[i*2+1][1] != 1E6)
					{
						va[i][1]=min(va[i][1], va[i*2][1]+va[i*2+1][1]);
					}
				}

			if (ch[i])
			{
				//changeable

				if (ga[i]==0)
				{
					//to be and
					if (va[i*2][0]!=1E6 && va[i*2+1][0] != 1E6)
					{
						va[i][0]=min(va[i][0],va[i*2][0]+va[i*2+1][0]+1);
					}

					// 1?
					if (va[i*2][0]!=1E6 && va[i*2+1][1] != 1E6)
					{
						va[i][0]=min(va[i][0], va[i*2][0]+va[i*2+1][1]+1);
					}

					if (va[i*2][1]!=1E6 && va[i*2+1][0] != 1E6)
					{
						va[i][0]=min(va[i][0], va[i*2][1]+va[i*2+1][0]+1);
					}

					if (va[i*2][1]!=1E6 && va[i*2+1][1] != 1E6)
					{
						va[i][1]=min(va[i][1], va[i*2][1]+va[i*2+1][1]+1);
					}


				}
				else
				{
					//to be or
					if (va[i*2][0]!=1E6 && va[i*2+1][0] != 1E6)
					{
						va[i][0]=min(va[i][0],va[i*2][0]+va[i*2+1][0]+1);
					}

					// 1?
					if (va[i*2][0]!=1E6 && va[i*2+1][1] != 1E6)
					{
						va[i][1]=min(va[i][1], va[i*2][0]+va[i*2+1][1]+1);
					}

					if (va[i*2][1]!=1E6 && va[i*2+1][0] != 1E6)
					{
						va[i][1]=min(va[i][1], va[i*2][1]+va[i*2+1][0]+1);
					}

					if (va[i*2][1]!=1E6 && va[i*2+1][1] != 1E6)
					{
						va[i][1]=min(va[i][1], va[i*2][1]+va[i*2+1][1]+1);
					}
				}


			}
		}

		if (va[1][v]==1E6)
		{
			printf("Case #%d: IMPOSSIBLE\n", te);
		}
		else
		{
			printf("Case #%d: %d\n", te, va[1][v]);
		}
	}

	return 0;
}
