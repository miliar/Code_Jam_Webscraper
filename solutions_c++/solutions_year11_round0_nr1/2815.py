/* 
 * File:   main.cpp
 * Author: Sreekanth
 *
 * Created on May 7, 2011
 */

#include <stdlib.h>
#include <stdio.h>

/*
 * 
 */
int main()
{
  freopen("I.in","r",stdin);
  freopen("O.op","w",stdout);

  int cases;
  scanf("%d",&cases);
  int caserunning=0;
  while (cases--)
  {
    int tottime = 0;
    int timeforother = 0;
    char prevsail;
	int orpos = 1;
	int blpos = 1;
	int moves = 0;
	scanf("%d",&moves);

	while(moves--)
	{
		char sail;
		char space;
		int topos = 0;
		scanf("%c",&space);
		scanf("%c",&sail);
		scanf("%d",&topos);
		unsigned int totravel;
		int timenow = 0;
		if(sail == 'O' || sail == 'o')
		{
			sail = 'O';
			if(topos > orpos)
			{
				totravel = topos -  orpos ;
			}
			else
			{
				totravel = orpos - topos;
			}
			if(sail == prevsail)
			{
				timenow = totravel + 1;
			}
			else
			{
				if(totravel > timeforother)
				{
					timenow = totravel - timeforother + 1;
				}
				else
				{
					timenow = 1;
				}
			}
			orpos = topos;
				
			
		}
		if(sail == 'B' || sail == 'b')
		{
			sail = 'B';

			if(topos > blpos)
			{
				totravel = topos -  blpos ;
			}
			else
			{
				totravel = blpos - topos;
			}

			if(sail == prevsail)
			{
				timenow = totravel + 1;
			}
			else
			{
				if(totravel > timeforother)
				{
					timenow = totravel - timeforother + 1;
				}
				else
				{
					timenow = 1;
				}
			}
			blpos = topos;
			
			
		}
		tottime += timenow;
		
		if(sail == prevsail)
		{
			timeforother += timenow;

		}
		else
		{
			timeforother = timenow;
		}
		prevsail = sail;
	}
    
    printf("Case #%d: %d\n",++caserunning,tottime);
  }


  return 0;
}

