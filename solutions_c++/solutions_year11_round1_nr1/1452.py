/* 
 * File:   main.cpp
 * Author: Sreekanth
 *
 * Created on May 21, 2011
 */

#include <stdlib.h>
#include <stdio.h>

/*
 * 
 */

int gcd(int a,int b)
{
	int c;
	while(1)
	{
		c = a%b;
		if(c==0)
		  return b;
		a = b;
		b = c;
	}
}

int main()
{
  freopen("I.in","r",stdin);
  freopen("O.op","w",stdout);

  int cases;
  scanf("%d",&cases);
  int caserunning=0;
  while (cases--)
  {
	  int gamestoday = 0;
	  int todayp = 0;
	  int totalp = 0;
	  bool ispos = false;

	  scanf("%d",&gamestoday);
	  scanf("%d",&todayp);
	  scanf("%d",&totalp);

	
	  if((totalp == 100 && (totalp > todayp)) || (totalp == 0 && (totalp < todayp)) )
	  {

	  }
	  else if((todayp == 0) ||((gamestoday >= (100 / gcd(100,todayp)))))
	  {
		ispos = true;
	  }
	  if(ispos == true)
	  {
		printf("Case #%d: Possible\n",++caserunning);
	  }
	  else
	  {
		printf("Case #%d: Broken\n",++caserunning);
	  }
	
  }


  return 0;
}

