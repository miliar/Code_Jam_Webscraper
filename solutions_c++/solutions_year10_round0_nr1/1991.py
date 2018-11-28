#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<vector>
#include<string>
using namespace std;


main()
{
	int T,N,K,CASE=0;
	int i,j,k;

//	freopen("A-small-attempt2.in","r",stdin);
//	freopen("A-small-attempt2.out","w",stdout);

	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);


	scanf("%d",&T);

	while(T--)
	{
		CASE++;

		scanf("%d %d",&N,&K);

		i = (1<<N) - 1;

		if((K & i) == i)
			printf("Case #%d: ON\n",CASE);
		else
			printf("Case #%d: OFF\n",CASE);

	}




}