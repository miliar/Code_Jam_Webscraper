#include <stdio.h>

struct robotinfo
{
	int t;
	int pl;
};
robotinfo orange,blue,empty;

int t,tcase,n;
int re;

int myabs(int x)
{
	if(x<0) return -1*x;
	else return x;
}

int main()
{
	int i,num=0;
	char rb[5];

	FILE *out;
	out=stdout;//fopen("A.out","w");

	empty.t=0;
	empty.pl=1;
	scanf("%d",&tcase);
	for(t=0;t<tcase;t++)
	{
		re=0;
		orange=empty;
		blue=empty;

		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%s",rb);
			scanf("%d",&num);

			if(rb[0]=='O')
			{
				if(orange.pl!=num)
				{
					if(re-orange.t<myabs(num-orange.pl))
						re+=myabs(num-orange.pl)+1-(re-orange.t);
					else
						re++;
				}
				else
					re++;
				orange.t=re;
				orange.pl=num;
			}
			if(rb[0]=='B')
			{
				if(blue.pl!=num)
				{
					if(re-blue.t<myabs(num-blue.pl))
						re+=myabs(num-blue.pl)+1-(re-blue.t);
					else
						re++;
				}
				else
					re++;
				blue.t=re;
				blue.pl=num;
			}
		}
		fprintf(out,"Case #%d: %d\n",t+1,re);
	}
	return 0;
}