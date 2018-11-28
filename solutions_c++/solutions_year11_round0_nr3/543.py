#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>

using namespace std;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		int n,v[1002]={0},res=0,sum=0,mn=100000000;
		scanf("%d",&n);
		for(int i=0;i<n;i++)
		{
			scanf("%d",&v[i]);
			res^=v[i];
			sum+=v[i];
			if (v[i]<mn) mn=v[i];
		}
		printf("Case #%d: ",t);
		if (res!=0) printf("NO\n");
		else printf("%d\n",sum-mn);
	}
	return 0;
}