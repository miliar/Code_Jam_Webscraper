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

using namespace std;

typedef long long ll;
typedef vector <int> vi;
typedef pair<int, int> pii;
typedef pair <int, pii> piii;

int T;


piii mas[2000];
int x, s, r, t, n;

int main()
{
  scanf("%d", &T);
  for (int t1 = 0; t1 < T; ++t1)
  {
    scanf("%d %d %d %d %d", &x, &s, &r, &t, &n);
    int xx = x;
    for (int i = 0;i < n; ++i)
    {
      int w, b, e;
    	scanf("%d %d %d", &b, &e, &w);
    	mas[i] = piii(w, pii(b, e));
    	xx -= e - b;
    }
    //sort(mas, mas + n);
    mas[n] = piii(0, pii(0, xx));
    sort(mas, mas + n + 1);
    //reverse(mas, mas + n);
    double res = 0;;
    double tt = t;
    
    for (int i = 0; i < n + 1; ++i)
    {
      int d = mas[i].second.second - mas[i].second.first;
    	double a = min( tt, (double)d / (r + mas[i].first) );
    	double b = a + (d - (double)a*(r + mas[i].first))/(s + mas[i].first);
    	res += b;
    	tt -= a;
    }
    /*double a = min(tt, double(xx) / r );
    double b = a + ( xx - (double)a*r/s );
    res += b;*/
  	printf("Case #%d: %.7f\n", t1+1, res);
  }
  return 0;
}