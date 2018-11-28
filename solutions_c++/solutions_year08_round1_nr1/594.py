#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	cin>>t;
	int cnt;
	for(cnt=1;cnt<=t;cnt++)
	{
		int n;
		scanf("%d",&n);
		int i;
		vector<__int64> vi1;
		vector<__int64> vi2;
		for(i=0;i<n;i++)
		{
			__int64 x;
			scanf("%I64d",&x);
			vi1.push_back(x);
		}
		for(i=0;i<n;i++)
		{
			__int64 x;
			scanf("%I64d",&x);
			vi2.push_back(x);
		}
		sort(vi1.begin(),vi1.end());
		sort(vi2.begin(),vi2.end(),greater<__int64>());
		__int64 sum=0;
		for(i=0;i<n;i++)
		{
			sum+=vi1[i]*vi2[i];
		}
		printf("Case #%d: %I64d\n",cnt,sum);
	}
	return 0;
}