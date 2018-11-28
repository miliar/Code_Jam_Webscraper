#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <cmath>

using namespace std;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		int num[41]={0};
		bool u[41]={0};
		char s[41];
		int n,i,j;
		scanf("%d",&n);
		gets(s);
		for(i=0;i<n;i++) 
		{
			gets(s);
			for(j=0;s[j];j++);
			--j;
			while(j>=0 && s[j]=='0') --j;
			for(;u[j];j++);
			num[i]=j;
			u[j]=true;
		}
		int ans=0;
		for(i=0;i<n;i++)
			for(j=i+1;j<n;j++)
				if (num[i]>num[j])
				{
					++ans;
					swap(num[i],num[j]);
				}
				printf("Case #%d: %d\n",t,ans);
	}

	return 0;
}