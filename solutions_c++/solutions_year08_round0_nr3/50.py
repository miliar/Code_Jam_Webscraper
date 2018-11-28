#include<iostream>
#include<cmath>
#include<algorithm>
using namespace std;

const double tol=1e-9;
const double pi = 2*acos(0);
double bararea(double r,double w,double off,double bot)
{
  double maxw=sqrt(max(0.0,r*r-bot*bot))-off;
  if(maxw<0) return 0;
  if(maxw<w) w=maxw;
  double th1=acos(off/r), th2=acos(min((off+w)/r,1.0));
  double ar1=r*r*(th1/2-sin(2*th1)/4);
  double ar2=r*r*(th2/2-sin(2*th2)/4);
//  cerr<<th1*180/pi<<' '<<th2*180/pi<<' '<<ar1<<' '<<ar2<<' '<<w<<endl;
  return ar1-ar2-w*bot;
}

double sqarea(double r,double w,double stx,double sty)
{ 
  double rv=bararea(r,w,stx,sty)-bararea(r,w,stx,sty+w); 
//  cerr<<"Sq "<<r<<' '<<w<<' '<<stx<<' '<<sty<<' '<<bararea(r,w,stx,sty)<<' '<<bararea(r,w,stx,sty+w)<<endl;
  return rv;
}
double isectarea(double r,double w,double g)
{
  double rv=0;
  typedef long long lli;
  lli c=lli(tol+ceil((r-g/2)/(w+g)));
  if(c>20000000) return pi*r*r*(w*w/((w+g)*(w+g)));
  lli i,j;
  for(i=0;i<c;++i)
  { double ex=g/2+(w+g)*i+w;
    double ulim=sqrt(max(0.0,r*r-ex*ex));
    double uulim=sqrt(max(0.0,r*r-(ex-w)*(ex-w)));
    lli wholec=lli((ulim+g/2)/(w+g));
    lli allc=lli(tol+ceil((uulim-g/2)/(w+g)));
//    cerr<<c<<' '<<ex<<' '<<ulim<<' '<<uulim<<' '<<wholec<<' '<<allc<<endl;
    rv+=w*w*wholec;
    for(j=wholec;j<allc;++j) rv+=sqarea(r,w,g/2+i*(g+w),g/2+j*(g+w));
  }
  return rv*4;
}
double calc(double f,double R,double t,double r,double g)
{
  if(t==0 && r==0) return 0;
  double den=pi*R*R;
  double ar=R-t-f,aw=g-2*f,ag=2*r+2*f;
  if(ar<0||aw<0) return 1;
//  cerr<<"adjusted "<<ar<<' '<<aw<<' '<<ag<<endl;
  double num=isectarea(ar,aw,ag);
  return 1-num/den;
}

int main()
{
  //double r,w,off,bot;
  //while(cin>>r>>w>>off>>bot) cout<<bararea(r,w,off,bot)<<endl;
  //*
  int ci,cn;
  double f,R,t,r,g;
  cin>>cn;
  for(ci=1;ci<=cn;++ci)
  { cin>>f>>R>>t>>r>>g;
    cout.precision(6);
    cout<<"Case #"<<ci<<": "<<fixed<<calc(f,R,t,r,g)<<endl;
  }
  // */
}
