#include<cstdio>
#include<cstring>
#include<set>
using namespace std;

int lenx(int x)
{
	int c = 0;
	while(x > 0)
	{
		c++;
		x /= 10;
	}
	return c;
}

int countN(int x,int a,int b)
{
	set<int> s;
	int ret=0, l=lenx(x), rec=x, mul=1;
	
	for(int i=1; i<l; i++) { mul *=  10; }
	for(int i=1; i<l; i++)
	{
		rec = (rec%10)*mul + (rec/10);
		if(lenx(rec)==l && rec>x && rec>=a && rec<=b && s.find(rec)==s.end())
		{
			s.insert(rec);
			ret++;
		}
	}
	s.clear();
	return ret;
}

int main()
{
	int t,a,b,ans;
	scanf("%d",&t);
	for(int cases=1; cases<=t; cases++)
	{
		scanf("%d%d",&a,&b);
		ans = 0;
		for(int i=a; i<=b; i++)
			ans += countN(i,a,b);
		printf("Case #%d: %d\n",cases,ans);
	}
	return 0;
}
