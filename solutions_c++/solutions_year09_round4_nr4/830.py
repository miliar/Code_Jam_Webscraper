#include<cstdio>
#include<cstring>
#include<string>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<iostream>
#include<sstream>
#include<fstream>
#include<cmath>

using namespace std;

int n;
vector<double> x, y, r;
double tryTwo(int ind1, int ind2)
{
	return r[ind1]+r[ind2]+sqrt((x[ind1]-x[ind2])*(x[ind1]-x[ind2]) + (y[ind1]-y[ind2])*(y[ind1]-y[ind2]));
}
int main()
{
	freopen("D-small-attempt2.in", "r", stdin);
	freopen("D-small-attempt2.out", "w", stdout);

	int numCase;
	scanf("%d", &numCase);
	for(int c=1; c<=numCase; c++)
	{
		scanf("%d", &n);
		x.clear();
		y.clear();
		r.clear();
		
		for(int i=0; i<n; i++)
		{
			double tx,ty,tr;
			scanf("%lf %lf %lf", &tx,&ty,&tr);
			x.push_back(tx);
			y.push_back(ty);
			r.push_back(tr);
		}
		double ans;
		if(n == 1)
		{
			ans = r[0]*2;
		}
		else if(n==2)
		{
			ans = max(r[0]*2,r[1]*2);
		}
		else
		{
			ans = max(tryTwo(0,1), r[2]*2);
			ans = min(ans, max(tryTwo(0,2), r[1]*2));
			ans = min(ans, max(tryTwo(1,2), r[0]*2));
		}
		printf("Case #%d: %lf\n", c, ans/2);
	}

	return 0;
}
