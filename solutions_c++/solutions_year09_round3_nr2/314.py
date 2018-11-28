#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

double eps = 0.0000000001;

int main()
{
  
  long T;

  cin >>T;
  for( int ttt=1; ttt<=T; ++ttt )
    {
      int i;
      long N;
      cin >>N;
      vector<double> x(N);
      vector<double> y(N);
      vector<double> z(N);
      vector<double> vx(N);
      vector<double> vy(N);
      vector<double> vz(N);
      double A1=0;
      double B1=0;
      double A2=0;
      double B2=0;
      double A3=0;
      double B3=0;
      for(i = 0; i < N; ++i)
	{
	  cin >>x[i];
	  cin >>y[i];
	  cin >>z[i];
	  A1 += x[i];
	  A2 += y[i];
	  A3 += z[i];
	  cin >>vx[i];
	  cin >>vy[i];
	  cin >>vz[i];
	  B1 += vx[i];
	  B2 += vy[i];
	  B3 += vz[i];
	}
      A1 /= N;
      A2 /= N;
      A3 /= N;
      B1 /= N;
      B2 /= N;
      B3 /= N;
      double t,d;
      if( B1*B1 + B2*B2 + B3*B3 > eps )
	{
	  t = -(A1*B1+A2*B2+A3*B3)/(B1*B1 + B2*B2 + B3*B3);
	  if(t<0) t=0;
	  d = sqrt((A1+t*B1)*(A1+t*B1)+(A2+t*B2)*(A2+t*B2)+(A3+t*B3)*(A3+t*B3));
	}
      else
	{
	  t=0;
	  d = sqrt((A1+t*B1)*(A1+t*B1)+(A2+t*B2)*(A2+t*B2)+(A3+t*B3)*(A3+t*B3));
	}
      cout <<"Case #"<<ttt<<": ";
      cout <<setprecision(10)<<d<<" "<<t<<endl;
    }
}
