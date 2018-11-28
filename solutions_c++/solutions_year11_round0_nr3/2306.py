#include <cstdio>
#include <vector>
#include <numeric>
#include <functional>
#include <algorithm>
using namespace std;
int main()
{
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		int n;
		scanf("%d",&n);
		vector<int> c(n);
		for(int j=0;j<n;j++)
			scanf("%d",&c[j]);
		printf("Case #%d: ",i);
		if(accumulate(c.begin(),c.end(),0,bit_xor<int>())!=0)
		{
			puts("NO");
			continue;
		}
		printf("%d\n",accumulate(c.begin(),c.end(),0,plus<int>())-*min_element(c.begin(),c.end()));
	}
	return 0;
}
