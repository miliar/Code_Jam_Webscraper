#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
#define SZ(x) (int)(x.size())
#define F0(i,n) for(i=0;i<n;i++)
#define F1(i,n) for(i=1;i<=n;i++)
const int inf = 1000000009;
const double pi = atan(1.0)*4.0;
const double eps = 1e-8;

int i, j, k, m, n, l;

int N,M,A;

int main(void)
{

	freopen("c:\\Temp\\B-small.in", "r", stdin);
	freopen("c:\\Temp\\B-small.out", "w", stdout);
	int CC;
	cin >> CC;
	for (int cc=1;cc<=CC;++cc)
	{
		cin >>N >> M >> A;

		cout << "Case #" << cc << ": ";

		if (N*M < A ) {
			cout << "IMPOSSIBLE" << endl;
			continue;
		}
		int found=0;
		for(int x2 = 0; x2<=N; ++x2)
		{
			if (found) break;
			for(int y2=0;y2<=M;++y2)
			{
				if (found) break;
				for(int x3=0; x3<=N; ++x3)
				{
					if (found) break;
					for (int y3 = 0; y3<=M; ++y3)
					{
						if (found) break;
						if (x2==0 && y2==0) break;
						if (x3==0 && y3==0) break;
						if (x2==y2 && x3==y3) break;
						int ss = x2*y3 - x3*y2;
						if (ss == A || ss == -A) 
						{
							printf("%d %d %d %d %d %d\n",0,0,x2,y2,x3,y3);
							found = 1;
						}
					}
				}
			}
		}
		if (!found)
		cout << "IMPOSSIBLE" << endl;
	}
}
