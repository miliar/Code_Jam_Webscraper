#include <stdio.h>
#include <math.h>
#include <vector>
#include <utility>
#include <algorithm>
using namespace std;
int W,L,U,G;
vector <pair<int,int> > lower;
vector <pair<int,int> > upper;

double computeinlineupper(int id,double x)
{
  return upper[id].second+(upper[id+1].second-upper[id].second)*(x-upper[id].first)/(double)(upper[id+1].first-upper[id].first);
}
double computeinlinelower(int id,double x)
{
  return lower[id].second+(lower[id+1].second-lower[id].second)*(x-lower[id].first)/(double)(lower[id+1].first-lower[id].first);

}

double computetotarea(double x)
{
  int il=0;
  int ih=0;
  int cx=0;
  double totarea=0;
  while(il<lower.size() && ih<upper.size())
    {
      //line from il to il+1
      //line from ih to ih+1
      int nil,nih,nx;
      if(lower[il+1].first<upper[ih+1].first)
	{
	  nx=lower[il+1].first;
	  nil=il+1;
	  nih=ih;
	}
      if(lower[il+1].first>upper[ih+1].first)
	{
	  nx=upper[ih+1].first;
	  nil=il;
	  nih=ih+1;
	}
      if(lower[il+1].first==upper[ih+1].first)
	{
	  nx=upper[ih+1].first;
	  nil=il+1;
	  nih=ih+1;
	}
      //printf("%d to %d\n",cx,nx);


      //check if x is between cx and nx
      if(x>=cx && x<=nx)
	{
	  double yh1=computeinlineupper(ih,cx);
	  double yh2=computeinlineupper(ih,x);
	  double yl1=computeinlinelower(il,cx);
	  double yl2=computeinlinelower(il,x);

	  return totarea+0.5*(yh2-yl2+yh1-yl1)*(x-cx);
	}
        double yh1=computeinlineupper(ih,cx);
	double yh2=computeinlineupper(ih,nx);
	double yl1=computeinlinelower(il,cx);
	double yl2=computeinlinelower(il,nx);
	totarea+=0.5*(yh2-yl2+yh1-yl1)*(nx-cx);
	//printf("%lf\n",totarea);
	cx=nx;
	il=nil;
	ih=nih;
      
    }
}

int main()
{
  int T;
  scanf("%d",&T);
  for(int t=1;t<=T;t++)
    {
      printf("Case #%d:\n",t);
      scanf("%d",&W);
      scanf("%d%d%d",&L,&U,&G);
      lower.resize(0);
      upper.resize(0);
      for(int i=0;i<L;i++)
	{
	  int x,y;
	  scanf("%d%d",&x,&y);
	  lower.push_back(make_pair(x,y));
	}
      for(int i=0;i<U;i++)
	{
	  int x,y;
	  scanf("%d%d",&x,&y);
	  upper.push_back(make_pair(x,y));
	}
      sort(lower.begin(),lower.end());
      sort(upper.begin(),upper.end());
   
      double totarea=computetotarea(W);
      //printf("totarea= %lf\n",totarea);
      //return(0);
      for(int a=1;a<=G-1;a++)
	{
	  double reqdarea=a*(totarea/G);
	  double low=0;
	  double high=W;
	  for(int iters=1;iters<=100;iters++)
	    {
	      double mid=(low+high)/2;
	      if(computetotarea(mid)>reqdarea)
		high=mid;
	      else
		low=mid;
	    }
	  printf("%1.10f\n",low);
	  
	}


    }
}
