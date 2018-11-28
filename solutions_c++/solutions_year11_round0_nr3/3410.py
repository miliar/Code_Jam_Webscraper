#include<stdio.h>
#include<stdlib.h>
#include<memory.h>
#include<iostream>
using namespace std;
int main()
{
	freopen("C-large.in","r",stdin); 
	freopen("C.txt","w",stdout);
	int cas,n;
	int a[1001];
	scanf("%d",&cas);
	for(int ca=1;ca<=cas;ca++)
	{
		scanf("%d",&n);
		int ans=0;
		int sum=0;
		for(int i=0;i<n;i++)
		{
			scanf("%d",a+i);
			ans^=a[i];
			sum+=a[i];
		}
		if(ans!=0)
		{
			cout<<"Case #"<<ca<<": NO"<<endl;
			continue;
		}
		int minn=987654321;
		for(int i=0;i<n;i++)
			if(minn>a[i]) minn=a[i];
		cout<<"Case #"<<ca<<": "<<sum-minn<<endl;	
	}
	return 0;
}
