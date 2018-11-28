#include <cstdio>
#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <map>
#include <vector>
#include <queue>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi; 
typedef pair<int,int> ii; 
typedef vector<ii> vii;
typedef vector<vii> vvii;

#define FOR(i, x) for (int i = 0; i < x; i++)
#define FORI(i,a, x) for (int i = a; i < x; i++)
#define ALL(x) (x).begin(), (x).end()
#define FORE(i, x) for (__typeof__((x).begin()) i = (x).begin(); i != (x).end(); i++)
#define SZ(x) ((int) (x).size())
#define EPS 1E-9
#define INF 0x3F3F3F3f
#define D(x) cout<<__LINE__<<"  "#x" is "<<x<<endl
#define DV(mat,n) FOR(imprimir,n)cout<<mat[imprimir]<<" ";cout<<endl;
#define DM(mat,rows,cols) FOR(i,rows){FOR(j,cols)cout<<mat[i][j]<<" ";cout<<endl;}

int cmp(double x, double y = 0, double tol = EPS) {
   return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1;
}

bool cmp_eq(double x, double y) { return cmp(x, y) == 0; }
bool cmp_lt(double x, double y) { return cmp(x, y) < 0; }

#define MAX 500

double f[MAX+1][3], v[MAX+1][3];

int main()
{
   freopen("in/B-large.in","r",stdin);
   freopen("out/B-large.out","w",stdout);   
   
   int T, F;
   bool zeros;
   double m11[3],m12[3];
   double m21[3],m22[3];
   
   scanf("%d",&T);
   
   FOR(t,T)
   {
      scanf("%d",&F);
      FOR(i,F)
      {
         scanf("%lf%lf%lf%lf%lf%lf",&f[i][0],&f[i][1],&f[i][2],&v[i][0],&v[i][1],&v[i][2]);
         //printf("%lf %lf %lf %lf %lf %lf\n",f[i][0],f[i][1],f[i][2],v[i][0],v[i][1],v[i][2]);
      }
      
      zeros = true;
      m11[0] = m11[1] = m11[2] = 0.0;
      m21[0] = m21[1] = m21[2] = 0.0;
      FOR(i,F)
      {
         FOR(j,3)
         {
            m11[j] += f[i][j];
            //D(m11[j]);
            m21[j] += v[i][j];
            if(!cmp_eq(v[i][j],0.0)) zeros =  false;
         }
      }
      
      FOR(j,3)
      {
         m12[j] = m11[j] * m11[j];
         m22[j] = m21[j] * m21[j];
      }
      
      double tm = 0.0, tm2 = 0.0, tm3 = 0.0, dm;
      
      if(zeros) tm3 = 0.0;
      else
      {
         FOR(i,3)
         {
            //cout << m11[i] << " * " << m21[i] << " = " << (m11[i] * m21[i]) << endl;
            tm += m11[i] * m21[i];
            tm2 += m22[i];
         }
         tm *= -1.0;
         //D(tm); D(tm2);
         if(cmp_eq(tm2,0.0)) tm3 = 0.0;
         else tm3 = tm/tm2;
      }
      
      double r[3];
      r[0] = r[1] = r[2] = 0.0;
      if(cmp_lt(tm3,0.0)) tm3 = 0.0;
      if(cmp_eq(tm3,-0.0)) tm3 = 0.0;
      
      FOR(i,F)
      {
         FOR(j,3)
         {
            r[j] += f[i][j] + v[i][j] * tm3;
         }
      }
      dm = 0.0;
      FOR(j,3) { r[j] /= (F * 1.0); dm += r[j] * r[j]; }
      
      
      printf("Case #%d: %.8lf %.8lf\n",t+1,sqrt(dm),tm3);
   }
   
   return 0;
}
