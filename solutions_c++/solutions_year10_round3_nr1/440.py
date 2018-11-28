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
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>

using namespace std;

typedef struct point
{
	int x;
	int y;
};
bool cmp(point a,point b)
{
	if(a.x<b.x)
		return true;
	return false;
}
int main()
{
	freopen("in.in","r",stdin);
	freopen("out.out","w",stdout);

	int T,n;
	cin>>T;

	int round=1;
	while (round<=T)
	{
		point p[1000];
		cin>>n;
		int x,y;
		for (int i=0;i<n;i++)
		{
			cin>>x>>y;
			p[i].x=x;
			p[i].y=y;
		}
		sort(p,p+n,cmp);
		int res=0;
		for (int i=1;i<n;i++)
		{
			for (int j=0;j<i;j++)
			{
				if(p[i].y<p[j].y)
					res++;
			}
		}
		cout<<"Case #"<<round<<": "<<res<<endl;
		round++;
	}
	return 0;
}