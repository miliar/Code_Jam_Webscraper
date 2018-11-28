#include <stdio.h>
#include <math.h>
#include <string>
#include <vector>
using namespace std;

FILE *testfile;
char filename[100];
int numtestcases;
int isnode[10002];
int G[10002];
int C[10002];
int value[10002];
int minchange(int nodenum,int reqvalue);
int M,V;
int minn(int a,int b,int c);
int cache[20000][3];
int main(int argc,char*argv[])
{

 
  strcpy(filename,argv[1]);
  testfile=fopen(filename,"r");
  fscanf(testfile,"%d",&numtestcases);
  
  for(int n=1;n<=numtestcases;n++)
    {
      fscanf(testfile,"%d",&M);
      fscanf(testfile,"%d",&V);
      for(int i=1;i<=20000;i++)
	{
	cache[i][0]=-1;
	cache[i][1]=-1;
	}
      //printf("%d %d\n",M,V);
      for(int i=1;i<=(M-1)/2;i++)
	{
	  fscanf(testfile,"%d",&G[i]);
	  fscanf(testfile,"%d",&C[i]);
	  C[i]=1-C[i];
	  isnode[i]=1;
	  
	}
      for(int i=(M+1)/2;i<=M;i++)
	{
	  fscanf(testfile,"%d",&value[i]);
	  isnode[i]=0;
					       
	}
      int answers=minchange(1,V);
      if(answers<=10000)
      printf("Case #%d: %d\n",n,minchange(1,V));
      else
	      printf("Case #%d: IMPOSSIBLE\n",n);

      
    }


  fclose(testfile);
  
}


//G is 1->and gate
//G is 0-> or gate
int minchange(int nodenum,int reqvalue)
{
  
  int i=nodenum;
  if(isnode[i]==0 && reqvalue!=value[i])
    return 20000;
  if(isnode[i]==0 && reqvalue==value[i])
    return 0;
  if(cache[nodenum][reqvalue]>=0)
  return cache[nodenum][reqvalue];
  
  //nodenum is connected to 2*nodenum and 2*nodenum+1
  
  //if it is an or and required value is 0
  if(G[i]==0 && reqvalue==0)
    {
     
	cache[i][0]= minn(minchange(2*nodenum,0)+minchange(2*nodenum+1,0),minchange(2*nodenum,1)+minchange(2*nodenum+1,0)+1+C[i]*20000,minchange(2*nodenum,0)+minchange(2*nodenum+1,1)+1+C[i]*20000);
	return cache[i][0];
      return minn(minchange(2*nodenum,0)+minchange(2*nodenum+1,0),minchange(2*nodenum,1)+minchange(2*nodenum+1,0)+1+C[i]*20000,minchange(2*nodenum,0)+minchange(2*nodenum+1,1)+1+C[i]*20000);
	
    }
  //or and 1
  if(G[i]==0 && reqvalue==1)
    {
      cache[i][1]= minn(minchange(2*nodenum,0)+minchange(2*nodenum+1,1),minchange(2*nodenum,1)+minchange(2*nodenum+1,0),minchange(2*nodenum,1)+minchange(2*nodenum,1));
      return cache[i][1];
      return minn(minchange(2*nodenum,0)+minchange(2*nodenum+1,1),minchange(2*nodenum,1)+minchange(2*nodenum+1,0),minchange(2*nodenum,1)+minchange(2*nodenum,1));
    }
//and and 1
  if(G[i]==1 && reqvalue==1)
    {
      cache[i][1]= minn(minchange(2*nodenum,1)+minchange(2*nodenum+1,1),minchange(2*nodenum,0)+minchange(2*nodenum+1,1)+1+C[i]*20000,minchange(2*nodenum,1)+minchange(2*nodenum+1,0)+1+C[i]*20000);
    
      return minn(minchange(2*nodenum,1)+minchange(2*nodenum+1,1),minchange(2*nodenum,0)+minchange(2*nodenum+1,1)+1+C[i]*20000,minchange(2*nodenum,1)+minchange(2*nodenum+1,0)+1+C[i]*20000);
    }
  if(G[i]==1 && reqvalue==0)
    {
      cache[i][0]= minn(minchange(2*nodenum,0)+minchange(2*nodenum+1,1),minchange(2*nodenum,1)+minchange(2*nodenum+1,0),minchange(2*nodenum,0)+minchange(2*nodenum+1,0));
      return cache[i][0];
      return minn(minchange(2*nodenum,0)+minchange(2*nodenum+1,1),minchange(2*nodenum,1)+minchange(2*nodenum+1,0),minchange(2*nodenum,0)+minchange(2*nodenum+1,0));
    }
  

}


int minn(int a,int b,int c)
{
  if(a<=b && a<=c)
    return a;
  if(b<=a && b<=c)
    return b;
  return c;
}
