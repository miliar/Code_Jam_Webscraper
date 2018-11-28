#include <iostream>
using namespace std;
int main()
{
	
	freopen("out.txt","w",stdout);
	__int64 l,p,c,i,j;
	__int64 t,sum,temp,d,s;
	scanf("%I64d",&t);
	__int64 ans;
	int ca=0;
	while(t--)
	{
		scanf("%I64d%I64d%I64d",&l,&p,&c);
		//cin>>l>>p>>c;
		sum=0;
		temp=l;
		while(temp*c<p)
		{
			sum++;
			temp*=c;
		}
		s=sum;
		ans=0;
		while(s>=1)
		{
			ans++;
			d=(s+1)/2;
			s=(s-d)>(d-1)?(s-d):(d-1);
		}
		printf("Case #%d: %I64d\n",++ca,ans);
	}
	return 0;
}




