#include<iostream>
#include<algorithm>
__int64 mi(__int64 a,int ti)
{
	if(ti==1)return a;
	if(ti==0)return 1;
	if(ti%2)return a*mi(a,ti/2)*mi(a,ti/2);
	return mi(a,ti/2)*mi(a,ti/2);
}
int main()
{
	int T,cs,i,j,n,ans;
	__int64 a,b,c,tt,two;
	two=2;
	freopen("B-Large.in","r",stdin);
	freopen("B-Large.out","w",stdout);
	scanf("%d",&T);
	for(cs=1;cs<=T;cs++)
	{
		scanf("%I64d%I64d%I64d",&a,&b,&c);
		for(i=0;i<100;i++)
		{
			tt=mi(two,i);
			if(a*mi(c,tt)>=b)break;
		}
		printf("Case #%d: %d\n",cs,i);
	}
	return 0;
}