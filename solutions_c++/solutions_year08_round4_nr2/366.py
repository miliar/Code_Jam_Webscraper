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
int main()
{
	ifstream fin("a.in");
	ofstream fout("a.out");
	int i, j, n, k, l, m, t, T, s;
	fin>>T;
	for (t=1;t<=T;t++)
	{
		fin>>n>>m>>s;
		int x1,x2, y1, y2, res=0;
		double y;
		for (x1=1;x1<=n;x1++)
			for (x2=0;x2<=n;x2++)
				for (y1=0;y1<=m;y1++)
				{
					y=((double)(x2*y1+s)/(double)x1);
					if (fabs(y-((x2*y1+s)/x1))<1e-9)
					{
						y2=(x2*y1+s)/x1;
						if (y2<=m && y2>=0)
						{
							res=1;
							fout<<"Case #"<<t<<": 0 0 "<<x1<<" "<<y1<<" "<<x2<<" "<<y2<<endl;
							goto l1;
						}
						
					}
					y=((double)(x2*y1-s)/(double)x1);
					if (fabs(y-((x2*y1-s)/x1))<1e-9)
					{
						y2=(x2*y1-s)/x1;
						if (y2<=m && y2>=0)
						{
							res=1;
							fout<<"Case #"<<t<<": 0 0 "<<x1<<" "<<y1<<" "<<x2<<" "<<y2<<endl;
							goto l1;
						}
						
					}
				}
						
/*		for (i=1;i<=n;i++)
		{
			if (fabs((double)s/(double)i-(double)(s/i))<1e-9 && s/i<=m)
			{
				x=i;
				y=s/i;
				res=1;
				break;
			}
		}
		if (res==1)
		{
			goto l1;

		}
		for (i=1;i<=m;i++)
		{
			if (fabs((double)s/(double)i-(double)(s/i))<1e-9 && s/i<=n)
			{
				y=i;
				x=s/i;
				res=1;
				break;
			}
		}*/
		fout<<"Case #"<<t<<": IMPOSSIBLE"<<endl;
l1:;


	}
	fin.close();
	fout.close();
	return 0;
}