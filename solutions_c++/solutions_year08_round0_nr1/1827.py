#include<stdio.h>
#include<string.h>
#include<stdlib.h>

#define MAXNAME 110L
#define MAXCAR 110L
#define MAXQ 1010L

int main()
{
  char name[MAXNAME][MAXCAR],nameTemp[MAXCAR];
  int *v[MAXNAME];
  int N,a,b,sol,num,numQ,qwer,c;

  for(a=0;a<MAXNAME;a++)
    v[a]=(int *)malloc(sizeof(int)*MAXQ);

  fgets(nameTemp,MAXCAR,stdin);
  sscanf(nameTemp," %d",&N);
  for(qwer=1;qwer<=N;qwer++)
  {
    for(a=0;a<MAXNAME;a++)
      memset(v[a],0,sizeof(int)*MAXQ);

    fgets(nameTemp,MAXCAR,stdin);
    sscanf(nameTemp," %d",&num);
    for(a=0;a<num;a++)
      fgets(name[a],MAXCAR,stdin);

    fgets(nameTemp,MAXCAR,stdin);
    sscanf(nameTemp," %d",&numQ);
    for(a=0;a<numQ;a++)
    {
      fgets(nameTemp,MAXCAR,stdin);
      for(b=0;b<num;b++)
        if(!strcmp(nameTemp,name[b]))
	  v[b][a]=-1;
    }

    for(b=0;b<num;b++)
    v[b][numQ]=numQ;
    for(a=numQ-1;a>=0;a--)
      for(b=0;b<num;b++)
        if(v[b][a]!=-1)
	{
	  if(v[b][a+1]==-1)
	    v[b][a]=a;
	  else
	    v[b][a]=v[b][a+1];
	}

    sol=0;
    for(a=0;a<numQ;a++,sol++)
    {
      for(c=0,b=1;b<num;b++)
        if(v[b][a]>v[c][a])
	  c=b;
      a=v[c][a];
    }
    sol--;
    if(sol<0)sol=0;

    printf("Case #%d: %d\n",qwer,sol);
  }

  return(0);
}

