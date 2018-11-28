#include<iostream>
#include<cmath>
#define pi acos(-1)
using namespace std;

long double getchordarea(long double x2,long double y2,long double x1,long double y1,long double R)
{ long double theta=atan((y2*x1-y1*x2)/(x1*x2+y1*y2));
  long double sectorarea=R*R*theta/2;
  sectorarea-=abs(x1*y2-y1*x2)/2;
  return sectorarea;
}

int main()
{ int N;
  long double f, R, t, r ,g;
  cin>>N;
  for(int i=0;i<N;i++)
  { cin>>f>>R>>t>>r>>g;
    long double x1=r,x2=r+g;
    long double y1=r,y2=r+g;
    long double sum=0;
    if(2*f<g)
    while(x1<R-t)
    { y1=r;
      y2=r+g;
      while(y1<R-t)
      { long double xmin=x1+f;
        long double xmax=x2-f;
        long double ymin=y1+f;
        long double ymax=y2-f;
        long double RR=R-t-f;
        long double ux=-1,bx=-1,ry=-1,ly=-1;
        ux=((RR>=ymax)?(sqrt(RR*RR-ymax*ymax)):-1);
        bx=sqrt(RR*RR-ymin*ymin);
        ry=((RR>=xmax)?(sqrt(RR*RR-xmax*xmax)):-1);
        ly=sqrt(RR*RR-xmin*xmin);
        if(ymax<=RR&&xmax<=RR&&ux>=xmin&&ux<=xmax&&ry>=ymin&&ry<=ymax)
        { 
          sum+=(xmax-xmin)*(ymax-ymin)-(xmax-ux)*(ymax-ry)/2+getchordarea(ux,ymax,xmax,ry,RR);
        }
        else if(ymax<=RR&&ux>=xmin&&ux<=xmax&&bx>=x1&&bx<=x2)
        { 
          sum+=(ux-xmin)*(ymax-ymin)+(ymax-ymin)*(bx-ux)/2+getchordarea(ux,ymax,bx,ymin,RR);
        }
        else if(xmax<=RR&&ly>=ymin&&ly<=ymax&&ry>=ymin&&ry<=ymax)
        { 
          sum+=(ry-ymin)*(xmax-xmin)+(xmax-xmin)*(ly-ry)/2+getchordarea(xmin,ly,xmax,ry,RR);
        }
        else if(ly>=ymin&&ly<=ymax&&bx>=xmin&&bx<=xmax)
        {
          sum+=(bx-xmin)*(ly-ymin)/2+getchordarea(xmin,ly,bx,ymin,RR);
        }
        else if(xmax<=RR&&ymax<=RR&&ux>xmax&&ry>ymax)
        { 
          sum+=(xmax-xmin)*(ymax-ymin);
        }
        y1+=g+2*r;
        y2+=g+2*r;
      }
      x1+=g+2*r;
      x2+=g+2*r;
    }
    long double totarea=pi*R*R;
    long double res=1.0-sum*4/totarea;
    cout<<"Case #"<<i+1<<": "<<res<<"\n";
  }
}
