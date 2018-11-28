#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <stack>
#include <queue>
#include <numeric>
#include <iterator>
#include <exception>

using namespace std;

//----- Start Includes -----
// END CUT HERE
typedef vector<int> Vi;
typedef vector<string> Vs;
typedef vector<Vi> Mi;
#define forUp(x,y) for(int x=0;x<(y);x++)
#define forDown(x,y) for(int x=(y)-1;x>=0;x--)
// BEGIN CUT HERE
// ----- End Includes -----
int main() {
  std::set_terminate (__gnu_cxx::__verbose_terminate_handler);

  string s;
  int nCases;
  cin >> nCases; 
  forUp(caseNr, nCases) {
    int nEng,nQueries;
    cin >> nEng;
    Vs eng(nEng);
    getline(cin,s);
    forUp(i,nEng) getline(cin,eng[i]);
    cin >> nQueries;
    Vs queries(nQueries);
    getline(cin,s);
    forUp(i,nQueries) getline(cin,queries[i]);

    Mi T(nEng, Vi(nQueries+1)); // T[e][q] = min changes if at engine e before starting with query q.
    forUp(e,nEng) T[e][nQueries]=0;
    forDown(q,nQueries) forUp(e,nEng)
      if (queries[q] != eng[e])
        T[e][q] = T[e][q+1];
      else {
        T[e][q]=1000000;
        forUp(e2,nEng) if (e2 != e)
          T[e][q] = min(T[e][q], 1+T[e2][q+1]);
      }

    int res=10000;
    forUp(e,nEng) res = min(res, T[e][0]);
    cout << "Case #" << caseNr+1 <<": " << res << endl;
  }
  
  return 0;
}

// ----- Code Ends -----
