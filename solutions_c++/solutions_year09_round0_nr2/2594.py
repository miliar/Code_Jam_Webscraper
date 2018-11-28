#include <iostream>
#include <algorithm>
using namespace std;

int a[102][102];
char b[102][102];
int n, m;
int di[4] = {-1,0,0,1};
int dj[4] = {0,-1,1,0};

struct tr
{
	int i,j,a;
	bool operator<(tr&other) const
	{
		if(a != other.a)
		{
			return a > other.a;
		}
		if(i != other.i)
		{
			return i < other.i;
		}
		if(j != other.j)
		{
			return j < other.j;
		}
	}
} all[10005];

bool good(int i, int j)
{
	return i >= 0 && i < n && j >= 0 && j < m;
}

int fill(int i, int j, int c)
{
	if(b[i][j] >= 0)
	{
		return b[i][j];
	}
	int ib = -1;
	int jb = -1;
	for(int w=0;w<4;w++)
	{
		if(good(i+di[w],j+dj[w]) && a[i+di[w]][j+dj[w]] < a[i][j] && (ib == -1 || a[i+di[w]][j+dj[w]] < a[ib][jb]))
		{
			ib = i+di[w];
			jb = j+dj[w];
			
		}
	}
	if(ib >= 0) 
	{
		return b[i][j] = fill(ib, jb, c);
	}
	return b[i][j] = c;
}

void fill2(int i, int j, char c, int old)
{
	b[i][j] = c;
	for(int w=0;w<4;w++)
	{
		if(good(i+di[w],j+dj[w]) && b[i+di[w]][j+dj[w]] == old)
		{
			fill2(i+di[w], j+dj[w], c, old);
		}
	}
}

int main()
{
	freopen("c:\\B-small.in", "r", stdin);
	freopen("c:\\B.out", "w", stdout);
	int t;
	cin>>t;
	int xx = 1;
	while(t--)
	{
		cin>>n>>m;
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<m;j++)
			{
				scanf("%d", &a[i][j]);
				all[i*m+j].a = a[i][j];
				all[i*m+j].i = i;
				all[i*m+j].j = j;
			}
		}
		sort(all, all+n*m);
		memset(b, -1, sizeof(b));
		int cur = 0;
		for(int i=0;i<n*m;i++)
		{
			if(b[all[i].i][all[i].j] == -1)
			{
				fill(all[i].i, all[i].j, cur++);
			}
		}
		char c = 'a';
		printf("Case #%d:\n", xx++);
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<m;j++)
			{
				if(b[i][j] < 'a')
				{
					fill2(i,j,c++,b[i][j]);
				}
				printf("%c", b[i][j]);
				if(j< m-1) printf(" ");
			}
			cout<<endl;
		}
	}
	return 0;
}
/*
5
3 3
9 6 3
5 9 6
3 5 9
1 10
0 1 2 3 4 5 6 7 8 7
2 3
7 6 7
7 6 7
5 5
1 2 3 4 5
2 9 3 9 6
3 3 0 8 7
4 9 8 9 8
5 6 7 8 9
2 13
8 8 8 8 8 8 8 8 8 8 8 8 8
8 8 8 8 8 8 8 8 8 8 8 8 8
*/