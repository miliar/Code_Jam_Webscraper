#include <iostream>
#include <fstream>
#include <set>
#include <map>
#include <vector>
#include <sstream>
#include <algorithm>
using namespace std;

__int64 d[1000][1000];
__int64 d2[1000][1000];
__int64 d3[1000][1000];
__int64 dpc[1000][1000];
__int64 dpc2[1000][1000];
__int64 dpc3[1000][1000];
int n,m;

__int64 getSum(int l, int t, int r, int b)
{
	++r;
	++b;
	return dpc[r][b] - dpc[r][t] - dpc[l][b] + dpc[l][t];
}
__int64 getSum2(int l, int t, int r, int b)
{
	++r;
	++b;
	return dpc2[r][b] - dpc2[r][t] - dpc2[l][b] + dpc2[l][t];
}
__int64 getSum3(int l, int t, int r, int b)
{
	++r;
	++b;
	return dpc3[r][b] - dpc3[r][t] - dpc3[l][b] + dpc3[l][t];
}

void prepare()
{
	memset(dpc, 0, sizeof(dpc));
	memset(dpc2, 0, sizeof(dpc2));
	memset(dpc3, 0, sizeof(dpc3));

	for (int i=0;i<n;i++)
		for (int j=0;j<m;j++)
		{
			d2[i][j] = d[i][j] * i;
			d3[i][j] = d[i][j] * j;
			dpc[i+1][j+1] = dpc[i][j+1] + dpc[i+1][j] - dpc[i][j] + d[i][j];
			dpc2[i+1][j+1] = dpc2[i][j+1] + dpc2[i+1][j] - dpc2[i][j] + d2[i][j];
			dpc3[i+1][j+1] = dpc3[i][j+1] + dpc3[i+1][j] - dpc3[i][j] + d3[i][j];
		}
}
bool test(int l, int t, int r, int b)
{
	__int64 s = getSum(l, t, r, b) - d[l][t] - d[l][b] - d[r][t] - d[r][b];
	__int64 s2 = getSum2(l, t, r, b) - d2[l][t] - d2[l][b] - d2[r][t] - d2[r][b];
	__int64 s3 = getSum3(l, t, r, b) - d3[l][t] - d3[l][b] - d3[r][t] - d3[r][b];
	return ( (l+r) * s == s2 * 2)  && ((t+b) * s == s3 * 2 );
}


int main()
{
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int taa;
	cin>>taa;
	cout.setf(ios_base::fixed);
	cout.precision(20);
	for (int aaa = 0; aaa < taa; aaa++)
	{
		int nu;
		cin>>n>>m>>nu;

		for (int i=0;i<n;i++)
			for (int j=0;j<m;j++)
			{
				char c;
				cin>>c;
				d[i][j] = c - '0';
			}

		prepare();

		int ans = -1;

		for (int k=3;k<=min(n,m);k++)
		{
			bool fl = false;
			for (int i=0;i+k <= n && !fl; i++)
				for (int j=0;j+k <= m && !fl;j++)
					if (test(i, j, i + k - 1, j + k - 1))
						fl = true;
			if (fl)
			{
				ans = k;
			}
		}

		cout<<"Case #"<<aaa + 1<<": ";
		if (ans == -1)
			cout<<"IMPOSSIBLE";
		else
			cout<<ans;
		cout<<endl;
	}
	
}