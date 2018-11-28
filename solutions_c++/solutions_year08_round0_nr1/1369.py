#include <stdio.h>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <math.h>
#include <algorithm>
using namespace std;


main()
{
	int i,j,k;
	char in[1000];
	char all[105][105];
	int flag[105],count,res;

	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	int CASE=0,n,s,q;

	n = atoi(gets(in));

	while(n--)
	{
		s = atoi(gets(in));

		for(i=0; i<s; i++)
			strcpy(all[i],gets(in));
		
		q = atoi(gets(in));

		for(i=0; i<s; i++)
			flag[i] = 0;

		count = 0;
		res = 0;

		for(i=0; i<q; i++)
		{
			gets(in);
			
			for(j=0; strcmp(all[j],in); j++);

			if(flag[j] == 0)
			{
				flag[j] = 1;
				count++;
			}

			if(count == s)
			{
				res++;

				for(k=0; k<s; k++)
					flag[k] = 0;

				flag[j] = 1;
				count = 1;
			}
		}

		CASE++;
		printf("Case #%d: ",CASE);
		printf("%d\n",res);

	}

}

