#include <iostream>
#include <string>
using namespace std;
typedef struct
{
  int start,end;
}TR;
TR a[200],b[200];
int main()
{
  int n,na,nb,cs=0,p1[200],p2[200],p;
  int i,j,tmp1,tmp2;
  int t1,t2,t3,t4;
  int tmp3,tmp4,t,test;
  scanf("%d",&n);
  while(n--)
    {
      cs++;
      memset(p1,0,sizeof(p1));
      memset(p2,0,sizeof(p2));
      scanf("%d",&t);
      scanf("%d%d",&na,&nb);
      for(i=0;i<na;i++)
	{
	  getchar();
	  scanf("%d:%d",&t1,&t2);
	  a[i].start=t1*60+t2;
	  getchar();
	  scanf("%d:%d",&t1,&t2);
	  a[i].end=t1*60+t2;
	  //printf("%d %d\n",a[i].start,a[i].end);
	}
      for(i=0;i<nb;i++)
	{
	  getchar();
	  scanf("%d:%d",&t1,&t2);
	  b[i].start=t1*60+t2;
	  getchar();
	  scanf("%d:%d",&t1,&t2);
	  b[i].end=t1*60+t2;
	  //printf("%d %d\n",b[i].start,b[i].end);
	}
      //sort(a,a+na,cmp);
      //sort(b,b+nb,cmp);
      tmp1=na;
      tmp2=nb;
      for(i=0;i<nb;i++)
	{
	  p=-1;
	  tmp4=10000;
	  test=b[i].end+t;
	  for(j=0;j<na;j++)
	    {
	      if(p1[j]==0)
		{
		  tmp3=a[j].start-test;
		  if(tmp3>=0&&tmp3<tmp4)
		    {
		      tmp4=tmp3;
		      p=j;
		    }
		}
	    }
	  if(p!=-1)
	    {
	      p1[p]=1;
	      tmp1--;
	    }
	}

      for(i=0;i<na;i++)
	{
	  p=-1;
	  tmp4=10000;
	  test=a[i].end+t;
	  //printf("  %d\n",test);
	  for(j=0;j<nb;j++)
	    {
	      if(p2[j]==0)
		{
		  tmp3=b[j].start-test;
		  //printf("%lf\n",tmp3);
		  if(tmp3>=0&&tmp3<tmp4)
		    {
		      tmp4=tmp3;
		      p=j;
		    }
		}
	    }
	  if(p!=-1)
	    {
	      p2[p]=1;
	      tmp2--;
	      //printf("%lf\n",b[p].start);
	    }
	}
      printf("Case #%d: %d %d\n",cs,tmp1,tmp2);
    }
  return 0;
}
