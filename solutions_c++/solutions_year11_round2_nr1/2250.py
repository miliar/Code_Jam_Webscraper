/* 
 * File:   main.cpp
 * Author: Sreekanth
 *
 * Created on May 21, 2011
 */

#include <stdlib.h>
#include <stdio.h>

#define FOR(i,a,b) for(int i=(a);i<(b);++i)  
#define REP(i,n) FOR(i,0,n)  
#define FORE(i,a,b) for(int i=(a);i<=(b);++i)  
#define REPE(i,n) FORE(i,0,n)  


int main()
{
  freopen("I.in","r",stdin);
  freopen("O.op","w",stdout);

  int cases;
  scanf("%d",&cases);
  int caserunning=0;
  while (cases--)
  {	
	  int orig[120][120] = {0};
	  int opps[120][120] = {0};
	  double wp[120] = {0.0};
	  double cwp[120][120] = {0.0};
	  double owp[120] = {0.0};
	  double oowp[120] = {0.0};
	  double finres[120] = {0.0};
	  int oppscount[120] = {0};
	  int elements = 0;
	  scanf("%d",&elements);
	  
	  int teams = elements;

	  int i = 0;
	  

	  while(elements--)
	{
		int oppelem = teams;
		int j = 0;
		int k = 0;
		int wins = 0;
		int loses = 0;

		char dummy;
	    scanf("%c",&dummy);

		while(oppelem--)
		{
			char res;
			scanf("%c",&res);

			if(res == '.')
			{
				orig[i][j] = -1;
			}
			else if(res == '0')
			{
				orig[i][j] = 0;
				opps[i][k] = j;
				k += 1;
				loses += 1;
			}
			else if(res == '1')
			{
				orig[i][j] = 1;	
				opps[i][k] = j;
				k += 1;
				wins += 1;
			}
			j += 1;
			
		}

		wp[i] = (((double )(wins)) / ((double )(wins + loses)));
		oppscount[i] = k;
		i += 1;
		
	  }
	  i = 0;

	  for(i = 0; i < teams ; i++)
	  {		 
		  int j = 0;
		  for(j = 0; j < teams ; j++)
		  {
			   int cwin = 0;
			  int k = 0;
			  bool isminus = false;
			  for(k = 0; k < oppscount[i] ; k++)
			 {
				 if(opps[i][k] == j)
				 {
					isminus = true;
				 }
				 else if(orig[i][opps[i][k]] == 1)
				 {
					cwin += 1;
				 }
			 }
			  if(isminus)
			  {
				  cwp[i][j] = ((double)(cwin))/((double)(oppscount[i] - 1));
			  }
			  else
			  {
				cwp[i][j] = ((double)(cwin))/((double)(oppscount[i]));
			  }
			
		  }

	  }

	  for(i = 0; i < teams ; i++)
	  {
		  int j = 0;
		  double totwp = 0;
		 for(j = 0; j < oppscount[i] ; j++)
		 {
			totwp += cwp[opps[i][j]][i];
		 }

		 owp[i] = totwp / ((double)(oppscount[i]));

	  }

	  i = 0;

	  for(i = 0; i < teams ; i++)
	  {
		  int j = 0;
		  double totowp = 0;
		 for(j = 0; j < oppscount[i] ; j++)
		 {
			totowp += owp[opps[i][j]];
		 }

		 oowp[i] = totowp / ((double)(oppscount[i]));
	  }

	  i = 0;

	  for(i = 0; i < teams ; i++)
	  {
		  finres[i] = 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]	;	  
	  }

	printf("Case #%d:\n",++caserunning);	

	for(i = 0; i < teams ; i++)
	  {
		  printf("%.12f\n",finres[i]);	  
	  }
  }
  return 0;
}