#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>

#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cmath>


using namespace std;
const int MAXN = 99999;
double errorProb[MAXN+10][2];
double P[MAXN];
void doit(int n)
{
   for(int i = 1; i <= MAXN; i++) {
      errorProb[i][0] = errorProb[i][1] = 0.0;
   }
//cerr<<errorProb[2][0]<<endl;

   errorProb[1][0] = P[1];
   errorProb[1][1] = (1.0-P[1]);

   for(int i = 2; i <= n; i++) {
      //if ith contains error
      errorProb[i][1] += (1.0-P[i]) * (errorProb[i-1][0] + errorProb[i-1][1]);
      //if ith contains no error
      errorProb[i][1] += P[i] * errorProb[i-1][1];

      errorProb[i][0] += P[i] * errorProb[i-1][0];
   }


}
const double EPS = 0.000001;
double minm(double a, double b)
{
      if(fabs(a-b)<=EPS) {
         return a;
      }
      if(a < b) return a;
      return b;
}

double option1(int A, int B)
{
   //correct first attempt
   double ret = errorProb[A][0] * (B-A+1);
   ret += (errorProb[A][1]) * ((B-A+1)+B+1);
  // cerr<<ret<<endl;
   return ret;

}

double option2(int A, int B)
{
   double ret = (errorProb[A][0]+errorProb[A][1])*(A+B+1);
 //  cerr<<ret<<endl;
   for(int back = 1; back < A; back++) {
      if(back==A) {

      }
      else {
         double cur = errorProb[A-back][0]*(B-(A-back)+2) + errorProb[A-back][1]*(B-(A-back)+2 + B+1);
       //  cerr<<cur<<endl;
         ret = minm(ret,cur);
      }
   }
   return ret;
}

double option3(int A, int B)
{
   return (errorProb[A][0] + errorProb[A][1]) * (1 + B + 1);
}

double solve(int A, int B)
{
   double a = option1(A,B), b = option2(A,B), c = option3(A,B);
   //cout<<a<<" "<<b<<" "<<c<<endl;
 //  cerr<<c<<endl;
   double ret = minm(a,minm(b,c));
   return ret;

}

int main()
{
   freopen("A-small-attempt1.in","r",stdin);
   freopen("A1.out","w",stdout);

   int A, B;
   int T;
   //scanf("%d",&T);
   cin>>T;
   for(int tc = 1; tc <= T; tc++) {
     // scanf("%d %d",&A,&B);
     cin>>A>>B;
      for(int i = 1; i <= A; i++) cin>>P[i];
      doit(A);

      double ret = solve(A,B);

      printf("Case #%d: %.6f\n",tc,ret);

   }
   return 0;
}
