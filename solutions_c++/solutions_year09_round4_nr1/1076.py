//compiled in vc
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;


long long mat[42];

char buf[1024];
int n;
int bubbleSort(long long a[])
{
	int i ,j;
	int cnt = 0;
	for(i=0;i<n;i++)
	{
		for(j=1;j<n-i;j++)
		{
			if( a[j-1] > a[j] )
			{
				swap(a[j-1] , a[j]);
				cnt++;
			}
		}
	}

	return cnt;
}

long long m2[42];

int main()
{
	int cases, Case = 0;
	scanf("%d" , &cases);

	int ans = 0;
	
	int i;
	while(cases--)
	{
		scanf("%d" , &n);

		for(i=0;i<n;i++)
		{
			scanf("%s" , buf);
			mat[i] = 0;
			int j=0;
			for( j = strlen(buf)-1; j>-1;j-- )
			{
				
				if( buf[j] == '1' )
				 break;
			}
			mat[i] = j;
		}

		/*
		for each row i (0 to n) 
		if the row is not valid 
		find the first valid row (say row k, k > i)
        move this valid row k up to i (surely by swapping)
		*/
		ans = 0;
		for(i=0;i<n;i++)
		{
			if( i < mat[i] )
			{
				int j;
				for( j=i+1;j<n;j++)
				{
					if( i >=mat[j] ) break;
				}

				for(int k=j;k>i;k--)
				{
					swap(mat[k],mat[k-1]);
					ans++;
				}
			}
		}





		printf("Case #%d: %d\n" , ++Case , ans);
	}




	return 0;
}