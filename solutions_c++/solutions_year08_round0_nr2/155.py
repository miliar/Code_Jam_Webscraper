#include <iostream>
#include <string>
#include <fstream>

using namespace std;

ifstream fin("B-large.in");
ofstream fout("B-large.out");

const int maxn = 200;

int n1,n2;
int t;
bool g[maxn][maxn];
int ta1[maxn],ta2[maxn],tb1[maxn],tb2[maxn];
int cx[maxn],cy[maxn];
bool sy[maxn];

int convert(string t)
{
	return ((t[0]-'0')*10+t[1]-'0')*60+(t[3]-'0')*10+t[4]-'0';
}

bool find(int u)
{
	for (int v=1; v<=n2; ++v)
	    if (g[u][v] && !sy[v])
	    {
			sy[v] = 1;
			if (cy[v]==0 || find(cy[v]))
			{
				cx[u]=v;
				cy[v]=u;
				return 1;
			}
		}
	return 0;
}

int hungary()
{
	memset(cx,0,sizeof(cx));
	memset(cy,0,sizeof(cy));
	for (int i = 1; i <= n1; ++i)
	{
		memset(sy,0,sizeof(sy));
		find(i);
	}
	int ret = 0;
	for (int i = 1; i <= n1; ++i)
	    if (cx[i] > 0) ret++;
	return ret;
}

void solve()
{
	fin >> t >> n1 >> n2;
	for (int i = 1; i <= n1; ++i)
	{
		string time1,time2;
		fin >> time1 >> time2;
		ta1[i] = convert(time1);
		tb1[i] = convert(time2);
	}
	for (int i = 1; i <= n2; ++i)
	{
		string time1,time2;
		fin >> time1 >> time2;
		ta2[i] = convert(time1);
		tb2[i] = convert(time2);
	}
	memset(g,0,sizeof(g));
	for (int i = 1; i <= n1; ++i)
	    for (int j = 1; j <= n2; ++j)
			g[i][j] = tb2[j]+t <= ta1[i];

	fout << n1-hungary() << " ";

	memset(g,0,sizeof(g));
	for (int i = 1; i <= n1; ++i)
	    for (int j = 1; j <= n2; ++j)
			g[i][j] = tb1[i]+t <= ta2[j];
	fout << n2-hungary() << endl;
	
}

int main()
{
	int tc;
	fin >> tc;
	for (int i = 1; i <= tc; ++i)
	{
		fout << "Case #" << i << ": ";
		solve();
	}
	fin.close();
	fout.close();
	return 0;
}
