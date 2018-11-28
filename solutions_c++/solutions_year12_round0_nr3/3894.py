#include<cstdio>
#include<string>
#include<stdlib.h>
using namespace std;
long long int fun(int i,int a,int b)
{
	int num=i;
	long long int c=0;
	string s="";
	while(i>0)
	{
		s+=(i%10+'0');
		i/=10;
	}
	string x(s.rbegin(),s.rend());
	s=x;
	while(1)
	{
		s+=s[0];
		s.erase(s.begin());
		if(atoi(s.c_str())==num)
			break;
		if(s[0]!='0')
			if(atoi(s.c_str())>=a && atoi(s.c_str())<=b)
				c++;
	}
	return c;
}

int main()
{
	int t,i,j,a,b;
	long long int ans;
	scanf("%d",&t);
	for(j=1;j<=t;j++)
	{
		printf("Case #%d: ",j);
		scanf("%d%d",&a,&b);
		ans=0;
		for(i=a;i<=b;i++)
			ans+=fun(i,a,b);
		printf("%lld\n",ans/2);
	}
	return 0;
}
