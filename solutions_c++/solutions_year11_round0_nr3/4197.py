#include<iostream>
#include<vector>
#include<algorithm>
#include<stdio.h>
using namespace std;
int main()
{
	int N,T;
	vector<int> v;
	freopen("C-large.in","rt",stdin);
        freopen("output.out","wt",stdout);
	scanf("%d",&T);
	for(int i=1;i<=T;i++)
	{
		int j,sean_sum=0,pat_sum=0,sum=0,xr=0,itr_status,part;
		scanf("%d",&N);
		v.resize(N);
		for(j=0;j<N;j++)
		scanf("%d",&v[j]);
		sort(v.begin(),v.end());
//		for(j=0;j<N;j++)
//		printf("%d",v[j]);
		for(part=1;part<N;part++)
		{
			for(int k=0;k<part;k++)
			pat_sum+=v[k];
			for(int k=part;k<N;k++)
			{
			sean_sum+=v[k];
			xr=xr^v[k];
			}
			if(xr==pat_sum)
			sum=sean_sum;
		}
		if(sum>0)
		printf("Case #%d: %d\n",i,sum);
		else
		printf("Case #%d: NO\n",i);
	}
	return 0;
}

