#include<iostream>
#include<cstdio>
#include<cmath>
#include<math.h>
using namespace std;
int countdig(int a)
{
	int cnt=0;
	while(a>0)
	{
		int r=a%10;
		a=a/10;
		cnt++;
	}
	return cnt;
}
int main()
{
	int cases,k=1;
	scanf("%d",&cases);
	while(cases--)
	{
		int a,b;
		int res=0;
		scanf("%d %d",&a,&b);
		int ndigits=countdig(a);
		//cout<<ndigits<<endl;
		for(int i=a;i<=b;i++)
		{
			for(int j=1;j<ndigits;j++)
			{
				int num=i;
				int rem=num%(int)(pow((float)10,(float)ndigits-j));
				//cout<<"rem="<<rem<<endl;
				int quo=num/(int)(pow((float)10,(float)ndigits-j));
				//cout<<"quo="<<quo<<endl;
				int ans=rem*(int)(pow((float)10,(float)j))+quo;
				
				if(ans>=a && ans<=b && ans!=i) res++;
			}
		}
		if(res%2==0) res=res/2;
		else res=(res/2)+1;
		printf("Case #%d: %d\n",k,res);
		k++;
	}
	return 0;
}
		
				
			