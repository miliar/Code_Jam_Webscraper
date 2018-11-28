#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <cstring>
#include <queue>
#include <sstream>
#include <cmath>

using namespace std;

typedef long long ll;
typedef vector <int> vi;
typedef pair<int, int> pii;

const double eps = 1e-7;

int T;

int c, d;

int x[1000100];

int n;

double y[10001000];
double r[1000];

bool f(double t)
{
  double p = -1e15;
  for (int i = 0; i < n; ++i)
  {
  	p = max( p + d, x[i] - t );
  	if (fabs(p - x[i]) > t + eps)
  		return false;	
  }
  return true;
}

int main()
{
  scanf("%d", &T);
  for (int t = 0; t < T; ++t)
  {
    n = 0;
    scanf("%d %d", &c, &d);
    for (int i = 0; i < c; ++i)
    {
    	int xx;
    	int k;
    	scanf("%d %d", &xx, &k);
    	for (int j = 0; j < k; ++j)
    		x[n++] = xx;
    }
    double A = 0.0;
    double B = 100000100000000.0;
    while (fabs(A - B) > 0.01)
    {
    	double C = (A + B)*0.5;
    	if ( f(C) )
    		B = C;
    	else
    		A = C;
    }
  	printf("Case #%d: %.1f\n", t+1, (A + B)*0.5);
  }
  return 0;
}