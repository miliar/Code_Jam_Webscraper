#include <iostream>
#include <sstream>
#include <cctype>
#include <utility>
#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std ;

typedef pair < int, int > PII ;
typedef vector < PII > VPII ;
typedef pair < string, int > PSI ;
typedef vector < PSI > VPSI ;
typedef vector < int > VI ;
typedef vector < VI >  VVI ;
typedef vector < double > VD ;
typedef vector < VD >  VVD ;
typedef vector < string > VS ;
typedef vector < VS >  VVS ;

#define F first
#define S second
#define PB push_back
#define SIZE(x) (int)x.size()
#define MP(a,b) make_pair(a,b)
#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,s,e) for(int i=(s);i<=(e);++i)
#define REPEACH(it,x) for(typeof((x).begin()) it=(x).begin();it!=(x).end();++it)


int p,k,l ;

VI num ;


void getinput()
{
    int a ;
    num.clear() ;
    cin >> p >> k >> l ;
    REP(i, l)
    {
	cin >> a ;
	num.PB(a) ;
    }
}

long long solve()
{
    long long keypress = 0 ;
    int count = 0 ;
    sort(num.begin(), num.end(), greater<int>()) ;
    REP(i,p)
    {
	int sum = 0 ;
	REP(j,k)
	{
	    sum += num[count] ;
	    count++ ;
	    if (count == SIZE(num))
		break ;
	}
	keypress += (long long) sum * (i + 1) ;
	if (count == SIZE(num))
	  return keypress ;
    }
    if (num[count] != 0)
      return -1 ;
    return keypress ;
}

int main()
{
    int ncase ;
    
    cin >> ncase ;
    //    printf("ncase %d\n", ncase) ;
    FOR(icase,1,ncase)
    {
	getinput() ;
	long long n = solve() ;
	if (n == -1)
	  printf("Case #%d: Impossible\n", icase) ;
	else
	  printf("Case #%d: %Ld\n", icase, n) ;
    }
}

