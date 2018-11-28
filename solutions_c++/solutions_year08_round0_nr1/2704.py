#include<stdio.h>
#include<string.h>
char q[100][100];
char s[100][100];
int findno(char s[],int start,int qn)
{
     
     int flag=0,i;
     for(i=start;i<qn;i++)
     {
	if(strcmp(s,q[i])==0)
	 {
	    flag=1;
	    break;
	 }
      }
     if (flag==0)
      {
	return 9999;
      }
     else
      return (i-start);
}
int findmax(int a[],int sn)
{
   int k=a[0];
   for(int i=1;i<sn;i++)
   {
       if(k<a[i])
	{
	  k=a[i];
	}
   }
   return k;
}

void main()
{
 FILE *f1;
 int n,sn,qn,i,nos,nproce,k,proce;
 int order[20];
 f1=fopen("universe.out","w");
 scanf("%d",&n);
 for(k=0;k<n;k++)
  {
       nos=0;
       scanf("%d",&sn);
	for(i=0;i<sn;i++)
	{
	   scanf(" %[^\n]", s[i]);
	}
       scanf("%d",&qn);
	for(i=0;i<qn;i++)
	{
	   scanf(" %[^\n]", q[i]);
	}

	for(i=0;i<sn;i++)
	order[i]=findno(s[i],0,qn);
	nproce=findmax(order,sn);
	proce=nproce;
	while(proce<qn)
	{
	     nos+=1;
	     for(i=0;i<sn;i++)
	     order[i]=findno(s[i],proce,qn);
	     nproce=findmax(order,sn);
	     proce+=nproce;
	}
	fprintf(f1,"Case #%d: %d\n",k+1,nos);
   }
  fclose(f1);
}

