#include <stdio.h>
#include <math.h>
struct zw
{
	double x;
	double y;
	double r;
}d[10];
int main()
{
  int n,i,j,k,t,t1;
  double t2,t3,t4,t5,res;
  freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
  scanf("%d",&t);
  t1=1;
  while (t--) 
  {
    scanf("%d",&n);
	for(i=0;i<n;i++)
     scanf("%lf%lf%lf",&d[i].x,&d[i].y,&d[i].r);
	if(n==1)
	{
		printf("Case #%d: %lf\n",t1++,d[0].r);
	}
	else if(n==2)
	{
		if(d[0].r>d[1].r)
		printf("Case #%d: %lf\n",t1++,d[0].r);
		else
        printf("Case #%d: %lf\n",t1++,d[1].r);
	}
		else if(n==3)
	{
		res=1000000.0;
		t2=sqrt((d[0].x-d[1].x)*(d[0].x-d[1].x)+(d[0].y-d[1].y)*(d[0].y-d[1].y));
		t2=(t2+d[0].r+d[1].r)/2.0;
        t3=d[2].r;
		if(t3>t2)
			t4=t3;
		else
			t4=t2;
		if(t4<res)
			res=t4;
		t2=sqrt((d[0].x-d[2].x)*(d[0].x-d[2].x)+(d[0].y-d[2].y)*(d[0].y-d[2].y));
		t2=(t2+d[0].r+d[2].r)/2.0;
        t3=d[1].r;
		if(t3>t2)
			t4=t3;
		else
			t4=t2;
		if(t4<res)
			res=t4;
		t2=sqrt((d[1].x-d[2].x)*(d[1].x-d[2].x)+(d[1].y-d[2].y)*(d[1].y-d[2].y));
		t2=(t2+d[1].r+d[2].r)/2.0;
        t3=d[0].r;
		if(t3>t2)
			t4=t3;
		else
			t4=t2;
		if(t4<res)
			res=t4;
		printf("Case #%d: %lf\n",t1++,res);
	}
  }
  return 0;
}
