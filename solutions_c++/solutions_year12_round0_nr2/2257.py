/*
 * main.cpp
 *
 *  Created on: 14.04.2012
 *      Author: kalhit
 */
#include <stdio.h>
#include <stdlib.h>
int a[10];
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T = 0;
	scanf("%d", &T);
	for(int j = 0; j < T;)
	{
		if(j)
			printf("\n");
		int n,s,p;
		scanf("%d%d%d", &n, &s, &p);
//		int ost = s;
		int used = 0;
		int sum = 0;
		for(int i = 0; i < n; ++i)
		{
			int k;
			scanf("%d", &k);
			a[2] =  k/3;
			k-=a[2];
			a[1] =k/2;
			a[0] = k-a[1];
			if(a[0] >= p ||(used < s && a[1]>0 && a[0] <10 && a[0] == a[1] && a[0]+1 == p))
			{
				++sum;
				if(a[0]<p)
					++used;
			}
//			if((a[1]>0 && a[0] <10 && a[0] == a[1])||
//					(a[2]>0 && a[1] <10 && a[1] == a[2]))
//			{
//				--ost;
//			}
		}
		printf("Case #%d: %d", ++j, sum);
	}
	return 0;
}
