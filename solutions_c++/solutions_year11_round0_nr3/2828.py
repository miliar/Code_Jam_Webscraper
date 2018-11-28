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
	int candies = 0;
	scanf("%d",&candies);
	int min = 2147483645;
	int total = 0;
	int res = 0;

	while(candies--)
	{
		int candieid;
		scanf("%d",&candieid);
		res ^= candieid;
		if(candieid < min)
		{
			min = candieid;
		}
		total += candieid;
	}

	if(res == 0)
	{    
		printf("Case #%d: %d\n",++caserunning,(total - min));
	}
	else
	{
		printf("Case #%d: NO\n",++caserunning);
	}
  }


  return 0;
}

