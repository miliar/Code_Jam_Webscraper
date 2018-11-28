#include <stdio.h>
#include <iostream>
#include <cmath>

using namespace std;

int x[10], y[10], r[10];

int main()
{
	freopen("d.txt", "r", stdin);
	freopen("d.out", "w", stdout);
	int T, i, j, n;
	double d, dis, ans, cas=0;
	scanf("%d", &T);
while (T--)
{
	scanf("%d", &n);
	for (i=0; i<n; i++)
	  scanf("%d%d%d", &x[i], &y[i], &r[i]);
	if (n==1)
	{
		ans=r[0];
	}
	else 
	if (n==2)
	{
		if (r[0]>r[1]) ans=r[0];
		else ans = r[1];
	}
	else 
	if (n==3)
	{
		ans = 1e+15;
		for (i=0; i<3; i++)
		 for (j=i+1; j<3; j++)
		 {
		 	d=r[3-i-j]*2;
		 	dis=sqrt(1.0*(x[i]-x[j])*(x[i]-x[j])+1.0*(y[i]-y[j])*(y[i]-y[j]));
		 	dis += r[i]+r[j];
		 	if (r[i]*2>dis) dis=r[i];
		 	if (r[j]*2>dis) dis=r[j];
		 	if (dis>d) d=dis;
		 	if (d<ans) ans = d;
		 }
		ans /=2;  
	}
//	printf("Case #%d: %lf\n", ++cas, ans);
	cout << "Case #" << ++cas << ": " << ans << endl;
}
	return 0;
}
