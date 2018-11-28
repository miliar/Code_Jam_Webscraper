#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define REP(i, n) for(int i=0;i<int(n);i++)
#define FOR(i, a, b) for(int i=(a);i<int(b);i++)
#define RFOR(i, b, a) for(int i=(b);i>int(a);i--)
#define foreach(it, c)  for(typeof((c).begin()) it = (c).begin();it!=(c).end();++it)
#define ALL(x)   (x).begin(),(x).end()
#define SORT(x) sort(ALL(x))
#define VI vector<int>
#define VS vector<string>
#define PB push_back
#define ISS istringstream
#define OSS ostringstream
#define SIZE(X) ((int)(X.size()))
#define LENGTH(X) ((int)(X.length()))
#define MP(X,Y) make_pair(X,Y)

#define ll long long
const double pi=acos(-1.0);
const double eps=1e-11;
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}
template<class T> inline int countbit(T n){return (n==0)?0:(1+countbit(n&(n-1)));}





int main()
{
	int i,j ,k;
	int casos; cin >> casos;
	for( int h = 0 ; h < casos; h ++ )
	{
	       int N; cin >> N;
	       int val[41];
	       for( i = 0 ; i < N ; i ++ )
	       {
		      string s; cin >> s;
		      val[i] = -1;
		      for( j = 0 ; j < s.size(); j ++ ) if( s[j] == '1' ) val[i] = j;
	       }
	       int res = 0 ;
	       for( i = 0 ; i  < N ; i ++ )
	       {
		      for( j = i; j < N; j ++ )
		      {
			     if( val[j] <= i )
			     {
				    int a = val[j];
				    for( k = j; k > i; k -- ) val[k] = val[k-1];
				    val[i] = a;
				    res += j-i;
				    break;
			     }
		      }
	       }
	       cout << "Case #" << (h+1) << ": " << res << endl;
	}return 0;
}











