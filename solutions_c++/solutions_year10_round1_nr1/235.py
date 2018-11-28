// GCJ 2010 Round 1
// 1. Rotate

// May 22, 2010
// wookayin

#include <stdio.h>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

vector<string> a;
int n, K;

vector<string> rot(vector<string> &a)
{
	vector<string> x = a;
	for(int i=0; i<n; ++i) 
	{
		for(int j=0; j<n; ++j)
		{
			x[j][n-i-1] = a[i][j];
		}
	}
	return x;
}

vector<string> gra(vector<string> &a)
{
	vector<string> x = a;
	for(int i=0; i<n; ++i)
		for(int j=0; j<n; ++j)
			x[i][j] = '.';

	for(int j=0; j<n; ++j)
	{
		vector<char> temp;
		for(int i=n-1; i>=0; --i)
		{
			if(a[i][j] != '.')
				temp.push_back(a[i][j]);
		}
		int q=0;
		for(int i=n-1; i>=0 && q < temp.size(); --i)
			x[i][j] = temp[q++];
	}
	return x;
}

void solve()
{
	vector<string> r = gra(rot(a));
	int dx[] = {1, 0, 1, 1};
	int dy[] = {0, 1, -1, 1};

	bool ok[128] = {0,};
	for(char *p = "BR"; *p; ++p)
	{
		for(int i=0; i<n; ++i)
		{
			for(int j=0; j<n; ++j)
			{
				for(int q=0; q<4; ++q)
				{
					bool err = false;
					for(int amt = 0; amt < K & !err; ++ amt)
					{
						int ii = i + dx[q]*amt;
						int jj = j + dy[q]*amt;
						if(ii < 0 || jj < 0 || ii >= n || jj >= n) {
							err = true;
							break;
						}
						if(r[ii][jj] != *p)
							err = true;
					}
					if(!err) ok[*p] = true;
				}
			}
		}
	}

	if(ok['R'] && ok['B'])
		puts("Both");
	if(!ok['R'] && !ok['B'])
		puts("Neither");
	if(ok['R'] && !ok['B']) puts("Red");
	if(ok['B'] && !ok['R']) puts("Blue");
}

void input()
{
	scanf("%d %d", &n, &K);
	a.resize(n);
	char buf[55];
	for(int i=0; i<n; ++i)
	{
		scanf("%s", buf);
		a[i] = buf;
	}
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int T, tt;
	scanf("%d", &T);
	for(tt=1; tt<=T; ++tt)
	{
		input();
		printf("Case #%d: ", tt);
		solve();
	}
	return 0;
}