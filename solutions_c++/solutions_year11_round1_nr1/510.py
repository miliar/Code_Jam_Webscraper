
//include
//------------------------------------------
#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <istream>
#include <iterator>
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

#include <stdio.h>
#include <memory.h>
#include <math.h>

using namespace std;

//conversion
//------------------------------------------
inline int toInt(string s) {int v; istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x) {ostringstream sout;sout<<x;return sout.str();}

//math
//-------------------------------------------
template<class T> inline T sqr(T x) {return x*x;}

//typedef
//------------------------------------------
typedef vector<int> VI;
typedef vector<long long> VLL;
typedef vector<VI> VVI;
typedef vector<double> VD;
typedef vector<VD> VVD;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef long long LL;

//container util
//------------------------------------------
#define ALL(a)  (a).begin(),(a).end()
#define RALL(a) (a).rbegin(), (a).rend()
#define PB push_back
#define MP make_pair
#define SZ(a) int((a).size())
#define EACH(i,c) for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); ++i)
#define EXIST(s,e) ((s).find(e)!=(s).end())
#define SORT(c) sort((c).begin(),(c).end())

//repetition
//------------------------------------------
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define RFOR(i,a,b) for(int i=(a)-1;i>=(b);--i)
#define REP(i,n)  FOR(i,0,n)

//constant
//--------------------------------------------
const double EPS = 1e-10;
const double PI  = acos(-1.0);

//clear memory
#define CLR(a) memset((a), 0 ,sizeof(a))

//debug
#ifdef DEBUG
#define dump(x)  cerr << #x << " = " << (x) << endl;
#define debug(x) cerr << #x << " = " << (x) << " (L" << __LINE__ << ")" << " " << __FILE__ << endl;
#define print(x) cerr << x << endl;
#else
#define dump(x) ;
#define debug(x) ;
#define print(x) ;
#endif

int ni(){
	int a;
	scanf("%d", &a);
	return a;
}

double nf(){
	double d;
	scanf("%lf", &d);
	return d;
}

long long nll(){
	long long l;
	scanf("%lld", &l);
	return l;
}

VI nvi(int num){
	VI v;
	FOR(i, 0, num){
		v.push_back(ni());
	}
	return v;
}

VD nvf(int num){
	VD v;
	FOR(i, 0, num){
		v.push_back(nf());
	}
	return v;
}

VLL nvll(int num){
	VLL v;
	FOR(i, 0, num){
		v.push_back(nf());
	}
	return v;
}

char sbuf[10000];
string ns(){
	scanf("%s", sbuf);
	return sbuf;
}

string s = "abcd";
string t = "becd";
const int n = 4;
const int m = 4;


int gcd( int m, int n )
{
	if ( ( 0 == m ) || ( 0 == n ) )
		return 0;
	
	while( m != n )
	{
		if ( m > n ) m = m - n;
		else         n = n - m;
	}
	return m;
}


int main(void){
	freopen("A-large.in", "r", stdin);
	freopen("output.txt","w", stdout);

	int num = ni();

	FOR(i, 1, num + 1){
		LL n = nll();
		int pd = ni();
		int pg = ni();

		bool p = true;

		if(pg == 100){
			if(pd != 100) p = false;

		}else if(pg == 0){
			if(pd != 0) p = false;
		}else if(pd == 100){
			if(pg == 0) p = false;
		}
		else if(pd == 0){
			if(pg == 100) p = false;

		}else{
			int gc = gcd(pd, 100 - pd);
			int win = pd / gc;
			int lose = (100 - pd) / gc;

			if(win + lose > n) p = false;
		}
		if(p){
			printf("Case #%d: Possible\n",i);
		}else{
			printf("Case #%d: Broken\n",i);
		}

	}
	
}