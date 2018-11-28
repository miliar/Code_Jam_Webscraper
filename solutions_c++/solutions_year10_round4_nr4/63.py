#include "stdio.h"
#include "stdlib.h"
#include "string.h"
#include <vector>
#include <string>
#include <iostream>
#include <cmath>
#include <cctype>
#include <sstream>
#include <algorithm>
#include <iomanip>
#include <set>
#include <queue>

using namespace std;

typedef long double real;
typedef long long TT;

#define PB push_back
#define SQR(x) ((x)*(x))
#define PII pair<int, int>
#define VPII vector<pair<int, int> >
#define VI vector<int>
#define VVI vector<VI >
#define VS vector<string>
#define VTT vector<TT>
#define VR vector<real>
#define A first
#define B second

VPII p, q;

double dist(double x1, double y1, double x2, double y2)
{
   return sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1));
}

double calcs(double r1, double r2, double d)
{
   double cosg = (r1*r1 - r2*r2 + d*d) / (2*r1*d);
   if (cosg < -1) cosg = -1;
   if (cosg > 1) cosg = 1;
   double alfa = 2 * acos(cosg);
   return 0.5*r1*r1*alfa - 0.5*r1*r1*sin(alfa);
}

int main()
{
   freopen("input.txt" ,"rt", stdin); freopen("output.txt", "wt", stdout);
   
   int T, sc;
   cin >> T;
   for (sc = 0; sc < T; sc++) {
      p.clear(); q.clear();
      int i, j, k, n, m;
      cin >> n >> m;
      for (i = 0; i < n; i++) {
         cin >> j >> k; p.PB(make_pair(j, k));
      }
      for (i = 0; i < m; i++) {
         cin >> j >> k; q.PB(make_pair(j, k));
      }
      
      cout << "Case #" << sc+1 << ": ";
      
      for (i = 0; i < m; i++) {
         double d = dist(p[0].A, p[0].B, p[1].A, p[1].B);
         double r1 = dist(p[0].A, p[0].B, q[i].A, q[i].B);
         double r2 = dist(p[1].A, p[1].B, q[i].A, q[i].B);
         
         double s1 = calcs(r1, r2, d);
         double s2 = calcs(r2, r1, d);
         cout << fixed << setprecision(7) << s1 + s2 << " ";
      }
      
      cout << endl;
   }
   

   fclose(stdin); fclose(stdout);
   return 0;   
}