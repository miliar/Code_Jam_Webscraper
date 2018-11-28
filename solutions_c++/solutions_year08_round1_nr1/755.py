#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cmath>
#include<vector>

using namespace std;

int main()
{
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	int T;
	int n,nCase =1,i,temp;
	scanf("%d",&T);
	vector<int>x1;
	vector<int>y1;
	while(nCase <= T)
	{
		scanf("%d",&n);
		for(i=0;i<n;++i)
		{
			scanf("%d",&temp);
			x1.push_back(temp);
		}
		for(i=0;i<n;++i)
		{
			scanf("%d",&temp);
			y1.push_back(temp);
		}
		sort(x1.begin(),x1.end());
		sort(y1.begin(),y1.end());
		int res=0;
		for(i=0;i<n;++i)
		{
			res += x1[i] * y1[n-i-1];
		}
		printf("Case #%d: %d\n",nCase++,res);
		x1.clear();
		y1.clear();
	}
	return 0;
}