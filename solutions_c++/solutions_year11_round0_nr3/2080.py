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
	freopen("C-large-1.in","r",stdin);
	freopen("c-large.out","w",stdout);
	int t,cas=1,temp=0,flag=0;
	scanf("%d",&t);
	while(t--)
	{
		ans=temp=flag=0;
		scanf("%d",&n);
		for(int i=0;i<n;i++)
		{
			scanf("%d",&a[i]);
			temp^=a[i];
			ans+=a[i];
		}
		if(temp)flag++;
		if(!flag)
		{
			sort(a,a+n);
			ans-=a[0];
		}
		printf("Case #%d: ",cas++);
		if(!flag)
			printf("%d\n",ans);
		else
			printf("NO\n");
	}
	return 0;
}
