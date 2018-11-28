#include <iostream>
#include <sstream>
#include <cctype>
#include <utility>
#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std ;

typedef vector < long long > VLL ;

#define F first
#define S second
#define PB push_back
#define SIZE(x) (int)x.size()
#define MP(a,b) make_pair(a,b)
#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,s,e) for(int i=(s);i<=(e);++i)
#define REPEACH(it,x) for(typeof((x).begin()) it=(x).begin();it!=(x).end();++it)

int n ;
long long sum ;
VLL a, b ;

void calc_s()
{
    sort(a.begin(), a.end()) ;
    sort(b.begin(), b.end(),greater<long long>()) ;
    sum = 0 ;
    REP(i,n)
      sum += a[i] * b[i] ;
}

void getinput()
{
    int temp ;
    a.clear() ;
    b.clear() ;
    cin >> n ;
    REP(i,n)
    {
	cin >> temp ;
	a.PB(temp) ;
    }
    REP(i,n)
    {
	cin >> temp ;
	b.PB(temp) ;
    }
}

int main()
{
    int ncase ;
    
    cin >> ncase ;
    //    printf("ncase %d\n", ncase) ;
    FOR(icase,1,ncase)
    {
	getinput() ;
	calc_s() ;
	printf("Case #%d: %Ld\n", icase, sum) ;
    }
}

