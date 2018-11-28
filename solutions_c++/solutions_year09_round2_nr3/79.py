#pragma comment (linker, "/STACK:64000000")
#include <string>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <math.h>
#include <sstream>
#include <iostream>
#include <queue>
#include <set>
#include <map>

#define ABS(x) ((x)<0?-(x):(x))
#define SQR(x) ((x)*(x))
#define PB push_back
#define MP make_pair
#define SS stringstream
#define LL long long
#define LD long double
#define SZ(x) int(x.size())
#define ALL(x) x.begin(),x.end()
#define FOR(a,b) for(int a=0;a<b;a++)
#define DFOR(a,b) for(int a=b-1;a>=0;a--)
#define CLR(a,b) memset(a,b,sizeof(a))

using namespace std;

struct st
{
	int i, j, diff;
	bool flag;
	st() {}
	st(int i, int j, int diff, bool flag) : i(i), j(j), diff(diff), flag(flag) {}
};

struct edge
{
	char c1, c2;
	int i, j, diff;
	st from;
	edge(char c1, char c2, int i, int j, int diff, st from) : c1(c1), c2(c2), i(i), j(j), diff(diff), from(from) {}
	friend bool operator < (const edge &u, const edge &v)
	{
		if (u.c1 != v.c1) return u.c1 < v.c1;
		return u.c2 < v.c2;
	}
};

#define maxd 400

int d[20][20][maxd];
st from[20][20][maxd];
char from1[20][20][maxd], from2[20][20][maxd];
const int D = 200;


int w;
queue<st> q;
char a[22][22];

int di[] = {-1,1,0,0};
int dj[] = {0,0,-1,1};

bool push(st s, int dist, st fr, char f1, char f2)
{
	int dd = s.diff + D;
	if (dd < 0 || dd >= maxd) return false;
	if (d[s.i][s.j][dd] != -1) return false;
	d[s.i][s.j][dd] = dist;
	from[s.i][s.j][dd] = fr;
	from1[s.i][s.j][dd] = f1;
	from2[s.i][s.j][dd] = f2;
	q.push(s);
	return true;	
}


string restore(int i, int j, int diff)
{
	string res;
	while (true)
	{
		res += from2[i][j][diff];
		if (from1[i][j][diff] != 0)
			res += from1[i][j][diff];
		else
			break;
		st s = from[i][j][diff];
		i = s.i;
		j = s.j;
		diff = s.diff + D;
	}
	reverse(ALL(res));
	return res;
}

void solvecase() {
	int _q;
	scanf("%d%d", &w, &_q);
	for (int i = 0; i < w; i++)
		scanf("%s", a[i]);

	CLR(d, -1);
	while (!q.empty()) q.pop();

	for (char d = '0'; d <= '9'; d++)
	{
		bool was = false;
		for (int i = 0; i < w; i++)
			for (int j = 0; j < w; j++)			
			{				
				if (a[i][j] == d)
				{
					push(st(i,j,a[i][j]-'0',was), 0, st(), 0, a[i][j]);
					was = true;					
				}
			}
	}

	while (!q.empty())
	{
		vector<st> v;
		v.PB(q.front()); q.pop();
		while (!q.empty() && q.front().flag)
		{
			v.PB(q.front());
			q.pop();
		}

		vector<edge> e;
		for (int i = 0; i < v.size(); i++)
		{
			st &c = v[i];
			for (int d1 = 0; d1 < 4; d1++)
				for (int d2 = 0; d2 < 4; d2++)
				{
					int i2 = c.i + di[d1];
					int j2 = c.j + dj[d1];
					int i3 = i2 + di[d2];
					int j3 = j2 + dj[d2];
					if (i2 < 0 || j2 < 0 || i2 >= w || j2 >= w) continue;
					if (i3 < 0 || j3 < 0 || i3 >= w || j3 >= w) continue;
					int t;
					if (a[i2][j2] == '+')
					{
						t = a[i3][j3] - '0';
					}
					else if (a[i2][j2] == '-')
					{
						t = -(a[i3][j3] - '0');
					}
					else
					{
						abort();
					}
					e.PB(edge(a[i2][j2], a[i3][j3], i3, j3, c.diff + t, c));
				}
		}

		sort(ALL(e));

		int newdist = d[v[0].i][v[0].j][v[0].diff + D] + 1;
		int z = e.size();
		for (int i = 0; i < z; i++)
		{
			int j = i;
			while (j+1 < z && e[j].c1 == e[j+1].c1 && e[j].c2 == e[j+1].c2) j++;
			bool was = false;
			for (int t = i; t <= j; t++)
			{
				if (push(st(e[t].i, e[t].j, e[t].diff, was), newdist, e[t].from, e[t].c1, e[t].c2))
					was = true;
			}
			i = j;
		}
	}


	for (int _z = 0; _z < _q; _z++)
	{
		int t;
		scanf("%d", &t);

		int bestd = 1000000;
		for (int i = 0; i < w; i++)
			for (int j = 0; j < w; j++)
				if (d[i][j][t+D] != -1 && d[i][j][t+D] < bestd)
					bestd = d[i][j][t+D];

		//printf("%d\n", bestd);
		string ans = "z";
		for (int i = 0; i < w; i++)
			for (int j = 0; j < w; j++)
				if (d[i][j][t+D] == bestd)
				{					
					string tmp = restore(i, j, t+D);
					if (tmp < ans)
						ans = tmp;
				}
		printf("%s\n", ans.c_str());
	}
}

void solve() {
	int n;
	scanf("%d\n", &n);
	FOR(i, n) {
		printf("Case #%d:\n", i+1);
		solvecase();
		//printf("\n");
	}
}

int main() {
	freopen("x", "rt", stdin);
	//freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	solve();
	return 0;
}