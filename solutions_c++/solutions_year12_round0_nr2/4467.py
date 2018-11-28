/*
 * b.cpp
 *
 *  Created on: Apr 14, 2012
 *      Author: appemax
 */

#include<cstdio>
#include<cstring>
#include<algorithm>

using namespace std;

int M[200];

int main()
{
	int t, i, j, p, s, mark, c, r, n;

	freopen("B-large.in", "r", stdin);
	freopen("b-large.out", "w+", stdout);
	scanf("%d", &t);

	for(i=0; i<t; i++)
	{
		scanf("%d %d %d", &n, &s, &p);
		c = r = 0;
		for(j=0; j<n; j++)
		{
			scanf("%d", &mark);
			if(mark<p*3)
			{
				M[c++] = mark;
			}
			else r++;
		}

		sort(M, M+c);

		for(j=c-1; j>=0; j--)
		{
			if(3*p-M[j]<=2 && p>0) r++;
			else if(3*p-M[j]<=4 && s>0 && p>1) s--,r++;
			else break;
		}

		printf("Case #%d: %d\n", i+1, r);
	}


	return 0;
}

