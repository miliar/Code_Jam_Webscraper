#include<stdio.h>
#include<algorithm>

using namespace std;

int arr1[900] , arr2[900];

int main()
{
	freopen("a.in"  ,"r" , stdin);
	freopen("a.out" , "w" , stdout);
	int test , n , i , j , kase = 1;
	scanf("%d" , &test);
	while(test--)
	{
		scanf("%d" , &n);
		for(i = 0;i<n;i++)
			scanf("%d" , &arr1[i]);
		for(i = 0;i<n;i++)
			scanf("%d" , &arr2[i]);
		sort(arr1 , arr1+n);
		sort(arr2 , arr2+n);

		__int64 ret = 0;
		for(i = 0 , j = n-1;i<n;i++ , j--)
			ret += (arr1[i]*arr2[j]);
		printf("Case #%d: %I64d\n"  , kase++ , ret);
	}
	return 0;
}
