#include<iostream>
#include<algorithm>
#include<fstream>
#include<stdio.h>
using namespace std;
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int T,n,i,test,sum,ca;
	int Tu[1200];
	scanf("%d",&T);
	for(ca=1;ca<=T;++ca)
	{
		scanf("%d",&n);
		sum=0;
		for(i=0;i<n;++i)
		{
			scanf("%d",&Tu[i]);
			sum+=Tu[i];
		}
		test=0;
		for(i=0;i<n;++i)
		{
			
			test=(test|Tu[i])&(~(Tu[i]&test));
			//cout<<test<<endl;
		}
		if(test!=0)printf("Case #%d: NO\n",ca);
		else 
		{
			sort(Tu,Tu+n);
			printf("Case #%d: %d\n",ca,sum-Tu[0]);
		}
	}
	return 0;
}
