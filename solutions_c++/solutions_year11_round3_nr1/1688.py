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
	  char orig[60][60];
	  bool isimpossible = false;

	  int rows;
	  scanf("%d",&rows);

	  int columns;
	  scanf("%d",&columns);

	  int i = 0;

	  for(i = 0 ; i < rows ; i++)
	  {
		  char dummy;
		  scanf("%c",&dummy);

		  int j = 0;
		  for(j = 0 ; j < columns ; j++)
		  {
			  scanf("%c",&orig[i][j]);
		  }
	  }

	  i = 0;

	  for(i = 0 ; i < rows ; i++)
	  {
		  int j = 0;
		  for(j = 0 ; j < columns ; j++)
		  {
			  if(orig[i][j] == '#')
			  {
				  if( ((i + 1) < rows )&& ((j + 1 )< columns) && orig[i][j+1] == '#' && orig[i+1][j+1] == '#' && orig[i+1][j] == '#')
				  {
					 orig[i][j] = '/';
				     orig[i][j+1] = '\\';
					 orig[i+1][j] = '\\';
					 orig[i+1][j+1] = '/';
				  }
				  else
				  {
					isimpossible = true;
					break;
				  }
			  }
		  }
		  if(isimpossible)
		  {
				break;
		  }
	  }

	  printf("Case #%d:\n",++caserunning);

	  if(isimpossible)
	  {
		   printf("Impossible\n");
	  }
	  else
	  {
		  i = 0;

		  for(i = 0 ; i < rows ; i++)
		  {			  
			  int j = 0;
			  for(j = 0 ; j < columns ; j++)
			  {
				  printf("%c",orig[i][j]);
			  }
			  printf("\n");
		  }

	  }

	
	
  }


  return 0;
}