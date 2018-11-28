#include<iostream>
#include<cmath>

using namespace std;

struct el
{
   int x, y, z;
   int xi, yi, zi;

void read()
{
   scanf("%d%d%d%d%d%d",&x,&y,&z,&xi,&yi,&zi);
}
};

    el p[10000];
    int n;
   
    double xsum, xisum;
   double ysum, yisum;
   double zsum, zisum;

void input()
{
    scanf("%d", &n);
    for( int i = 0; i < n; ++i )p[i].read();
}

double func(double t)
{
   double X, Y, Z;
   X = (xsum + xisum*t)/n;
   Y = (ysum + yisum*t)/n;
   Z = (zsum + zisum*t)/n;
return sqrt(X*X + Y*Y + Z*Z);
}
void solve()
{
   input();
   xsum = 0; xisum = 0; ysum = 0; yisum = 0; zsum = 0; zisum = 0;

   for( int i = 0; i < n; ++i )
   {
    xsum += p[i].x; xisum += p[i].xi;
    ysum += p[i].y; yisum += p[i].yi;
    zsum += p[i].z; zisum += p[i].zi;
   }

   //printf("%lf %lf\n%lf %lf\n%lf %lf\n",xsum,xisum,ysum,yisum,zsum,zisum);

   double t1, t2, t3;

   if(xisum!=0)t1 = (-1.0*xsum)/xisum;
   else t1 =0;

   if(yisum!=0)t2 = (-1.0*ysum)/yisum;
   else t2 = 0;

   if(zisum!=0)t3 = (-1.0*zsum)/zisum;
   else t3 = 0;

   double left = 1e100;
   double right = 1e100;
   right = 0;

   if(left > t1)left = t1;
   if(left > t2)left = t2;
   if(left > t3)left = t3;

   if(right < t1)right = t1;
   if(right < t2)right = t2;
   if(right < t3)right = t3;

   int i;
  
   double mid, mid2;

   if(left < 0)left = 0;
   if(right < 0)right = 0;


   for( i = 0; i < 10000; ++i )
   {
     mid = left + (right - left)/3.0;
     mid2 = left + ((right - left)*2.0)/3.0;

     double f1, f2;
     f1 = func(mid);
     f2 = func(mid2);

     //cout<<"left i right "<<left<<" "<<right<<"\n";
     //cout<<mid<<" "<<mid2<<" "<<f1<<" "<<f2<<"\n";
     if(f1 < f2)right = mid2;
     else left = mid;
   }   
 //  printf("%lf %lf %lf %lf\n",t1,t2,t3,(t1+t2+t3)/3.0);
   printf("%.6lf %.6lf\n",func((left+right)/2.0), (left+right)/2.0);
}
int main()
{
    int t;
    scanf("%d", &t);
    for(int i = 1; i <= t; ++i)
    {
     printf("Case #%d: ",i);
     solve();
    }
return 0;
}
