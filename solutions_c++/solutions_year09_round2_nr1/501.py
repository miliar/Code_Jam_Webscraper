#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <utility>
#include <set>
#include <map>
#include <string>
#include <memory.h>
#include <sstream>
using namespace std;

#define god_mode on
#define mp make_pair
#define pb push_back

typedef pair<int,int> pii;
typedef long long ll;
typedef long double ld;

double   toFloat( string s ) { istringstream ss(s); double a; ss>>a; return a; };

double ans;
int NL[100010], NR[100010];
double val[100010];
string name[100010];
string text, buf;
set<string> ss;
int it, knode, L, root;
char sb[100];

string nexttoken()
{
  while ( it < (int)text.size() && text[it] == ' ' ) it++;
  string res = "";
  while ( it < (int)text.size() && text[it] != ' ' )
  {
    if ( res.size() > 0 && ( text[it] == '(' || text[it] == ')' ) ) break;
    res.pb( text[it] );
    it++;
    if ( text[it-1] == '(' || text[it-1] == ')' ) break;
  }
//  printf( "nexttoken return: %s\n", res.c_str() );
  return res;
}

int readnode()
{
  int i = ++knode;
  nexttoken();
  val[i] = toFloat( nexttoken() );
  name[i] = nexttoken();
  if ( name[i] != ")" )
  {
    NL[i] = readnode();
    NR[i] = readnode();
    nexttoken();
  }
  else name[i] = "";
//  printf( "-> node %d read.\n", i );
  return i;
}

void go( int i )
{
  ans *= val[i];
  if ( name[i] != "" )
    if ( ss.find( name[i] ) != ss.end() ) go( NL[i] );
    else go( NR[i] );
}

int main()
{
//  freopen( "in.txt", "r", stdin );
  int t;
  cin >> t;
  for ( int tc=1; tc<=t; tc++ )
  {
    printf( "Case #%d:\n", tc );
    scanf( "%d\n", &L );
    text = "";
    for ( int i=0; i<L; i++ )
    {
      if ( i ) text.pb( ' ' );
      gets( sb );
      for ( int i=0; i<(int)strlen(sb); i++ )
        text.pb( sb[i] );
    }
    for ( int i=0; i<(int)text.size(); i++ )
      if ( text[i] < 32 ) text[i] = 32;

    it = 0;
    knode = 0;
    root = readnode();

    int n, k;
    cin >> n;
    for ( int i=0; i<n; i++ )
    {
      cin >> buf;
      cin >> k;
      ss.clear();
      ans = 1.0;
      for ( int i=0; i<k; i++ )
      {
        cin >> buf;
        ss.insert( buf );
      }
      go( root );
      printf( "%.7f\n", ans );
    }
  }
}