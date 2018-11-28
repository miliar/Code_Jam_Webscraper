#include <stdio.h>
#include <math.h>
#include <string>

int numcases;
int numsearchengines;
char filename[50];
char searchengines[1002][102];
char searchquery[1002][102];
FILE *testfile;
int numqueries;

char word[100];
double starttime,endtime;
int NA,NB;
double tttime;

double timearray[300][4];
bool isscheduled[300];
double nextstarttime;
int nextstartwith;
bool starter[300];
int count;
bool allscheduled;
bool canhandlemoretrips;
double mintime;
int startwith;
int minnextstarttime;
int numstarttrains[4];
bool currlocation;
int main(int argc,char *argv[])
{

  strcpy(filename,argv[1]);
  testfile=fopen(filename,"r");
  fscanf(testfile,"%d",&numcases);
  
  for(int i=1;i<=numcases;i++)
    {
      //printf("case %d\n",i);
      fscanf(testfile,"%lf",&tttime);
      fscanf(testfile,"%d",&NA);
      fscanf(testfile,"%d",&NB);
      count=0;
      for(int j=1;j<=NA;j++)
	{
	  fscanf(testfile,"%s",word);
	  starttime=((word[0]-'0')*10+(word[1]-'0'))*60+((word[3]-'0')*10+word[4]-'0');
	  fscanf(testfile,"%s",word);
	  endtime=((word[0]-'0')*10+(word[1]-'0'))*60+((word[3]-'0')*10+word[4]-'0');
	  //printf("%lf %lf\n",starttime,endtime);
	  count++;
	  timearray[count][1]=0;
	  timearray[count][2]=starttime;
	  timearray[count][3]=endtime;
	  isscheduled[count]=0;

	}
      for(int j=1;j<=NB;j++)
	{
	  fscanf(testfile,"%s",word);
	  starttime=((word[0]-'0')*10+(word[1]-'0'))*60+((word[3]-'0')*10+word[4]-'0');
	  fscanf(testfile,"%s",word);
	  endtime=((word[0]-'0')*10+(word[1]-'0'))*60+((word[3]-'0')*10+word[4]-'0');
	  count++;
	  timearray[count][1]=1;
	  timearray[count][2]=starttime;
	  timearray[count][3]=endtime;
	  isscheduled[count]=0;
	 
	}
      
      for(int j=1;j<=NA+NB;j++)
	{
	  isscheduled[j]=0;
	  starter[j]=0;
	}
      allscheduled=0;
      numstarttrains[0]=0;
      numstarttrains[1]=0;
      while(allscheduled==0)
	{
	  allscheduled=1;
	  //find the min unscheduled
	  mintime=24*60;
	  
	  for(int j=1;j<=NA+NB;j++)
	    {
	      if(!isscheduled[j] && timearray[j][2]<=mintime)
		{
		  mintime=timearray[j][2];
		  startwith=j;
		  allscheduled=0;
		}
	      
	    }
	  //printf("Start with = %d\n",startwith);
	  //printf("%lf %lf\n",timearray[startwith][2],timearray[startwith][3]);
	  currlocation=(startwith<=NA);
	  if(allscheduled==0)
	    {
	      if(startwith<=NA)
	      numstarttrains[0]++;
	      else
		numstarttrains[1]++;
	    }
	  starter[startwith]=1;
	  canhandlemoretrips=1;
	  while(canhandlemoretrips)
	    {
	      canhandlemoretrips=0;
	      isscheduled[startwith]=1;
	      nextstarttime=timearray[startwith][3]+tttime;
	      //printf("Ends at %lf\n",nextstarttime);
	      minnextstarttime=24*60;
	      for(int j=1;j<=NA+NB;j++)
		{
		  
		  if(timearray[j][2]>=nextstarttime && timearray[j][2]<=minnextstarttime && isscheduled[j]==0 && (j<=NA)!=currlocation)
		    {
		      //printf("Found\n");
		      nextstartwith=j;
		      minnextstarttime=timearray[j][2];
		      canhandlemoretrips=1;
		    }
		  
		}
	      if(canhandlemoretrips)
		{
		  startwith=nextstartwith;
		  currlocation=!currlocation;
		 
		}

	    }
	  //printf("End with = %d\n",startwith);
	


	}
      
        printf("Case #%d: %d %d\n",i,numstarttrains[0],numstarttrains[1]);
	
      
    }

}
