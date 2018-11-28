#include<iostream>
#include<stdio.h>
#include<string>
#include<string.h>
#include<vector>
#include<algorithm>

using namespace std;
const int inf = 100000000;
int min_(int a,int b)
{
	if(a<=b) return a;
	return b;
}
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("temp.txt","w",stdout);
	int t,cas=1;
	int ans,n;
	cin>>t;
	while(t--)
	{
	
		ans=inf;
		int sum=0;
		int num=0;
		cin>>n;
		
		while(n--)
		{
			int temp;
			cin>>temp;
			ans=min_(temp,ans);
			sum+=temp;
		//	cout<<sum<<endl;
			num^=temp;
		}	
		printf("Case #%d: ",cas++);
		if(num ==0 )
			printf("%d\n",sum-ans);
		else printf("NO\n");
	}
}
