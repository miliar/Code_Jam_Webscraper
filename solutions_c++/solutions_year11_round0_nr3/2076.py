//============================================================================
// Name        : GCJ.cpp
// Author      : yb
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <cmath>
#include <cstdio>
#include <algorithm>
using namespace std;
int a[1005];
int ans,n;
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("3.out","w",stdout);
	int t,cas=1,temp=0,flag=0;
	scanf("%d",&t);
	while(t--)
	{
		ans=0;
		temp=0;
		flag=0;
		scanf("%d",&n);
		for(int i=0;i<n;i++)
		{
			scanf("%d",&a[i]);
			temp^=a[i];
		}
		//printf("%d\n",temp);
		if(temp)flag++;
		sort(a,a+n);
		for(int i=1;i<n;i++)
			ans+=a[i];
		printf("Case #%d: ",cas++);
		if(!flag)
			printf("%d\n",ans);
		else
			printf("NO\n");
	}
	return 0;
}
