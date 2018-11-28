/*
*	Author:   
*   FileName: 
*   Create:    
*/
#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <string>
#include <math.h>
using namespace std;
#define MAX 20 
int used[MAX];
int num[MAX];
int result[MAX];
int N, n, max, SUM;
void process(int step, int index) {
    int i, sum=0, j;
	int sum1 = -1, sum2 = -1;
	if(step<=N/2)
	{
		for (i = 0; i < N; i++)
		{
			if(used[i])
			{
				sum += num[i];
				if(sum1==-1)
					sum1=num[i];
				else
					sum1 ^= num[i];
			}
			else
			{
				if(sum2==-1)
					sum2 = num[i];
				else
					sum2 ^= num[i];
			}
		}
	}
	else return ;
//	puts("");
	if(sum1 == sum2)
	{
		if(max < sum)
			max = sum;
		sum = SUM-sum;
		if(max < sum)
			max = sum;
	}
	for (i = index; i < N; i++)
	{
         if (!used[i]) 
		 {
               used[i] = 1;
			   result[step]=num[i];
               process(step + 1, i + 1);
               used[i] = 0;
        }
    }
}
int main()
{
	#ifndef ONLINE_JUDGE
 	   freopen("D:/C-small-attempt1.in", "r", stdin);
//	   freopen("D:/test.in", "r", stdin);
	   freopen("D:/test.out", "w", stdout);
	#endif
	int cas, i;
	cin >> cas;
	for(int ca=1; ca <= cas; ca++)
	{
		max=-1;
		SUM = 0;
		printf ("Case #%d: ", ca);
		cin >> n;
		N = n;
		int or;
		for(i = 0; i < n; i++)
		{
			
			cin >> num[i];
			SUM += num[i];
			if(!i)
				or=num[i];
			else
				or ^= num[i];
		}
// 		if(or)
// 		{
// 			puts("NO");
// 			continue;
// 		}
		memset(used, 0, sizeof(used));
		process(0, 0);
		if(max==-1)
			puts("NO");
		else
			printf("%d\n", max);
	}
	return 0;
}