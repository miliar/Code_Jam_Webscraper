#pragma warning(disable:4786)

#include <iostream>
#include <cmath>
#include <cassert>
#include <string>
#include <numeric>
#include <cstdlib>
#include <algorithm>
#include <cstring>
#include <map>
#include <set>
#include <queue>
#include <vector>
#include <cstdio>
#include <ctime>

using namespace std;

typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;

#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define Ford(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define Rep(i,n) for (int i(0),_n(n); i < _n; ++i)
#define Repd(i,n) for (int i((n)-1); i >= 0; --i)
#define Fill(a,c) memset(&a, c, sizeof(a))
#define Mp(x, y) make_pair((x), (y))
#define B(a) (a).begin()
#define E(a) (a).end()

vector<string> aToken;

void toknize(char *p, char *del){
  aToken.clear();
  char *tok = strtok(p,del);
  if(tok != NULL) aToken.push_back( tok );  
  
  while( tok != NULL )  {
    tok = strtok( 0 , del);
    if(tok != NULL)  aToken.push_back( tok );
  }
}

void main()
{
	int nc;
	int num;

  cin >> nc;
  
  Rep( i, nc)
  {
    cin >> num;

    vi a, b;
     
    Rep( j, num*2)
    {
      int elem;
      cin >> elem;
      if( j < num) a.push_back(elem) ;
      else b.push_back(elem);
    }

    sort(a.begin(), a.end());
    sort(b.begin(), b.end());

    int r=0;
    for( j=0 ; j< num; j++)
    {
      r+= (a[j]*b[num-j-1]);
    }

    cout << "Case #" << i+1 <<": "<<r<<endl;
  }

}
