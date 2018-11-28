#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<string.h>
int buttonnumber[100];
char buttoncolour[100];
int next(char col,int b,int last)
{
int j,val;
for (val = 0,j=b;j<last;j++)
{
	if(buttoncolour[j]==col)
	{
		val = buttonnumber[j];
		break;
	}
}
return val;
}


void main()
{
int cases,index_cases,i, nbuttons,currentorange,currentblue,nextorange,nextblue;
int position,totaltime, thistime, distorange, distblue;
char nextcolour, colour[2];
//freopen("A-small-attempt0.in" , "rt" , stdin ) ;
//freopen("A-small-attempt0.out" , "wt" , stdout ) ;
freopen("A-large.in" , "rt" , stdin ) ;
freopen("A-large.out" , "wt" , stdout ) ;

cases = 0;
//read the number of test cases 
scanf("%d",&cases);
//printf("Cases = %d\n",cases);


//Loop through all the cases
for (index_cases=0 ; index_cases<cases; index_cases++)
{
	scanf("%d",&nbuttons);
//	printf("BUTTONS = %d\n",nbuttons);
	for (i=0;i<nbuttons;i++)
	{
		scanf("%s",&colour);

		scanf("%d",&position);
//		printf("Next button %c%d\n",colour[0],position);
		buttoncolour[i] = colour[0];
		buttonnumber[i] = position;
	}
	currentorange = 1;
	currentblue = 1;
	totaltime = 0;
	for (i=0;i<nbuttons;i++)
	{
		nextorange = next('O',i,nbuttons);
		nextblue = next('B',i,nbuttons);
		distorange = abs(nextorange - currentorange);
		distblue = abs(nextblue - currentblue);
		nextcolour = buttoncolour[i];
		if (nextcolour == 'B')
		{
			thistime = distblue + 1;
			totaltime = totaltime + thistime;
			currentblue = nextblue;
			if (nextorange )
			{
				if(nextorange > currentorange)
				{
					if(nextorange>currentorange+thistime)
						currentorange = currentorange+thistime;
					else 
						currentorange = nextorange;
				}
				else
				{
					if(nextorange<currentorange-thistime)
						currentorange = currentorange-thistime;
					else 
						currentorange = nextorange;
				}

			}
		}
		else if (nextcolour = 'O')
		{
			thistime = distorange + 1;
			totaltime = totaltime + thistime;
			currentorange = nextorange;
			if (nextblue )
			{
				if(nextblue > currentblue)
				{
					if(nextblue>currentblue+thistime)
						currentblue = currentblue+thistime;
					else 
						currentblue = nextblue;
				}
				else
				{
					if(nextblue<currentblue-thistime)
						currentblue = currentblue-thistime;
					else 
						currentblue = nextblue;
				}
			}
		}

	}
	printf("Case #%d: %d\n",index_cases+1,totaltime);

}
fclose(stdin) ;
fclose(stdout) ;

}