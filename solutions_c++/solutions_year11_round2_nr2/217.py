#include <iomanip>
#include <algorithm>
#include <map>
#include <fstream>
#include <stack>
#include <queue>
#include <vector>
#include <cmath>
#include <iostream>
#include <string>
#include <set>

#include <time.h>
#include <sys/time.h>

using namespace std;

#define con 1e15

vector<int> a;
int n,d,N;

bool f(double t)
{
//	cout << fixed << setprecision(5) << endl;
//	cout << t << endl;
	double c = -100001;
	c *= con;
	for (int i = 0; i < N; i++)
	{
		double r1 = a[i] - t;
		double r2 = a[i] + t;
		c+=d;
		if (c > r2) return false;
		if (r1 > c) c = r1;
//		cout << c << " ";
	}
/*	cout << endl;
	cout << " ----- " << endl;*/
	return true;
};

int main()
{
//	freopen("anarc05b.in","r",stdin);
//	freopen("anarc05b.out","w",stdout);
	int t;
	scanf("%d",&t);
	for (int T = 0; T < t; T++)
	{
		printf("Case #%d: ",T+1);		
		scanf("%d%d",&n,&d);
		N = 0;
		a.clear();
		for (int i = 0; i < n; i++)
		{
			int x,y;
			scanf("%d%d",&x,&y);
			for (int j = 0; j < y; j++)
				a.push_back(x);
		}

		N = a.size();
		sort(a.begin(),a.end());
			
		double l = 0.0;
		double r = con;

		for (int dix = 0; dix < 500; dix++)
		{
			double mid = (l+r) / 2;

//			cout << l << " " << r << endl;
	

			if (f(mid)) r = mid;
			else l = mid;
		}

		printf("%.9lf\n",l);
	}

//	in.getline(s);

	return 0;	
}
