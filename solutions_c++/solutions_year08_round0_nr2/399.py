#include <cstdio>
#include <queue>
#include <vector>
using namespace std;

struct st
{
	int t1;
	int t2;
	st(){t1=t2=0;}
	st(int tt1, int tt2){ t1 = tt1, t2 = tt2; }

};

int T;
int n;
int n1, n2;
vector<st> data;
int edge[510][510];

int network(int, int);
int main()
{
	int t;
	int i, j;
	int  loop = 0;

	freopen("B-large.in", "r", stdin);
	freopen("B.txt", "w", stdout);

	scanf("%d", &t);
	while(t--)
	{
		fill(edge[0], edge[0]+510*510, 0);
		data.clear();
		scanf("%d", &T);
		scanf("%d %d", &n1, &n2);

		n = n1 + n2;
		data.resize(n);
		for(i=0; i<n; i++)
		{
			int a, b, c, d;
			scanf("%d:%d %d:%d", &a, &b, &c, &d);
			data[i] = st(a*60+b, c*60+d);
		}

		int s, e;
		s = 0; e = n*2+1;
		for(i=0; i<n; i++) edge[s][i+1] = edge[n+i+1][e] = 1;
		for(i=0; i<n; i++)
		{
			for(j=0; j<n; j++)
			{
				if(i<n1 && j>=n1 && data[i].t2+T<=data[j].t1)
				{
					edge[i+1][n+j+1] = 1;
				}
				if(i>=n1 && j<n1 && data[i].t2+T<=data[j].t1)
				{
					edge[i+1][n+j+1] = 1;
				}
			}
		}
		while(network(s, e));

		int res1, res2;
		res1 = res2 = 0;
		for(i=n+1; i<=n*2; i++)
		{
			if(edge[i][e]==1)
			{
				if(i-n<=n1) res1++;
				else res2++;
			}
		}
		printf("Case #%d: %d %d\n", ++loop, res1, res2);
	}

	return 0;
}

int network(int s, int e)
{
	queue<int> q;
	int via[510], chk[510];
	int c;

	fill(via, via+510, 0);
	fill(chk, chk+510, 0);

	q.push(s);
	chk[s] = 1; via[s] = -1;
	while(!q.empty())
	{
		c = q.front(); q.pop();
		if(c==e) break;
		for(int i=s; i<=e; i++)
		{
			if(chk[i] || edge[c][i]==0) continue;
			chk[i] = 1;
			via[i] = c;
			q.push(i);
		}
	}
	if(c==e)
	{
		while(c!=s)
		{
			edge[via[c]][c] = 0;
			edge[c][via[c]] = 1;
			c = via[c];
		}
		return 1;
	}
	return 0;
}
