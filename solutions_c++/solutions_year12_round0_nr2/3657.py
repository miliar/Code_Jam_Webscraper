#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <cmath>

using namespace std;

int main()
{
	int t;
	int n , s , p;
	
	scanf("%d" , &t);

	for (int i = 0; i < t; ++i)
	{
		scanf("%d %d %d" , &n , &s , &p);

		int actualS = s;
		int count = 0;
		
		for (int j = 0; j < n; ++j)
		{
			int value;
			
			scanf("%d" , &value);
			
			if (value > (p - 1) * 3)
			{
				count++;
			}
			else if (actualS > 0 && value > max((p * 3) - 5 , 0))
			{
				count++;
				actualS--;
			}
		}
		
			
		printf("Case #%d: %d\n" , i + 1 , count);  
	}
	
	return 0;
}