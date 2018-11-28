#include<iostream>
#include<sstream>
#include<cstdio>
#include<algorithm>
#include<string>
#include<vector>
#include<cmath>
#include<set>
#include<map>
#include<stack>
#include<queue>
#include<numeric>
#include<functional>
#include<complex>

using namespace std;

#define FOR(i,n)  for(int i=0;i<(int)(n);i++)
#define SZ(x) ((int)(x).size())
#define MP make_pair

typedef complex<double> cmp_t;
const double PI = 4.0*atan(1.0);
double outerProduct(cmp_t p, cmp_t q){ return imag(conj(p)*q); }
double area(vector<cmp_t>& pol)
{
  double val = 0.0;
  FOR(i,SZ(pol))
    {
      int ii = (i+1)%SZ(pol);
      val += outerProduct(pol[i] , pol[ii]);
    }
  return fabs(val)/2.0;
}

double solve(double f , double R , double t , double r , double g)
{
  long double sum = 0.0 , all ;
  all = PI * R * R / 4 ; 
  if(g < 0) return 1.0;
  
  long double x = r ; 
  long double RR = R-t;
  for(;x < R - t; x += 2*r + g)
    {
      double y = r ; 
      for(; ; y += 2*r + g)
        {
          // 4 3
          // 1 2
          cmp_t p1 = cmp_t(x,y);
          cmp_t p2 = cmp_t(x+g,y);
          cmp_t p3 = cmp_t(x+g,y+g);
          cmp_t p4 = cmp_t(x,y+g);
          int cnt = 0 ;
          bool b1,b2,b3,b4;
          b1=b2=b3=b4=false;
          if(abs(p1) <= R - t) {cnt++; b1=true;}
          if(abs(p2) <= R - t) {cnt++; b2=true;}
          if(abs(p3) <= R - t) {cnt++; b3=true;}
          if(abs(p4) <= R - t) {cnt++; b4=true;}
          if(cnt==0) break;
          if(cnt==4){
            sum += g*g;
          }
          bool a1,a2,a3,a4;
          a1=a2=a3=a4=false;
          vector<cmp_t> crs;
          if(b1!=b2){
            double tx = sqrt(max(RR*RR-y*y,0.0L));
            if(x<tx && tx<x+g) {
              crs.push_back(cmp_t(tx,y));
              a1=true;
            }
          }
          if(b2!=b3){
            double ty = sqrt(max(RR*RR-(x+g)*(x+g),0.0L));
            if(y<ty && ty<y+g){
              crs.push_back(cmp_t(x+g,ty));
              a2=true;
            }
          }
          if(b3!=b4){
            double tx = sqrt(max(RR*RR-(y+g)*(y+g),0.0L));
            if(x<tx && tx<x+g) {
              crs.push_back(cmp_t(tx,y+g));
              a3=true;
            }
          }
          if(b4!=b1){
            double ty = sqrt(max(RR*RR-x*x,0.0L));
            if(y<ty && ty<y+g){
              crs.push_back(cmp_t(x,ty));
              a4=true;
            }
          }
          if(crs.size()==2)
            {
              vector<cmp_t> pol;
              if(a1&&a4){
                pol.push_back(p1);
                pol.push_back(crs[0]);
                pol.push_back(crs[1]);
              }
              if(a2&&a3){
                pol.push_back(p1);
                pol.push_back(p2);
                pol.push_back(crs[0]);
                pol.push_back(crs[1]);
                pol.push_back(p4);
              }
              if(a2&&a4){
                pol.push_back(p1);
                pol.push_back(p2);
                pol.push_back(crs[0]);
                pol.push_back(crs[1]);
              }
              if(a1&&a3){
                pol.push_back(p1);
                pol.push_back(crs[0]);
                pol.push_back(crs[1]);
                pol.push_back(p4);
              }
              if(pol.size()==0) abort();
              sum += area(pol);
              double th = arg(crs[1])-arg(crs[0]);
              if(th > 2*PI) th -= 2*PI;
              if(th < 0) th += 2*PI;
              sum += th * RR * RR / 2.0;
              // triangle
              vector<cmp_t> pol2;
              pol2.push_back(cmp_t(0,0));
              pol2.push_back(crs[0]);
              pol2.push_back(crs[1]);
              sum -= area(pol2);
            }
        }
    }
  return 1.0 - sum / all ;
}

int main()
{
  int n , case_no=1; 
  cin>>n;
  while(n--)
    {
      double f , R , t , r , g ;
      cin>>f>>R>>t>>r>>g;
      g -= 2*f;
      t += f ; 
      r += f ;
      f = 0 ;
      printf("Case #%d: %0.9f\n" , case_no++ , solve(f, R , t , r , g));
    }
  return 0 ;
}
