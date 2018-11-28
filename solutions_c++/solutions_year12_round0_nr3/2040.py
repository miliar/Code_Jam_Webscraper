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
int main() {
  freopen("C-large-0.in", "rt", stdin);
  freopen("C-large-0.out", "wt", stdout);

  int T;
  long v_A[60];
  long v_B[60];
  long v_result[60];

  GETI(T);
  FOR(TestCase, 1, T) {
    long A, B;
    GETDI(A,' ');
    GETI(B);
    //cout << "A=" << A << " B=" << B << endl;
    v_A[TestCase] = A;
    v_B[TestCase] = B;
    v_result[TestCase] = 0;
  }

  long A(1);
  long B(2000000);
  FOR(n, A, B) 
  {
    // n as string = s_n
    stringstream ss_n;
    ss_n << n;
    string s_n;
    ss_n >> s_n;

    // l is the cycle count
    int l(ss_n.str().length());
    --l;

    // v_m is the result vector, v_m_s is the size of it
    long v_m[8];
    int v_m_s(0);

    FOR(i, 1, l)
    {
      // recycle
      s_n += s_n[0];
      s_n.erase(0,1);

      // m is the recycled n
      stringstream ss_m;
      ss_m << s_n;
      long m;
      ss_m >> m;

      if (m <= B && m > n)
      {
        bool found(false);
        FOR(j, 0, v_m_s-1)
        {
          if (v_m[j] == m)
          {
            found = true;
            break;
          }
        }
        if (!found)
        {
          //cout << "(" << n << "," << m << ")" << endl;
          v_m[v_m_s++] = m;
          FOR(TestCase, 1, T) {
            if (n >= v_A[TestCase] && m <= v_B[TestCase])
            {
              ++v_result[TestCase];
            }
          }
        }
      }
    }
  }

  FOR(TestCase, 1, T) 
  {
    cout << "Case #" << TestCase << ": " << v_result[TestCase] << endl;
  }

  return EXIT_SUCCESS;
}

