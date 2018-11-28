
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <math.h>
#include <sstream>
#include <cmath>

using namespace std;


#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define forit(i, a) for (__typeof((a).begin()) i = (a).begin(); i != (a).end(); i++)
#define fi(n) forn(i,n)
#define fj(n) forn(j,n)
#define fk(n) forn(k,n)
#define sz .size()
#define mp make_pair
#define pb push_back
#define all(v) (v).begin(), (v).end()
#define MIN(a,b) if(a>(b)) a=(b)
#define MAX(a,b) if(a<(b)) a=(b)
#define last(a) int(a.size() - 1)

int case_number = 0;
#define gout case_number++, printf("Case #%d: ",case_number), cout

#define fs first
#define sc second


typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vii;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef map<string,int> msi;


const long double eps = 1e-9;
const int inf = (1 << 30) - 1;
const ll inf64 = ((ll)1 << 62) - 1;
const long double pi = 3.1415926535897932384626433832795;


int ni() { int a; scanf( "%d", &a ); return a; }
double nf() { double a; scanf( "%lf", &a ); return a; }
char sbuf[100005]; string ns() { scanf( "%s", sbuf ); return sbuf; }
long long nll() { long long a; scanf( "%lld", &a ); return a; }



int main( )
{
	int T;

  cin >> T;
  while( T--){
    vector<string> s(4);
    fi(4){
      cin >> s[i];
    }

    int nt= 0, nx = 0, no= 0, np = 0;
    int flag = 0;
    fi(4){
      nt = 0;
      nx = 0;
      no = 0;

      fj(4){

        if(s[i][j] == 'O') no++;
        if(s[i][j] == 'X') nx++;
        if(s[i][j] == 'T') nt++;
        if(s[i][j] == '.') np++;



      }
      if (no + nt == 4){
      	flag = 1;
        break;
      }
      if (nx + nt == 4){
        flag = 2;
        break;
      }
    }
    if (flag == 1){
    	gout << "O won" << endl;
      continue;
    }
    if (flag == 2){
      gout << "X won" << endl;
      continue;
    }

    fi(4){
      nt = 0;
      nx = 0;
      no = 0;

      fj(4){

        if(s[j][i] == 'O') no++;
        if(s[j][i] == 'X') nx++;
        if(s[j][i] == 'T') nt++;


      }
      if (no + nt == 4){
      	flag = 1;
        break;
      }
      if (nx + nt == 4){
        flag = 2;
        break;
      }
    }
    if (flag == 1){
    	gout << "O won" << endl;
      continue;
    }
    if (flag == 2){
      gout << "X won" << endl;
      continue;
    }

      nt = 0;
      nx = 0;
      no = 0;

      fj(4){

        if(s[j][j] == 'O') no++;
        if(s[j][j] == 'X') nx++;
        if(s[j][j] == 'T') nt++;


      }
      if (no + nt == 4){
      	gout << "O won" << endl;
        continue;
      }
      if (nx + nt == 4){
        gout << "X won" << endl;
        continue;
      }

      
      nt = 0;
      nx = 0;
      no = 0;

      fj(4){

        if(s[j][3-j] == 'O') no++;
        if(s[j][3-j] == 'X') nx++;
        if(s[j][3-j] == 'T') nt++;

      }
      if (no + nt == 4){
      	gout << "O won" << endl;
        continue;
      }
      if (nx + nt == 4){
        gout << "X won" << endl;
        continue;
      }

      if ( np > 0) {
        gout << "Game has not completed" << endl;
      }
      else{
        gout << "Draw" << endl;
      }
    
	  }

	return 0;
}
