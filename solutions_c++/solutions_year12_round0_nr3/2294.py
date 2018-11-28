/*
 * temp.cpp
 *
 *  Created on: 14.04.2012
 *      Author: kalhit
 */

/*
 * main.cpp
 *
 *  Created on: 14.04.2012
 *      Author: kalhit
 */
#include <stdio.h>
#include <stdlib.h>
namespace
{
int a[2000010];
int tmp[20];
static inline bool check (int* a, int* b, int len)
{
	--a; --b;
	if(!*b)
		return false;
	for(int i = len; i; --i)
	{
		if(*a != *b)
		{
			return *b < *a;
		}
		--a; --b;
	}
	return false;
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int T = 0;
	scanf("%d", &T);
	for(int j = 0,l,r; j < T;)
	{
		if(j) printf("\n");
		scanf("%d%d", &l, &r);
		for(int i = l; i <=r;++i)
		{
			int k = i;
			int l = 0;
			do{
				tmp[l] = k%10;
				k/=10;
				++l;
			}while(k);
			for(int q = 0; q < l; ++q)
				tmp[q+l] = tmp[q];
			for(int q = 1; q < l; ++q)
				if(check(&tmp[k+l], &tmp[q+l], l))
					k = q;
			int p= 0;
			for(int q = k+l-1;q >=k; --q)
				p = p*10 + tmp[q];
			++a[p];
		}
		long long sum = 0;
		for(int i = 0; i < r; ++i)
			sum +=a[i] * (a[i]-1)/2;
		printf("Case #%d: %lld", ++j, sum);
	}
	return 0;
}
}
