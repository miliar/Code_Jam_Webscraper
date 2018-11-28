#include<iostream>
#include<cstdio>

using namespace std;

int arr[20];

void function(int t)
{
	int n;
        int i;
        int j;
	
	cin >> n;
	
	int a = 0;
	
	int sum = 0, min = 0x7fffffff;
	
	for (i = 0; i < n; i++) 
	{
		cin >> arr[i];
		sum += arr[i];

		if (arr[i] < min) min = arr[i];

		a ^= arr[i];
	}

	if (a) 
	{
		printf("Case #%d: NO\n", t);
		return;
	}

	printf("Case #%d: %d\n", t, sum-min);

	return;
}

int main()
{
	int t, i;
	
	cin >> t;

	for (i = 1; i <= t; i++)
	{
		function(i);
	}

	return 0;
}
