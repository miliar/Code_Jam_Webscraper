#include <cassert>
#include <cmath>
#include <cstdio>
#include <set>
#include <string>
#include <vector>
#include <time.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#pragma comment(linker, "/STACK:10000000")
using namespace std;

int arr[20][1<<15];
int mincost[20][20][1<<15];
const int inf = 1000000000;

int mcf(int l, int kmax, int j)
{
	int res = inf;
	for (int k=0;k<=kmax;k++)
		res = min(res, mincost[l][k][j]);
	return res;
}

int main()
{ 
/*	time_t ct = time(0);
	int dt =20*60 + 0*1800 +10*3600;//5*3600 + 1800;
	while (time(0) - ct < dt)
	{
		cout<<(dt + ct - time(0))<<' ';
	}
	for (;;)
	{
		cout<<char(7);
	}
	return 0;*/

	ifstream cin("input.txt");
	ofstream cout("output.txt");

	int tn;
	cin>>tn;
	for (int aaa=0;aaa<tn;aaa++)
	{
		int ans = 0;
		int n;
		cin>>n;
		vector<int> m(1<<n);
		for (int i=0;i<(1<<n);i++)
			cin>>m[i];
		memset(arr,0,sizeof(arr));
		for (int i=n-1;i>=0;i--)
			for (int j=0;j<(1<<i);j++)
				cin>>arr[n-i - 1][j];

		for (int i=0;i<=n;i++)
			for (int j=0;j<(1<<(n-i));j++)
			{
				if (i == 0)
				{
					for (int k=0;k<15;k++)
						if (n - 1 - m[j] >= k)
							mincost[i][k][j] = inf;
						else
							mincost[i][k][j] = 0;
				}
				else
				{
					int jl = (j << 1);
					int jr = jl + 1;
					for (int k=0;k<15;k++)
					{
						//get
						int c = arr[i-1][j];
						c += mcf(i-1, k+1, jl);
						c += mcf(i-1, k+1, jr);
						mincost[i][k][j] = c;
						//unget
						c = mcf(i-1,k,jl) + mcf(i-1,k,jr);
						mincost[i][k][j] = min(mincost[i][k][j],  c);
					}
				}
			}

		cout<<"Case #"<<aaa+1<<": "<<mincost[n][0][0]<<endl;
	}

	return 0;
}