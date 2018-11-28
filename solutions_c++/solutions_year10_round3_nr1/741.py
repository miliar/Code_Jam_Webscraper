#include<stdio.h>
#include<stdlib.h>
#include<string>
#include<set>
#include<stack>
#include<iostream>
#include<math.h>
#include<map>
#include<memory.h>
#include<algorithm>
using namespace std;
struct acm
{
	int x,y;
}a[1001];
int cmp(acm lwl,acm py)
{
	return lwl.x<py.x;
}

int main()
{
    freopen("A-large.in","r",stdin);
	freopen("A.txt","w",stdout);
	int t,i,j,n;
	scanf("%d",&t);
	int cas=1;
	int ans;
	while(t--)
	{
		ans=0;
		scanf("%d",&n);
		for(i=0;i<n;i++)
		scanf("%d %d",&a[i].x,&a[i].y);
		sort(a,a+n,cmp);
		for(i=0;i<n;i++)
		{
			for(j=i+1;j<n;j++)
			if(a[i].y>a[j].y)
			    ans++;
		}
		printf("Case #%d: %d\n",cas++,ans);
	}
	return 0;
}
