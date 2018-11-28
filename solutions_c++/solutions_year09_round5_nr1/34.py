#include <iostream>
#include <vector>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cstring>
#include <string>
#include <map>
#include <algorithm>

using namespace std;

struct Tpoint
{
	int x,y;
}box[10], pos[10];
int nbox, npos;

int	n,m;
char board[13][13];
int a[13][13];
map<string, int> f;
vector<string> q;

void	init()
{
	scanf("%d%d",&n,&m);
	for (int i=0; i<n; i++)
		scanf("%s",board[i]);
}

string inital, goal;
bool flag;
int cur;

string	opt(Tpoint *a, int len)
{
	string ret = "";
	for (int i=0; i<len; i++)
	{
		if (a[i].x<10)
			ret = ret+"0"+(char)(a[i].x+'0');
		else if (a[i].x==10)
			ret = ret+"10";
		else if (a[i].x==11)
			ret = ret+"11";
		if (a[i].y<10)
			ret = ret+"0"+(char)(a[i].y+'0');
		else if (a[i].y==10)
			ret = ret+"10";
		else if (a[i].y==11)
			ret = ret+"11";
	}
	return ret;
}

void	sort(Tpoint *a, int len)
{
	int t;
	for (int i=0; i<len; i++)
		for (int j=i+1; j<len; j++)
			if (a[j].x<a[i].x||(a[j].x==a[i].x&&a[j].y<a[i].y))
			{
				t=a[i].x;a[i].x=a[j].x;a[j].x=t;
				t=a[i].y;a[i].y=a[j].y;a[j].y=t;
			}
}

void	prepare()
{
	nbox = 0;
	npos = 0;
	for (int i=0; i<n; i++)
		for (int j=0; j<m; j++)
			if (a[i][j]>0)
			{
				if ((a[i][j]&1)==1)
				{
					box[nbox].x = i;
					box[nbox].y = j;
					nbox++;
				}
				if ((a[i][j]&2)==2)
				{
					pos[npos].x = i;
					pos[npos].y = j;
					npos++;
				}
				if (a[i][j]>0)
					a[i][j]=0;
			}
	inital = "", goal = "";
	sort(box, nbox);
	sort(pos, npos);
	if (nbox!=npos)
		return;
	inital = opt(box, nbox);
	goal = opt(pos, npos);
}

int fa[6];
int bfsx[6];
int bfsy[6];

bool	checkSafe(int n)
{
	for (int i=0; i<n; i++)
		fa[i] = i;
	for (int i=0; i<n; i++)
		for (int j=i+1; j<n; j++)
			if (abs(bfsx[i]-bfsx[j])+abs(bfsy[i]-bfsy[j])==1)
			{
				int xx = i, yy = j;
				while (fa[xx]!=xx) xx=fa[xx];
				while (fa[yy]!=yy) yy=fa[yy];
				if (xx!=yy)
					fa[yy]=xx;
			}
	for (int i=0; i<n; i++)
	{
		while (fa[i]!=fa[fa[i]]) fa[i]=fa[fa[i]];
		if (fa[i]!=fa[0])
			return false;
	}
	return true;
}

void	push(int K)
{
	if (!flag)
		if (!checkSafe(K))
			return;
	int x[6],y[6];
	for (int i=0; i<K; i++)
	{
		x[i] = bfsx[i];
		y[i] = bfsy[i];
	}
	for (int i=0; i<K; i++)
		for (int j=i+1; j<K; j++)
			if (x[j]<x[i]||(x[j]==x[i]&&y[j]<y[i]))
			{
				int t=x[i];x[i]=x[j];x[j]=t;
				t=y[i];y[i]=y[j];y[j]=t;
			}

	int step = cur+1;
	string opt = "";
	for (int i=0; i<K; i++)
	{
		if (x[i]<10)
			opt = opt + "0"+(char)(x[i]+'0');
		else if (x[i]==10)
			opt = opt + "10";
		else if (x[i]==11)
			opt = opt + "11";
		if (y[i]<10)
			opt = opt + "0"+(char)(y[i]+'0');
		else if (y[i]==10)
			opt = opt + "10";
		else if (y[i]==11)
			opt = opt + "11";
	}
	map<string,int>::iterator it;
	it = f.find(opt);
	if (it!=f.end())
		return;
	f.insert(make_pair(opt, step));
	q.push_back(opt);
}

int bfsmap[13][13];

void	bfs(string opt)
{
	memset(bfsmap,0,sizeof(bfsmap));
	int K=opt.size()/4;
	for (int i=0; i<K; i++)
	{
		bfsx[i] = (opt[i*4]-'0')*10+opt[i*4+1]-'0';
		bfsy[i] = (opt[i*4+2]-'0')*10+opt[i*4+3]-'0';
		bfsmap[bfsx[i]][bfsy[i]]=1;
	}

	for (int i=0; i<K; i++)
	{
		bool goX = false;
		bool goY = false;
		if (bfsx[i]>0&&bfsx[i]<n-1&&a[bfsx[i]-1][bfsy[i]]==0&&a[bfsx[i]+1][bfsy[i]]==0&&
			bfsmap[bfsx[i]-1][bfsy[i]]==0&&bfsmap[bfsx[i]+1][bfsy[i]]==0)
			goX = true;
		if (bfsy[i]>0&&bfsy[i]<m-1&&a[bfsx[i]][bfsy[i]-1]==0&&a[bfsx[i]][bfsy[i]+1]==0&&
			bfsmap[bfsx[i]][bfsy[i]-1]==0&&bfsmap[bfsx[i]][bfsy[i]+1]==0)
			goY = true;
		if (goX == true)
		{
			bfsx[i]--;
			push(K);
			bfsx[i]+=2;
			push(K);
			bfsx[i]--;
		}
		if (goY == true)
		{
			bfsy[i]--;
			push(K);
			bfsy[i]+=2;
			push(K);
			bfsy[i]--;
		}
	}
}

int x[6];
int y[6];
bool	checkSafe(string opt)
{
	int n=opt.size()/4;
	for (int i=0; i<n; i++)
	{
		x[i] = (opt[i*4]-'0')*10+opt[i*4+1]-'0';
		y[i] = (opt[i*4+2]-'0')*10+opt[i*4+3]-'0';
		fa[i] = i;
	}
	for (int i=0; i<n; i++)
		for (int j=i+1; j<n; j++)
			if (abs(x[i]-x[j])+abs(y[i]-y[j])==1)
			{
				int xx = i, yy = j;
				while (fa[xx]!=xx) xx=fa[xx];
				while (fa[yy]!=yy) yy=fa[yy];
				if (xx!=yy)
					fa[yy]=xx;
			}
	for (int i=0; i<n; i++)
	{
		while (fa[i]!=fa[fa[i]]) fa[i]=fa[fa[i]];
		if (fa[i]!=fa[0])
			return false;
	}
	return true;
}

void	solve()
{
	for (int i=0; i<n; i++)
		for (int j=0; j<m; j++)
			if (board[i][j]=='.')
				a[i][j]=0;
			else if (board[i][j]=='#')
				a[i][j]=-1;
			else if (board[i][j]=='x')
				a[i][j]=2;
			else if (board[i][j]=='o')
				a[i][j]=1;
			else if (board[i][j]=='w')
				a[i][j]=3;
	f.clear();
	q.clear();
	prepare();
	if (nbox!=npos)
	{
		printf("-1\n");
		return;
	}

	q.push_back(inital);
	f.insert(make_pair(inital, 0));
	int op = 0;
	while (op<q.size())
	{
		inital = q[op];
		if (inital==goal)
		{
			printf("%d\n", f[inital]);
			return;
		}
		cur = f[inital];
		flag = false;
		if (checkSafe(inital))
			flag = true;

		bfs(inital);
		op++;
	}
	printf("-1\n");
	return;
}

int	main()
{
//	freopen("in.txt", "r", stdin);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.txt", "w", stdout);

	int	T;
	scanf("%d", &T);
	
	for (int t = 1; t <= T; t ++)
	{
		printf("Case #%d: ", t);

		init();
		solve();
	}

	return 0;
}
