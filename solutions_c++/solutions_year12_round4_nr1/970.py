#include<stdio.h>
#include<string.h>
#include<iostream>
using namespace std;
#define LIM 10009
int arr[LIM], d[LIM], l[LIM];
int main()
{
	int t, n, D;
	scanf("%d",&t);
	for(int tc=1; tc<=t; tc++)
	{
		scanf("%d",&n);
		for(int i=0; i<n; i++)
		scanf("%d%d",&d[i],&l[i]);
		scanf("%d",&D);
	//	printf("asdasd\n");
		memset(arr, -1, sizeof(arr));
		int swing = min(d[0], l[0]);
		int flag=0;
		arr[0]=swing;
		for(int i=0; i<n&&arr[i]!=-1; i++)
		{
			swing = arr[i];
	//		printf("ss %d\n",swing);
			if(arr[i]+d[i]>=D)
			{
				flag = 1;
				break;
			}
			for(int j=i+1; j<n; j++)
			if(d[j] - d[i] <= arr[i])
			arr[j] = max( arr[j], min(d[j]-d[i], l[j]));
		}

		printf("Case #%d: %s\n", tc, flag==1?"YES":"NO");
	}
	return 0;
}
