#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cfloat>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <functional>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

//#define NDEBUG
#ifdef NDEBUG
#define DEBUG if (false)
#else
#define DEBUG if (true)
#endif

#pragma GCC diagnostic warning "-Wall"
#define WRITE(x) DEBUG { cout << x << endl; }
#define WATCH(x) DEBUG { cout << #x << " = " << x << endl; }
#define ALL(x) (x).begin(), (x).end()
#define FORN(i, a, b) for(typeof(b) i = (a); i < (b); i++)
#define FOREACH(i, c) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)

void go(const vector<string> & field)
{

  bool owins = false;
  bool xwins = false;
  FORN(i, 0, 4) {
    bool owinsv = true, owinsh = true;
    bool xwinsv = true, xwinsh = true;
    FORN(j, 0, 4) {
      owinsv &= field[i][j] == 'O' or field[i][j] == 'T';
      owinsh &= field[j][i] == 'O' or field[j][i] == 'T';

      xwinsv &= field[i][j] == 'X' or field[i][j] == 'T';
      xwinsh &= field[j][i] == 'X' or field[j][i] == 'T';
    }
    owins |= owinsv;
    owins |= owinsh;
    xwins |= xwinsh;
    xwins |= xwinsv;
  }

  bool xwinsd1 = true, xwinsd2 = true;
  bool owinsd1 = true, owinsd2 = true;
  FORN(i, 0, 4) {
    xwinsd1 &= field[i][i] == 'X' or field[i][i] == 'T';
    owinsd1 &= field[i][i] == 'O' or field[i][i] == 'T';
    int ii = i, jj = 3 - i;
    xwinsd2 &= field[ii][jj] == 'X' or field[ii][jj] == 'T';
    owinsd2 &= field[ii][jj] == 'O' or field[ii][jj] == 'T';
  }

  owins |= owinsd1;
  owins |= owinsd2;
  xwins |= xwinsd1;
  xwins |= xwinsd2; 

  bool empty_cells = false;
  FORN(i, 0, 4) FORN(j, 0, 4) empty_cells |= field[i][j] == '.';

  if (owins) 
    cout << "O won" << endl;
  else if (xwins)
    cout << "X won" << endl;
  else if (not empty_cells)
    cout << "Draw" << endl;
  else 
    cout << "Game has not completed" << endl;
  

}

int main(){
	//Descomente para acelerar cin
	//ios::sync_with_stdio(false);
	
	int ntc;
	string temp;
	cin >> ntc;
	getline(cin, temp);
	FORN(tc, 1, ntc + 1) {
	  vector<string> field(4);
	  FORN(i, 0, 4) getline(cin, field[i]);
	  getline(cin, temp);
    cout << "Case #" << tc << ": ";
	  go(field);
  }
}
