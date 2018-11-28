#include<cstdio>
#include<utility>
#include<vector>
#include<algorithm>
#define s(n) scanf("%d",&n)
using namespace std;
pair<int,int> tmp1;
vector< pair<int,int> > da;
int digits(int x)
{
	if (x==0)
		return 1;
	int i = 0;
	while(x > 0)
	{
		x = x/10;
		i++;
	}
	return i;
}
int main()
{
	int a,b,t,ans,i,j,d,ex[10],x,tmp,ca=0;
	ex[0] = 1;
	for (i=1;i<=6;i++)
		ex[i] = ex[i-1]*10;
	s(t);
	while(t--)
	{
		ca++;
		s(a);
		s(b);
		d = digits(a);
		ans = 0;
		da.clear();
		for (i=a;i<=b;i++)
		{
			for (j=1;j<d;j++)
			{
				x = i;
				tmp = x%ex[j];
				x = x/ex[j];
				tmp = tmp*ex[d-j] + x;
				if (tmp > i && digits(tmp)==d && tmp <= b)
				{
					tmp1.first = i;
					tmp1.second = tmp;
					da.push_back(tmp1);
				}
			}
		}
		ans = 0;
		sort(da.begin(),da.end());
		if (!da.empty())
		{
			ans = 1;
			for (i=1;i<da.size();i++)
				if (da[i].first!=da[i-1].first || da[i].second!=da[i-1].second)
					ans++;
		}
			
		printf("Case #%d: %d\n",ca,ans);
	}
	return 0;
}
