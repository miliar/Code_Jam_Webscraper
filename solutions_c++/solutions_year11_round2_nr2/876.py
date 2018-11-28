#include<iostream>
#include<cmath>
double temp;
double max;
int t,c,d;
double a,b;
double loc[1000100],tt[1000100];
int nowloc;
int tempnow;
int total;
double low,high, mid, ans;
#define ep (1e-8)
using namespace std;
bool solve(double l)
{
	double pay= 0 ;
	double ds = 0;
	for (int i = 0 ; i < total ; ++i)
	tt[i] = loc [i];
	tt [0] = tt[0] - l;
	for (int i = 1; i < total; ++i)
	{
	if(tt[i] < tt[i-1] - ep) {
			pay = d + fabs(tt[i] - tt[i-1]);
			if(pay>l+ep) return false;
			else tt[i] = tt[i-1] + d;
		}
		else {
			ds = fabs(tt[i] - tt[i-1]);
			if(ds< d) {
				pay  = d - ds;
				if(pay > l + ep) return false;
				else tt[i] = tt[i-1] + d;
			}
			else {
				double low = ds - d;
				if(low >l) low = l;
				tt[i] =tt[i] - low;
			}
		}
		
	}
	return true;
}
int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	cin >> t;
	for (int  l = 1;  l <= t; ++l)
	{
		cin >> c >> d;	
		total = 0;
		temp = 0;
		for (int i = 0 ; i < c ; ++i)
		{
			cin >> a >> b;
			for (int j = 1; j <= b; j++)
			{
				loc[total++] = a;
			}
		}
	ans = -1000;
	high = d * 5e11;
	low = 0;
	while (low  <= high-ep)
	{
		mid = (low+ high)/2;
		if (solve(mid))
		{
			high = mid - ep;
			ans = mid;
		}
		else low = mid + ep;
	}	
		cout << "Case #"<<l<<": ";
		printf("%.9lf\n",ans);
	}
}
