#include <stdio.h>
#include <stdlib.h>

int cmp(const void *a,const void *b)
{
	return *(int*)a-*(int*)b;
}

int data[1005];

int main()
{
  int T,i,c = 0,sum,N;

  scanf("%d",&T);
  while(T--)
  {
	  c++;
	  sum = 0;
	  scanf("%d",&N);
	  for(i = 0;i<N;i++)
	  {
		  scanf("%d",&data[i]);
		  sum^=data[i];
	  }
	  if(sum==0)
	  {
		  qsort(data,N,sizeof(data[0]),cmp);
		  sum = 0;
		  for(i = N-1;i>=1;i--)
			  sum+=data[i];
		  printf("Case #%d: %d\n",c,sum);
	  }
	  else
		  printf("Case #%d: NO\n",c);
  }
  return 0;
}