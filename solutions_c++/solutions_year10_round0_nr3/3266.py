#include <iostream>

using namespace std;

int r,k,n,g[2000],t,nt;
int less,t1,tp;
long long sum;


int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin >> t;
for (nt=1; nt<=t; nt++)
{
	cin >> r >> k >> n;
	for (int i=0; i<n; i++)
		cin >> g[i];
	sum=0;
	t1=0;
	for (int i=0; i<r; i++)
	{
		less=k;
		tp=0;
		while ((g[t1]<=less)&&(tp<n)) { less-=g[t1]; sum+=g[t1]; t1++; t1%=n; tp++; }
	}
	printf("Case #%d: %lld\n", nt, sum);
}
	return 0;
}