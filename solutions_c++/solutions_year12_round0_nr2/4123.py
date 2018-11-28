#include<iostream>
#include<cstdio>
#include<algorithm>

using namespace  std;


int compare(const void *a,const void *b)
{
  return (*(int*)b-*(int*)a);
}

int main()
{
  int t,i;
  scanf("%d",&t);
  for(i=1;i<=t;i++)
    {
      int n,s,p,j,min,count=0,second=0;
      scanf("%d %d %d",&n,&s,&p);
      min=3*p-4;;second=3*p-2;
      if(p==1){min=1;second=1;}
      if(p==0){min=0;second=0;}
      int *kick=new int[n];
      for(j=0;j<n;j++)
	scanf("%d",&kick[j]);
      qsort(kick,n,sizeof(int),compare);
      for(j=n-1;j>=0 && count<s;j--)
	{
	  if(kick[j]>=min)
	    count++;
	}
      for(;j>=0;j--)
	{
	  if(kick[j]>=second)
	    count++;
	}
      delete(kick);
      printf("Case #%d: %d\n",i,count);
    }
  return 0;
}

