#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	int T;
	scanf("%d",&T);
	for (int i=0;i<T;i++)
	{
		int n;
		scanf("%d",&n);
		vector<int> v1(n,0);
		vector<int> v2(n,0);
		for (int j=0;j<n;j++)
		{
			scanf("%d",&(v1[j]));
		}

		for (int j=0;j<n;j++)
		{
			scanf("%d",&(v2[j]));
		}
		sort(v1.begin(),v1.end());
		sort(v2.begin(),v2.end());
		reverse(v2.begin(),v2.end());
		long prod = 0;
		for (int j=0;j<n;j++)
		{
			prod += v1[j]*v2[j];
		}

		printf("Case #%d: %ld\n",i+1,prod);
	}
}