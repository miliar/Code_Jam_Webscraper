#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
	int T,t;
	cin>>T;
	for(t=1;t<=T;t++)
	{
		int N,i;
		cin>>N;
		vector<__int64> v1,v2;
		for(i=0;i<N;i++)
		{
			__int64 a;
			scanf("%I64d",&a);
			v1.push_back(a);
		}
		for(i=0;i<N;i++)
		{
			__int64 a;
			scanf("%I64d",&a);
			v2.push_back(a);
		}
		__int64 ans=0;
		sort(v1.begin(),v1.end());
		sort(v2.begin(),v2.end());
		for(i=0;i<N;i++)
			ans=ans+v1[i]*v2[N-i-1];
		printf("Case #%d: %I64d\n",t,ans);
	}
	return 0;
}