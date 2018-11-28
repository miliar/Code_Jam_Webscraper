#include <stdio.h>
#include <math.h>
#include <string>
#include <vector>
using namespace std;

int numcases;
int numsearchengines;
char filename[50];
char searchengines[1002][102];
char searchquery[1002][102];
FILE *testfile;
int numqueries;

double costs[1001][1001];

int main(int argc,char*argv[])
{

 
  strcpy(filename,argv[1]);
  //printf("%s\n",filename);

  testfile=fopen(filename,"r");
  
  fscanf(testfile,"%d",&numcases);  
 

  for(int i=1;i<=numcases;i++)
    {
      fscanf(testfile,"%d",&numsearchengines);
      for(int j=1;j<=numsearchengines;j++)
	{
	  fscanf(testfile,"%s",&searchengines[j]);
	  //printf("%s\n",searchengines[i]);
	}
      fscanf(testfile,"%d",&numqueries);
      //printf("Starts here\n");
      for(int j=1;j<=numqueries;j++)
	{
	  fscanf(testfile,"%s",&searchquery[j]);
	  //printf("%s\n",searchquery[j]);
	}

      for(int j=1;j<=numsearchengines;j++)
	{
	  if(!strcmp(searchquery[1],searchengines[j]))
	    costs[j][1]=1e9;
	  else
	    costs[j][1]=0;
	}
	  
      for(int j=2;j<=numqueries;j++)
	{
	  for(int k=1;k<=numsearchengines;k++)
	    {
	      costs[k][j]=1e9;
	      if(strcmp(searchquery[j],searchengines[k]))
		{
		  for(int l=1;l<=numsearchengines;l++)
		    {
		      if(costs[l][j-1]+(k!=l)<costs[k][j])
			costs[k][j]=costs[l][j-1]+(k!=l);
		    }
		}
	    }

	}
      for(int j=2;j<=numqueries;j++)
	{
	  //for(int k=1;k<=numsearchengines;k++)
	  // printf("%lf ",costs[k][j]);
	  //printf("\n");
	}
      costs[0][0]=1e9;
      for(int k=1;k<=numsearchengines;k++)
	{
	  if(costs[0][0]>costs[k][numqueries])
	    {
	    costs[0][0]=costs[k][numqueries];
	    //printf("optimal ending is %s %lf\n",searchengines[k],costs[0][0]);
	    }
	}
      printf("Case #%d: %1.0f\n",i,costs[0][0]);
    }
  
  



}
