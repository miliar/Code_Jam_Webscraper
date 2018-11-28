// round1_3.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <stdio.h>
#include <algorithm>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	freopen("c:\\B-small-attempt0.in", "r", stdin);
	freopen("c:\\B-small-attempt0.out", "w", stdout);

	int t = 0;
	int c, n, ca = 0;
	scanf("%d", &t);
	while(t--)
	{
		c = 0;
		scanf("%d", &n);
		int k = n;
		int a[10], l = 0;
		while(k)
		{
			a[l++] = k % 10;
			k /= 10;
		}

		sort(a, a+l);

		int mmin = 1000000000;
		do{
			int m = 0;
			for(int i = 0;i < l; i++)
			{
				m *= 10;
				m += a[i];
			}
			//printf("%d\n", m);
			if(m > n && m - n < mmin)
			{
				mmin = m - n;
				c = m;
			}
		}while(next_permutation(a, a+l));

		if(c == 0)
		{
			mmin = 1000000000;
			a[l] = 0;
			l++;
			do{
				int m = 0;
				for(int i = 0;i < l; i++)
				{
					m *= 10;
					m += a[i];
				}//printf("%d\n", m);
				if(m > n && m - n < mmin)
				{
					mmin = m - n;
					c = m;
				}
			}while(next_permutation(a, a+l));
		}
		
		printf("Case #%d: %d\n", ++ca, c);
	}

	return 0;
}

