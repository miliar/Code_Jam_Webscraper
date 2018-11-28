#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
int a[110][110], b[110][110];
int main()
{
	ifstream fin("d.in");
	ofstream fout("d.out");
	int i, j, n, k, l, m, t, T, res, h, w;
	fin>>T;
	for (t=1;t<=T;t++)
	{
		fin>>h>>w>>k;
		for (i=1;i<=h;i++)
			for(j=1;j<=w;j++)
			{
				b[i][j]=1;
				a[i][j]=0;
			}
		for (i=0;i<k;i++)
		{
			fin>>j>>n;
			b[j][n]=0;
		}
		a[1][1]=1;
		for (i=1;i<=h;i++)
			for(j=1;j<=w;j++)
			{
				if (!b[i][j])
					continue;
				if (i-1>=1 && j-2>=1 && a[i-1][j-2])
					a[i][j]=(a[i][j]+a[i-1][j-2])%10007;

				if (i-2>=1 && j-1>=1 && a[i-2][j-1])
					a[i][j]=(a[i][j]+a[i-2][j-1])%10007;
			}
		res=a[h][w];
		fout<<"Case #"<<t<<": "<<res<<endl;
	}
	fin.close();
	fout.close();
	return 0;
}