#include <iostream>
#include <cmath>

using namespace std;

#define for_to(i,j,k) for(i=j; i<=k; ++i)
#define for_downto(i,j,k) for(i=j; i>=k; --i)

int n_tests,test;
int i,j,k;
double f,R,t,r,g;
double total,safe;
int row,col;
double X1,Y1,X2,Y2,side,ans,x_left,y_left,x_right,y_right;
double alpha,beta,in_r;
const double pi=acos(-1);

double other (double q)
{
  return sqrt(in_r*in_r-q*q);
}

int main()
{
  scanf("%d",&n_tests);
  for_to(test,1,n_tests)
  {
    scanf("%lf %lf %lf %lf %lf",&f,&R,&t,&r,&g);
    total=(pi*R*R)/4.0;
    //printf("total=%.6lf\n",total);
    //printf("inradius=%.6lf\n",R-t);
    safe=0.0;
    in_r=R-t-f;
    if (g>2*f)
    {
      for (col=0; ; ++col)
      {
        X1=r+(g+2*r)*col+f;
        if (X1>=in_r) break;
        for (row=0; ; ++row)
        {
          Y1=r+(g+2*r)*row+f;
          if (hypot(X1,Y1)>=in_r) break;
          //printf("corner %.6lf %.6lf distance %.6lf\n",X1,Y1,hypot(X1,Y1));
          side=g-2*f;
          X2=X1+side;
          Y2=Y1+side;
          if (hypot(X2,Y2)<=in_r)
          {
            //cout << "E" << endl;      
            safe+=side*side;
          }
          else
          {
            // intersection
            int in2,in4;
            in2=hypot(X1+side,Y1)<=in_r;
            in4=hypot(X1,Y1+side)<=in_r;
            if (!in2 && !in4)
            {
              x_left=X1;
              y_left=other(x_left);
              y_right=Y1;
              x_right=other(y_right);
              //cout << "A" << endl;              
              safe+=( (y_left-Y1)*(x_right-X1) ) / 2.0;
            }
            else if (in2 && !in4)
            {
              x_left=X1;
              y_left=other(x_left);
              x_right=X2;
              y_right=other(x_right);
              //cout << "B" << endl;
              safe+= ( ( (y_left-Y1)+(y_right-Y1) ) * side ) / 2.0;
            }
            else if (in4 && !in2)
            {
              y_left=Y2;
              x_left=other(y_left);
              y_right=Y1;
              x_right=other(y_right);
              //cout << "C" << endl;
              safe+= ( ( (x_left-X1)+(x_right-X1) ) * side ) / 2.0;
            }
            else if (in2 && in4)
            {
              y_left=Y2;
              x_left=other(y_left);
              x_right=X2;
              //cout << "D" << endl;
              y_right=other(x_right);
              safe+=side*(x_left-X1)+ ( ( side + (y_right-Y1) ) * (X2-x_left) )  / 2.0;
            }
            //printf("safe-> %.6lf\n",safe);
            

            alpha=atan2(y_left,x_left);
            beta=atan2(y_right,x_right);
            //printf("alpha %.6lf beta %.6lf\n",alpha,beta);
            safe+=((alpha-beta)*in_r*in_r)/2.0 - (in_r*in_r*sin(alpha-beta))/2.0;
            
          }
                
                
        }
      }
    }
    ans=(total-safe)/total;
    //printf("safe=%.6lf\n",safe);
    printf("Case #%d: %.6lf\n",test,ans);
  }
  return 0;
}
