#include <iostream>
#include <math.h>
using namespace std;
struct coord
{
	int x;
	int y;
	int r;
}plant[3];
double work(coord a, coord b)
{
	if(a.r < 0)
	{
		if(b.r < 0) return 0.00;
		else return (double)b.r;
	}
	double ret = sqrt((double)((a.x-b.x)*(a.x-b.x) + (a.y-b.y)*(a.y-b.y)));
	ret = ret + a.r;
	ret = ret + b.r;
	return ret*0.50;
}
int main()
{
	int c, tc;
	cin >> c;
	for(tc = 1; tc <= c; tc++)
	{
		int n;
		cin >> n;
		double ans = 100000.000;
		for(int i=0; i<3; i++) plant[i].r = -1;
		for(int i=0; i<n; i++)
		{
			cin >> plant[i].x >> plant[i].y >> plant[i].r;
		}
		for(int i=0; i<3; i++)
		{
			int j = (i+1)%3;
			int k = (i+2)%3;
			double t = work(plant[j],plant[k]);
			if(t < plant[i].r - 0.000001) t = plant[i].r;
			if(t < ans - 0.000001) ans = t;
		}
		cout << "Case #" << tc << ": " << ans << endl;
	}
	return 0;
}
