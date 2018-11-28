#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

int row,cul,n;
const int size=105,inf=1<<26;
int arr[size];

bool check(int now)
{
	int i;
	for(i=0;i<n;i++)
		if(arr[i]%now!=0&&now%arr[i]!=0)
			return false;
	return true;
}

int main()
{
	int t,e=1;

	freopen("C-small-attempt0.in","r",stdin);
	//freopen("C-small-attempt0.out","w",stdout);

	scanf("%d",&t);
	while(t--)
	{
		int i,j;
		int low,high;
		int ans=false;

		scanf("%d%d%d",&n,&low,&high);
		for(i=0;i<n;i++)
			scanf("%d",&arr[i]);
		for(i=low;i<=high;i++)
			if(check(i))
			{
				ans=true;
				break;
			}

		printf("Case #%d: ",e++);
		if(ans)
			printf("%d\n",i);
		else printf("NO\n");
	}
	return 0;
}