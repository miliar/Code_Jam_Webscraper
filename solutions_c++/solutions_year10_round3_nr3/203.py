#include <iostream>
using namespace std;

int used[600][600];
int w[600][600];
bool f[600][600];
int n,m;
char s[600];
int res[600];

void out()
{
	/*for(int i=0;i<n;i++)
	{
		for(int j=0;j<m;j++)
		{
			cout<<used[i][j];
		}
		cout<<endl;
	}
	cout<<"---------------------------------------"<<endl;*/
}

int main()
{
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);

	int t;
	cin>>t;
	for(int tt=1;tt<=t;tt++)
	{
		memset(used, 0, sizeof(used));
		memset(w, 0, sizeof(w));
		memset(f, 0, sizeof(f));
		memset(res, 0, sizeof(res));
		scanf("%d%d", &n, &m);
		gets(s);
		for(int i=0;i<n;i++)
		{
			gets(s);
			for(int j=0;j<m/4;j++)
			{
				int x;
				if(s[j] >= 'A' && s[j] <= 'F')
				{
					x = s[j] - 'A' + 10;
				}
				else 
				{
					x = s[j] - '0';
				}
				for(int k=3;k>=0;k--)
				{
					if(x & (1<<k))
					{
						f[i][(j*4) + (3-k)] = true;
					}
				}
			}
		}
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<m;j++)
			{
				if(j==0 && i==0)
				{
					w[i][j] = f[i][j];
				}
				else if(i == 0)
				{
					w[i][j] = w[i][j-1] + f[i][j];
				}
				else if(j == 0)
				{
					w[i][j] = w[i-1][j] + f[i][j];
				}
				else
				{
					w[i][j] = w[i-1][j] + w[i][j-1] - w[i-1][j-1] + f[i][j];
				}
			}
		}

		int sizes = 0;
		for(int sz = min(n,m);sz >= 1; sz--)
		{
			bool found = false;
			for(int i=0;i<=n-sz;i++)
			{
				for(int j=0;j<=m-sz;j++)
				{
					if(used[i][j] || used[i+sz-1][j] || used[i][j+sz-1] || used[i+sz-1][j+sz-1])
					{
						continue;
					}
					int cnt = w[i+sz-1][j+sz-1];
					if(i > 0)
					{
						cnt -= w[i-1][j+sz-1];
					}
					if(j > 0) 
					{
						cnt -= w[i+sz-1][j-1];
					}
					if(i > 0 && j > 0)
					{
						cnt += w[i-1][j-1];
					}
					if(sz % 2 == 0 && cnt != (sz*sz)/2)
					{
						continue;
					}
					if(sz % 2 == 1 && 
						((cnt % 2 == 0 && cnt != (sz*sz)/2)) || 
						 (cnt % 2 == 1 && cnt - 1 != (sz*sz)/2))
					{
						continue;
					}
					for(int ii=i;ii<i+sz;ii++)
					{
						for(int jj=j;jj<j+sz;jj++)
						{
							if(ii > i && f[ii][jj] == f[ii-1][jj])
							{
								goto no;
							}
							if(ii < i+sz-1 && f[ii][jj] == f[ii+1][jj])
							{
								goto no;
							}
							if(jj > j && f[ii][jj] == f[ii][jj-1])
							{
								goto no;
							}
							if(jj < j+sz-1 && f[ii][jj] == f[ii][jj+1])
							{
								goto no;
							}
						}
					}
					found = true;
					res[sz]++;
					for(int ii=i;ii<i+sz;ii++)
					{
						for(int jj=j;jj<j+sz;jj++)
						{
							used[ii][jj] = sz;
						}
					}
					out();
no:;
				}
			}
			if(found)
			{
				sizes++;
			}
		}
out();
		printf("Case #%d: %d\n", tt, sizes);
		cerr<<tt<<endl;
		for(int i=min(n,m);i>=1;i--)
		{
			if(res[i])
			{
				printf("%d %d\n", i, res[i]);
			}
		}
	}
	return 0;
}
