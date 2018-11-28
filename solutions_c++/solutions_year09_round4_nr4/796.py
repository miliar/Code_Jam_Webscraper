#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <set>
#include <map>
#include <cstring>
#include <cstdio>
#include <cmath>

using namespace std;
FILE *fp;

struct Node
{
	double x,y;
	double r;
};

Node no[10];

int t,n;

double dist(double x0,double y0,double x1,double y1)
{
	return sqrt((x0 - x1) * (x0 - x1) + (y0 - y1) * (y0 - y1));
}

double mmin;

double get(int i,int j)
{
	return (dist(no[i].x,no[i].y,no[j].x,no[j].y) + no[i].r + no[j].r) / 2.0;
}

int main()
{
	fp = fopen("out.txt","w");
	cin >> t;
	int r = 1;
	while(--t >= 0)
	{
		cin >> n;
		
		for(int i = 0;i < n;i ++)
		{
			cin >> no[i].x >>no[i].y >>no[i].r;
		}
		if(n == 1)
		{
			fprintf(fp,"Case #%d: %.6lf\n",r,no[0].r);
		    r ++;
			continue;
		}
		if(n == 2)
		{
			mmin = max(no[0].r,no[1].r);
			fprintf(fp,"Case #%d: %.6lf\n",r,mmin);
		    r ++;
			continue;
		}


		//mmin = 1e99;
		mmin = max(get(0,1),no[2].r);
		mmin = min(mmin,max(get(0,2),no[1].r));
		mmin = min(mmin,max(get(1,2),no[0].r));
		fprintf(fp,"Case #%d: %.6lf\n",r,mmin);
		r ++;
	}






	return 0;
}
