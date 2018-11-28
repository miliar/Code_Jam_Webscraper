#pragma comment(linker,"/STACK:100000000")  

#include <cstdio>
#include <cmath>
#include <string>
#include <iostream>
#include <vector>
#include <sstream>
#include <iostream>
#include <map>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

#define PI 3.1415926535897932384626433832795

int n, tn, nt;
int G[55][55];

char s[55];

struct circle
{
   double x, y, r;
   circle(double x=0, double y=0, double r=0):x(x), y(y), r(r){}
} c[55];

vector <circle> to_check;

double get(double x, double y, vector <circle> &v)
{
   double res=0;
   for (int i=0; i<(int)v.size(); i++)
   {
      double t=hypot(x-v[i].x, y-v[i].y)+v[i].r;
      if (t>res) res=t;
   }
   return res;
}

inline void run(vector <circle> &v)
{
   if (v.size()==1)
     to_check.push_back(v[0]);
   if (v.size()==2)
   {
      double l=0.0, r=1.0, m1, m2, nx1, ny1, nv1, nx2, ny2, nv2;
      while (r-l>1e-9)
      {
         m1=(r+l+l)/3;
         nx1=v[0].x*(1.0-m1)+v[1].x*m1, ny1=v[0].y*(1.0-m1)+v[1].y*m1;
         nv1=get(nx1, ny1, v);
         m2=(r+r+l)/3;
         nx2=v[0].x*(1.0-m2)+v[1].x*m2, ny2=v[0].y*(1.0-m2)+v[1].y*m2;
         nv2=get(nx2, ny2, v);
         if (nv1>nv2) l=m1;
         else r=m2;
      }
      to_check.push_back(circle(nx1, ny1, get(nx1, ny1, v)));
   }
}

int main(void)
{
   int i, j, k, l;
   freopen("D-small-attempt0.in", "r", stdin);
   freopen("D-small-attempt0.out", "w", stdout);
   //freopen("D-large.in", "r", stdin);
   //freopen("D-large.out", "w", stdout);

   scanf("%d\n", &nt);
   for (tn=0; tn<nt; tn++)
   {
      fprintf(stderr, "Case #%d: \n", tn+1);
      scanf("%d\n", &n);

      to_check.clear();

      for (i=0; i<n; i++)
      {
         int x, y, r;
         scanf("%d%d%d", &x, &y, &r);
         c[i]=circle(x, y, r);
      }

      vector <circle> v;
      for (i=0; i<n; i++)
      {
         v.clear();
         v.push_back(c[i]);
         run(v);
      }

      for (i=0; i<n; i++)
         for (j=i+1; j<n; j++)
         {
            v.clear();
            v.push_back(c[i]);
            v.push_back(c[j]);
            run(v);
         }

      double ans=1e10;
      for (i=0; i<(int)to_check.size(); i++)
         for (j=0; j<(int)to_check.size(); j++)
         {
            circle s1=to_check[i], s2=to_check[j];
            double r=max(s1.r, s2.r);
            int good=1;
            for (k=0; k<n; k++)
               if (hypot(s1.x-c[k].x, s1.y-c[k].y)+c[k].r>r+1e-9 && 
                   hypot(s2.x-c[k].x, s2.y-c[k].y)+c[k].r>r+1e-9) good=0;
            if (good && r<ans)
               ans=r;
         }

      printf("Case #%d: ", tn+1);
      printf("%.20lf", ans);
      printf("\n");
   }
   return 0;
}
