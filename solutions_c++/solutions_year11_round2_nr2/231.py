#include <iostream>
using namespace std;
#define M 1100000
int n;
double D;
int P[M];
void read_data()
{
	int m;
	cin >> m >> D;
	int i,p,v;
	n = 0;
	for (i=1;i<=m;i++)
	{
		cin >> p >> v;
		while (v--) P[++n] = p;
	}

	//for (i=1;i<=n;i++) printf("%d ",P[i]); puts("");
}

bool ok(double s)
{
	double nowplace,temp;
	int i;
	nowplace = P[1] - s + D;
	for (i=2;i<=n;i++)
	{
		if (nowplace < P[i])
		{
			nowplace = max(P[i] - s,nowplace) + D;
		}
		else
		{
			if (nowplace - P[i] > s) return false;
			nowplace += D;
		}
	}
	return true;
}

double work_ans()
{
	double up = 1e15,dn = 0,mid;
	while (up - dn > 1e-3)
	{
		mid = (up + dn) / 2;
		if (ok(mid)) up = mid; else dn = mid;
	}
	return (up + dn) / 2;
}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	double ans;
	int t,i;
	cin >> t;
	for (i=1;i<=t;i++)
	{
		fprintf(stderr,"%d\n",i);
		printf("Case #%d: ",i);
		read_data();
		ans = work_ans();
		printf("%.2lf\n",ans);
	}
	return 0;
}