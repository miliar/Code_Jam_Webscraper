#include <iostream>
#include <string>
#include <set>
#include <algorithm>
#include <stdio.h>
#include <map>
using namespace std;int num;int sum, N, T;int arr[202];int main(){		cin>>num;

	for(int k=1;k<=num;++k)	{		cin >> N;		sum = 0;		for(int i = 1; i <= N; i++)		{			cin >> arr[i];			sum += arr[i];		}		int left = N;		T = sum;		for(int i = 1; i <= N; i++)		{			if(sum * 2 / N < arr[i])			{								left--;										T -= arr[i];				arr[i] = -1;			}		}		printf("Case #%d: ",k);		for(int i = 1; i <= N; i++)		{			if(arr[i]==-1)				printf("0.000000 ");			else				printf("%.6lf ",100 * (1.0 * (sum + T) / left - arr[i]) / (1.0 * sum));		}		printf("\n");	}	return 0;}