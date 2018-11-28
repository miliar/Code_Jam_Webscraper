const double pi=3.1415926535897932, e=2.7182818284590452;
#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/stack:16000000")
#include <cstdio>
#include <cmath>
#include <complex>
#include <algorithm>
#include <functional>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
using namespace std;

int nn,n,m,a;

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	scanf("%d",&nn);
	for (int ii=0; ii<nn; ++ii)
	{
		scanf("%d%d%d",&n,&m,&a);
		bool fRes = false;
		for (int x1=0; x1<=n && !fRes; ++x1)
			for (int y1=0; y1<=m && !fRes; ++y1)
				for (int x2=0; x2<=n && !fRes; ++x2)
					for (int y2=0; y2<=m && !fRes; ++y2)
						if (labs(x1*y2-x2*y1)==a)
						{
							fRes = true;
							printf("Case #%d: 0 0 %d %d %d %d\n",ii+1,x1,y1,x2,y2);
						}
		if (!fRes)
			printf("Case #%d: IMPOSSIBLE\n",ii+1);

	}
	return 0;
}
