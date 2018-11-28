#include <stdio.h>

using namespace std;

int main()
{
	int cases,i;
	int testers,s,p;
	int objective,limit,tmp,res;

	scanf("%d",&cases);

	for(i=0;i<cases;i++)
	{
		scanf("%d%d%d",&testers,&s,&p);
		objective = 3*p-2;
		limit = 3*p-4;

		if(p==1)
			limit=1;

		res = 0;

		for(;testers>0;testers--)
		{
			scanf("%d",&tmp);
			if(tmp>=objective)
				res++;
			else if(s>0 && tmp>=limit)
			{
				res++;
				s--;
			}
		}

		printf("Case #%d: %d\n",i+1,res);
	}

	return 0;
}
