#include<iostream>
#include<vector>
#include<list>
#include<string>
#include<algorithm>
#include<stdio.h>
#include <sstream>
#include<math.h>
#define PI 3.14159265
using namespace std;
double f,r,t,R,g,ar,p,totar;
void outp(int i)
{
     cout<<"Case #"<<i+1<<": ";
     printf("%f\n",p);
}
int main()
{
    int N,i,j,k,xflag,yflag;
    double a1,a2,a3,x,y,x1,x2,y1,y2,r1,x3,y3,theta;
    cin>>N;
    for(i=0;i<N;i++)
    {
           cin>>f>>R>>t>>r>>g;
           //cout<<f<<" "<<R<<" "<<t<<" "<<r<<" "<<g;
           if(2*f>g)
           {
                   p=1;
                   outp(i);
                   continue;
           }
           totar=PI*R*R;
           a1=(g-(2*f))*(g-(2*f));
           x=r;
           a2=0;
           //flagx=flagy=0;
           while(x<R-t)
           {
               x=x+g;
               y=r;
               while(y<R-t)
               {
                      y=y+g;
                      if(sqrt((x*x+y*y))<R-t)
                      {
                            a2+=a1;
                            //cout<<"there"<<x<<" "<<y<<" "<<R-t;
                      }
                      else
                      {
                          //cout<<"here";
                          x1=(x+f-g); y1=y+f-g;
                          r1=(R-(t+f));
                          x2=sqrt((r1*r1)-(y1*y1));
                          y2=sqrt((r1*r1)-(x1*x1));
                          xflag=yflag=0;
                          if(x2>x-f)
                          {
                                    x2=x-f;
                                    y3=sqrt((r1*r1)-(x2*x2));
                                    xflag=1;
                          }
                          if(y2>y-f)
                          {
                                    y2=y-f;
                                    x3=sqrt((r1*r1)-(y2*y2));
                                    yflag=1;
                          }
                          if(x2>x1&&y2>y1)
                          {
                              if(xflag==1||yflag==1)
                              {
                                  if(xflag==1&&yflag==1)
                                  {
                                         a2+=((x3-x1)*(y2-y1))+((x2-x3)*(y3-y1))+(0.5*(x2-x3)*(y2-y3));//when 3 sides are visible
                                         theta=fabs(fabs(acos(x3/r1))-fabs(asin(y3/r1)));
                                  }
                                  else if(xflag==1)
                                  {
                                             a2+=((x2-x1)*(y3-y1))+(0.5*(x2-x1)*(y2-y3));//area of sq + triangle
                                             theta=fabs(fabs(acos(x1/r1))-fabs(asin(y3/r1)));
                                  }
                                  else if(yflag==1)
                                  {
                                             a2+=((x3-x1)*(y2-y1))+(0.5*(x2-x3)*(y2-y1));//area of sq + triangle
                                             theta=fabs(fabs(acos(x3/r1))-fabs(asin(y1/r1)));
                                  }//cout<<"here";
                              }
                              else
                              {
                                  a2+=(0.5*(x2-x1)*(y2-y1));//area of triangle
                                  theta=fabs(fabs(asin(y2/r1))-fabs(acos(x2/r1)));
                                  //cout<<"here";
                              }
                              a2+=r1*r1*0.5*(theta-sin(theta));//area of segment
                              //cout<<"here";
                          }
                      }
                      y+=(2*r);
               }
               x+=(2*r);
           }
           //cout<<"**"<<4*a2<<totar;
           p=1.0-(4*a2/totar);
           //if(p<0) p=0;
           outp(i);
    }
    //system("PAUSE");
    return 1;
}
