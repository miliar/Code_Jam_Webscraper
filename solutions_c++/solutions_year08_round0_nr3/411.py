#include<iostream>
using namespace std;
#include<math.h>
const double eps = 1e-7;
const double pi = acos(-1);
double f,R,r,g,t;
int main()
{
    double sums,dx,dy,x,y,inr,upy,res;
    long casenum = 1,caseamount;
    freopen("ansc.txt","w",stdout);
    
    scanf("%ld",&caseamount);
    while(caseamount--)
    {
      scanf("%lf%lf%lf%lf%lf",&f,&R,&t,&r,&g);
      
      sums = 0.0;
      
      inr = R-t;
      
      for(dx = 0.0;dx<=inr; dx += (2*r+g))
       for(dy = 0.0;dy<=inr; dy += (2*r+g))
       {
           if((dx+g+r)*(dx+g+r)
            +(dy+g+r)*(dy+g+r)<=inr*inr)
           sums += (g-2*f)*(g-2*f);
          
           else
           {
              for(x = dx+r+f;x<=dx+r+g-f&&x<inr; x += eps)
              {
               upy = sqrt((inr-f)*(inr-f)-x*x);
               
               if(upy<=dy+r+f)
               break;
               if(upy<=dy+r+g-f)
               sums += (upy-dy-r-f)*eps;
               else
               sums += (g-2*f)*eps;
              /* for(y = dy+r+f;y<=dy+r+g-f; y += eps)
               {
                   if(x*x+y*y>(inr-f)*(inr-f))
                   break;
                   
                   sums += eps*eps;
               }   */
               }                    
          }
          }
          res = 1.0000000-4.000*sums/(pi*R*R);
          if(res<=0.0)
          res = 0.0;
       printf("Case #%ld: %lf\n",casenum++,res);
       }  
      // system("pause");           
    return 0;
}
