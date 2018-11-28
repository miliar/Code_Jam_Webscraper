#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <list>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>
using namespace std;

#define FOR(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define GETI(i) { string _s; getline(cin, _s); i = atoi(_s.c_str()); }
#define GETDI(i, d) { string _s; getline(cin, _s, d); i = atoi(_s.c_str()); }

//----------------------------------------------------------------------------
void calculate(int p, int t, int &sum_greater, int &sum_maybe)
{
  int max_n(-1);
  int max_S(-1);
  switch (t%3)
  {    
    case 0:
      max_n = t/3;
      if (t >= 3 && t <= 27) max_S = t/3 + 1;
      break;
    case 1:
      max_n = t/3 + 1;
      if (t >= 4 && t <= 28) max_S = t/3 + 1;
      break;
    case 2:
      max_n = t/3 + 1;
      if (t >= 2 && t <= 26) max_S = t/3 + 2;
      break;
  }
  if (max_n >= p)
  {
    ++sum_greater;
  }
  else
  {
    if (max_S >= p)
    {
      ++sum_maybe;
    }
  }
}

//----------------------------------------------------------------------------
int main() {
  freopen("B-large-0.in", "rt", stdin);
  freopen("B-large-0.out", "wt", stdout);

  int result;

  int T;
  GETI(T);
  FOR(TestCase, 1, T) {
    result = 0;
    int N, S, p, t;
    int sum_greater(0), sum_maybe(0);

    GETDI(N,' ');
    GETDI(S,' ');
    GETDI(p,' ');
    //cout << "N=" << N << " S=" << S << " p=" << p;
    FOR(ti, 1, N-1)
    {
      GETDI(t,' ');
      //cout << " t" << ti << "=" << t;
      calculate(p, t, sum_greater, sum_maybe);
    }
    GETI(t);
    //cout << " t" << N << "=" << t << endl;
    calculate(p, t, sum_greater, sum_maybe);

    //cout << "sum_greater=" << sum_greater << " sum_maybe=" << sum_maybe << endl;
    
    result = sum_greater;

    if (sum_maybe >= S) 
      result += S;
    else
      result += sum_maybe;

    cout << "Case #" << TestCase << ": " << result << endl;
  }

  return EXIT_SUCCESS;
}

