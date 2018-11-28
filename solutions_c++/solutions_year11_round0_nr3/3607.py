#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
using namespace std;

main()
{
	int t, no=1;
	scanf("%d", &t);
	while(t--)
	{
		int n, result=0,i;
		scanf("%d", &n);
		vector<int> candies(n,0);

		for(i = 0; i < n; i++) 
		{
			scanf("%d", &candies[i]);
			result = result xor candies[i];
		}
	
		if(result == 0) 
		{
			sort(candies.begin(), candies.end());
			int sum = 0;
			for(i = 1; i < n;i++) {
				sum += candies[i];
			}
			printf("Case #%d: %d\n", no++, sum);
		}	
		else
		{
			printf("Case #%d: NO\n", no++);
		}
	}
}
