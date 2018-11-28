#include<iostream>
#include<cmath>
using namespace std;
long double pi=3.1415926535898;

long double sqr(long double x)
{
  return x*x;
}

long double calc(long double x0,long double y0,long double x1,long double y1,long double r)
{
  long double chord,cita,ans;
  chord=sqrt(sqr(x0-x1)+sqr(y0-y1));
  cita=asin(chord/2/r)*2;
  ans=(cita*r*r-x0*(y1-y0)-y0*(x1-x0))/2;
  return ans;
}

int main()
{
  freopen("c_large.out","w",stdout);
  int cn,ci;
  long double f,R,t,r,g,tot_s,cur_s,ra,sqra,step,len,x0,x1,x2,x3,xx0,xx2,yy0,yy1,y0,y1,y2,y3,ans;
  cout<<fixed;
  cout.precision(7);
  cin>>cn;
  for (ci=1;ci<=cn;ci++)
  {
    cin>>f>>R>>t>>r>>g;
    if (f*2>=g)
    {
      cout<<"Case #"<<ci<<": "<<1<<endl;
      continue;
    }
    tot_s=pi*R*R;
    cur_s=0;
    ra=R-t-f;
    sqra=ra*ra;
    step=g+r*2;
    len=g-f*2;
    for (x0=r+f;x0<ra;x0+=step)
      for (y0=r+f;sqr(x0)+sqr(y0)<sqra;y0+=step)
      {
        x1=x0+len;
        y1=y0;
        x2=x0;
        y2=y0+len;
        x3=x0+len;
        y3=y0+len;
        if (sqr(x3)+sqr(y3)<sqra)
        {
          cur_s+=sqr(len);
          continue;
        }
        if (sqr(x1)+sqr(y1)>=sqra)
        {
          if (sqr(x2)+sqr(y2)>=sqra)
          {
            xx0=sqrt(sqra-sqr(y0));
            yy0=sqrt(sqra-sqr(x0));
            cur_s+=calc(x0,y0,xx0,yy0,ra);
          }
          else
          {
            xx0=sqrt(sqra-sqr(y0));
            xx2=sqrt(sqra-sqr(y2));
            cur_s+=len*(xx2-x0)+calc(xx2,y0,xx0,y2,ra);
          }
        }
        else
        {
          if (sqr(x2)+sqr(y2)>=sqra)
          {
            yy0=sqrt(sqra-sqr(x0));
            yy1=sqrt(sqra-sqr(x1));
            cur_s+=len*(yy1-y0)+calc(x0,yy1,x1,yy0,ra);
          }
          else
          {
            xx2=sqrt(sqra-sqr(y2));
            yy1=sqrt(sqra-sqr(x1));
            cur_s+=len*(xx2-x0)+len*(yy1-y0)-(xx2-x0)*(yy1-y0)+calc(xx2,yy1,x1,y2,ra);
          }
        }
      }
    ans=1-cur_s*4/tot_s;
    cout<<"Case #"<<ci<<": "<<ans<<endl;
  }
  return 0;
}