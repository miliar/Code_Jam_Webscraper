#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>

using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VII;
typedef vector<string> VS;

#define ABS(x) ((x)<0? -(x):(x))
#define ALL(x) x.begin(),x.end()
#define SIZE(x)  int((x).size())
#define PB push_back
#define REP( a, b ) for ( int a = 0; a < b; a++ )
#define TR(x,it)  for(typeof((x).begin()) it=(x).begin(); it!=(x).end(); it++)

string getnum( string line )
{

  string n = line;
  sort( ALL(n) );
  string rn = n;
  //cout << "n " << n << endl;

  reverse( ALL(rn) );
  //cout << "line " << line << endl;
  //cout << "rn " << rn << endl;
  //cout << "n " << n << endl;

  if ( rn == line ) {
    //int c = 0;
    //REP( i, SIZE(n) ) {
    //  if ( n[i] != '0') {
    //	c++ ;
    //  }
    //}
    //if ( c == 1 ) return rn.substr(0,1) + "0" + rn.substr(1);
    //return ;
    string ret = n.substr(0,1) + "0" + n.substr(1);
    if ( ret[0] == '0' ) {
      int p = -1;
      REP( i, SIZE(ret) ) {
	if ( ret[i] != '0') {
	  p = i;
	  break;
	}
      }
      string tmp = ret.substr(0,p) + ret.substr(p+1,SIZE(ret));
      sort(ALL(tmp));
      return ret[p] + tmp;

    } else return ret;


  } else {
    next_permutation( ALL(line) );
    return line;
  }

}

int main( int argc, char *argv[] )
{
  FILE *fp;
  int N;

  fp = fopen( argv[1], "r" );
  fscanf( fp, "%d\n", &N );
  {
    for ( int i = 1; i <= N; i ++ ) {
      char buff[1000];
      //fgets( buff,1000,fp );
      //string line = string(buff);
      int tmp;
      fscanf( fp, "%d\n", &tmp );
      sprintf(buff,"%d",tmp);
      string line = string(buff);
      string a = getnum( line );
      //cout << a << endl;
      printf("Case #%d: %d\n", i, atoi(a.c_str()) );
    }
  }
  fclose(fp);
  return 0;
}


// Powered by FileEdit
// Powered by TZTester 1.01 [25-Feb-2003]
// Powered by CodeProcessor
