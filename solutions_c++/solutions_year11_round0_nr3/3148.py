#include<stdio.h>
#include<stdlib.h>
int main()
{
  int ca,n,x,min,sum,total=0,y,i;
  FILE *f;
  f=fopen("C.out","w");
  scanf("%d",&ca);
  while(ca--)
  {
	 scanf("%d",&n);
	 total++;
	 min=1000000000;
	 sum=0;
	 y=0;
	 for(i=1;i<=n;i++)
	 {
		scanf("%d",&x);
		if(x<min) min=x;
		sum+=x;
		y^=x;
	 }
	 if(y!=0) fprintf(f,"Case #%d: NO\n",total);
	 else fprintf(f,"Case #%d: %d\n",total,sum-min);
  }
  system("pause");
  return 0;
}