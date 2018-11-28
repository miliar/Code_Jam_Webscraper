#include <iostream>
#include <sstream>
#include <cctype>
#include <utility>
#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std ;

typedef vector < int > VI ;
typedef vector < VI >  VVI ;
typedef vector < long long > VLL ;
typedef vector < VLL >  VVLL ;

#define F first
#define S second
#define PB push_back
#define SIZE(x) (int)x.size()
#define MP(a,b) make_pair(a,b)
#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,s,e) for(int i=(s);i<=(e);++i)
#define REPEACH(it,x) for(typeof((x).begin()) it=(x).begin();it!=(x).end();++it)

int numlen ;
long long cnt ;

char str[50] ; 

void getinput()
{
    gets(str) ;
    numlen = strlen(str) ;
//     printf("%s %d\n", str, numlen) ;
}

void calc_ugly(VLL &num)
{
    long long sum = 0 ;
    REP(i, SIZE(num))
    {
	sum += num[i] ;
    }
    //    if (sum == 0) return ;
    if (sum % 2 == 0) cnt++ ;
    else if (sum % 3 == 0) cnt++ ;
    else if (sum % 5 == 0) cnt++ ;
    else if (sum % 7 == 0) cnt++ ;
//     printf("sum %Ld %d \n", sum, cnt) ;
}

void solve(int pos, VLL &num)
{
//     printf("%d ", pos) ;
//     REP(i, SIZE(num))
//     {
// 	printf("%Ld ",num[i]) ;
//     }
//     printf("\n") ;
    if (pos == numlen)
    {
      calc_ugly(num) ;
      return ;
    }
    FOR(i, 1, numlen - pos)
    {
	char a[50] ;
	strncpy(a, &str[pos], i) ;
	a[i] = '\0' ;
// 	printf("--- %d %s\n", SIZE(num), a) ;
	long long b = strtoll(a, NULL, 10) ;
	num.PB(b) ;
	solve(pos+i, num) ;
	num.pop_back() ;
	if (pos)
	{
	    num.PB(-b) ;
	    solve(pos+i, num) ;
	    num.pop_back() ;
	}
    }
    return ;
}

int main()
{
    int ncase ;
    
    gets(str) ;
    sscanf(str, "%d", &ncase) ;
    //    printf("ncase %d\n", ncase) ;
    FOR(icase,1,ncase)
    {
	getinput() ;
	cnt = 0 ;
	VLL num ;
	solve(0, num) ;
	printf("Case #%d: %Ld\n", icase, cnt) ;
    }
}

