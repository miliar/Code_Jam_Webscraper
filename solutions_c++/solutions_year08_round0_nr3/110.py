#include <iostream>
#include <math.h>
using namespace std;
#define pai 3.1415926
struct Point
{
	double x;
	double y;
}pa,pb,pc,pd,pe;
int main()
{
	//freopen("C-large.in","r",stdin);
	//freopen("C-large.out","w",stdout);
	int N,i;
	double f,R,t,r,g,sbank,sall,tmp;
	cin>>N;
	for(i=1;i<=N;i++)
	{
		cin>>f>>R>>t>>r>>g;
		g=g-f-f;
		r=r+f;
		t=t+f;	
		sall=pai*R*R;
		sbank=0;
		pa.x=r;
		pa.y=r;
		if(g>0)
		{
			while(true)
			{
				if((pa.x*pa.x+pa.y*pa.y)>=(R-t)*(R-t)) break;
				pb.y=pa.y;
				tmp=sqrt((R-t)*(R-t)-pb.y*pb.y);
				pb.x=pa.x+g;
				if(pb.x>tmp) pb.x=tmp;
				if(pb.x<pa.x) pb.x=pa.x;
				pc.x=pa.x;
				tmp=sqrt((R-t)*(R-t)-pc.x*pc.x);
				pc.y=pa.y+g;
				if(pc.y>tmp) pc.y=tmp;
				if(pc.y<pa.y) pc.y=pa.y;
				pd.y=pc.y;
				tmp=sqrt((R-t)*(R-t)-pd.y*pd.y);
				pd.x=pc.x+g;
				if(pd.x>tmp)pd.x=tmp;
				if(pd.x<pc.x) pd.x=pc.x;
				sbank+=(pd.x-pc.x)*(pc.y-pa.y);	
				if(pd.x!=pb.x)
				{
					pe.x=pb.x;
					pe.y=sqrt((R-t)*(R-t)-pe.x*pe.x);
					tmp=atan(pd.y/pd.x)-atan(pe.y/pe.x);
					sbank+=(R-t)*(R-t)*(tmp-sin(tmp))/2;			
					sbank+=(pe.y-pb.y+pd.y-pb.y)*(pe.x-pd.x)/2;
				}
				if(pc.y==pa.y+g)
				{
					pa.y=pc.y+r+r;
					if((pa.x*pa.x+pa.y*pa.y)>=(R-t)*(R-t))
					{
						pa.y=r;
						pa.x=pa.x+g+r+r;
					}
				}
				else 
				{
					pa.y=r;
					pa.x=pa.x+g+r+r;
				}
			}
		}
		printf("Case #%d: %.6f\n",i,(sall-sbank*4)/sall);		
	}
	return 0;
}