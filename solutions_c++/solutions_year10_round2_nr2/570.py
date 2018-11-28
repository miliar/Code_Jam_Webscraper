#include <iostream>

using namespace std;
struct str
{
	long x,v;
};
str a[100];
int g[100];
bool cmp(str a,str b)
{
	return a.x>b.x;
}

int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int c,ci,n,k,b,t,i,d,ans = 0;
	cin >> c;
	for(ci=1;ci<=c;ci++)
	{
		cin >> n >> k >> b >> t;
		for(i=0;i<n;i++)
			cin >> a[i].x;
		for(i=0;i<n;i++)
			cin >> a[i].v;
		sort(a,a+n,cmp);
		d = 0;ans = 0;
		for(i=0;i<n;i++)
		{
			if(i == 0) g[i] = 0;
			else g[i] = g[i-1];
			if(a[i].v*t >= b-a[i].x)
			{
				ans += g[i];
				d++;
			}
			else
				g[i]++;
			if(d == k)
			{
				cout << "Case #" << ci << ": " << ans << endl;
				break;
			}
		}
		if(d < k)	cout << "Case #" << ci << ": IMPOSSIBLE" << endl;
	}
	return 0;
}
