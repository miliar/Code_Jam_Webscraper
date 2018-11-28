#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<vector>
#include<string>
using namespace std;


main()
{
	int T,N,CASE=0;
	int i;
	int res;
	char buf[1000];
	int count[10];
	int check[10];

	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);

	scanf("%d",&T);

	while(T--)
	{
		CASE++;

		scanf("%d",&N);

		for(i=0; i<10; i++)
			count[i] = 0;

		sprintf(buf,"%d",N);

		for(i=0; buf[i]; i++)
			count[buf[i]-'0']++;

		bool found;

		for(res=N+1; ; res++)
		{
			for(i=0; i<10; i++)
				check[i] = 0;

			sprintf(buf,"%d",res);

			for(i=0; buf[i]; i++)
				check[buf[i]-'0']++;

			found = true;

			for(i=1; i<10 && found; i++)
				if(check[i] != count[i])
					found = false;

			if(found)
				break;
		}

		printf("Case #%d: %d\n",CASE,res);

	}

}