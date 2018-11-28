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

string s = "welcome to code jam";
int memo[20][10000];

int getnum( string line, int kpos, int lpos )
{
  if ( lpos >= line.size() ) return 0;

  int &res = memo[kpos][lpos];
  if ( res != -1 ) return res;

  res = 0;
  if ( s[kpos] == line[lpos] ) {
    if ( kpos + 1 == s.size() ) res += 1;
    else res += getnum( line, kpos + 1, lpos + 1 )%10000;
  }
  res += getnum( line, kpos, lpos + 1 )%10000;

  return res%10000;
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
      //fscanf( fp, "%[^\n]", buff );
      fgets( buff,1000,fp );
      string line = string(buff);
      memset( memo, -1, sizeof(memo) );
      printf("Case #%d: %04d\n", i, getnum( line, 0, 0 ) );
    }
  }
  fclose(fp);
  return 0;
}


// Powered by FileEdit
// Powered by TZTester 1.01 [25-Feb-2003]
// Powered by CodeProcessor
