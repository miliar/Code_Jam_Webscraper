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
	freopen("D-large.in","r",stdin);
	freopen("temp.txt","w",stdout);
	int t,cas=1;
	int ans,n;
	cin>>t;
	while(t--)
	{
		cin>>n;
		ans=0;
		for(int i=1;i<=n;i++)
		{
			int temp;
			cin>>temp;
			if(i!=temp)
				ans++;
		}
		printf("Case #%d: %.6lf\n",cas++,(double)ans);
	}
}
