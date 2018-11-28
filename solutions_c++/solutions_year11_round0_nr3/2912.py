#include<stdio.h>
#include<math.h>
#include<stdlib.h>

unsigned long int specialadd(unsigned long int x,unsigned long int y)
 {
	int a[21]={0},b[21]={0},la=0,lb=0,i=0,m;
	unsigned long int t;
	t=x;
	 while(t>0)
	  {
		 a[la]=(int)(t%2);
		 t=t/2;
		 la++;
	  }
	  t=y;i=0;
	  while(t>0)
		{
		 b[lb]=(int)(t%2);
		 t=t/2;
		 lb++;
		}
	m=max(la-1,lb-1);
	while(i<=m)
	  {
		 a[i]=abs(a[i]-b[i]);
		 i++;
	  }
	  i=0;
	  while(i<=m)
		{
			t=t+(pow(2,i)*a[i]);
			i++;
		}
		return t;

 }

void main()
	{
	 int t,tc=1,nc;
	 unsigned long int sum,part,mini,candy;
	  for(scanf("%u",&t);tc<=t;tc++)
		{
		sum=0;part=0;
		scanf("%d",&nc);
		scanf("%li ",&mini);
		sum=specialadd(sum,mini);
	  part=part+mini;
			for(int i=1;i<nc;i++)
			  {
				 scanf("%li ",&candy);
				 mini=min(candy,mini);
				 sum=specialadd(sum,candy);
				 part=part+candy;
		   }
			if(sum==0)
				printf("Case #%d: %li\n",tc,(part-mini));
			 else
			  printf("Case #%d: NO\n",tc);
		}

	}
