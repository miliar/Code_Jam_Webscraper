#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <complex>
#include <deque>
#include <iostream>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <string>
#include <sstream>
#include <set>
#include <utility>
using namespace std;
#define REP(I,N) for(int I=0;I<(N);++I)
#define FOR(I,A,B) for(int I=(A);I<=(B);++I)
#define FOD(I,A,B) for(int I=(A);I>=(B);--I)
#define FOREACH(I,C) for(typeof((C.begin())) I=(C).begin();I!=(C).end();++I)
#define ALL(A) (A).begin(),(A).end()
#define SIZE(A) (int)(A).size()

int val[51];

void solve(int test_num)
{
	int res = 0;
	int n;
	scanf("%d\n",&n);
	REP(i,n) {
		string s;
		cin >> s;
		val[i] = 0;
		REP(j,n)
			if(s[j]=='1')
				val[i] = j;
	}
	REP(i,n)
	{	
		FOR(j,i,n-1) {
			if( val[j] <= i ) {
				int tmp = val[j];
				
				FOD(k,j,i+1)
					val[k] = val[k-1]; 
				val[i] = tmp;
		
				res += j - i;
				break;
			}
		}
		//REP(i,n) printf("%d ",val[i]); printf("\n");
	}	
	printf("Case #%d: %d\n",test_num,res);
}

int main() {
	int tests;
	scanf("%d\n",&tests);
	FOR(i,1,tests)
		solve(i);
	return 0;
}







/* #########################################################################################################################
// DEFINICJE

#define INF 1000000000
#define EPS 1e-9
#define MP make_pair
#define ST first
#define ND second

typedef long long LL;
typedef long double LD;
typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef vector<string> VS;
typedef vector<int> VI;
typedef map<int,int> MII;
typedef map<string,int> MSI;
typedef set<int> SI;
typedef set<string> SS;

#define PI 3.141592653589793

struct par { int a,b; };
bool operator<(const par &A,const par &B) { return A.a!=B.a ? A.a<B.a : A.b<B.b; }

int dx[8]={1,1,1,-1,-1,-1,0,0};
int dy[8]={1,0,-1,1,0,-1,1,-1};
int dx[4]={0,0,1,-1};
int dy[4]={1,-1,0,0};

string is(int x) { char b[51]; sprintf(b,"%d",x); return b; }
int si(string s) { stringstream str(s); int x; str >> x; return x; }







// #########################################################################################################################
// CZESTO UZYWANE FUNKCJE: BFS, PRIME, NWD, EXTNWD;

int bfs() {
	REP() used[] = 0;
	queue<> Q;
	Q.push();
	used[] = 1;
	while(!Q.empty()) {
		= Q.front();
		Q.pop();
		if() {
			continue;
		}
		REP() {
			if( !used[] ) {
				Q.push();
				used[] = 1;
			}
		}
	}
}

bool is_prime(int x) {
	if(x<2) return 0;
	for(int i=2;i*i<=x;++i)  if((x%i)==0) return 0;
	return 1;
}

int nwd(int a,int b) { return !b?a:nwd(b,a%b); }
LL nwd(LL a,LL b) { return !b?a:nwd(b,a%b); }

// dla NWD(A,B) = aX+bY ->  NWD(A,B) , X , Y
// odwrotnosc a mod n to po prostu (EXT(a,n).second.first+n)%n
pair< int , pair<int,int> > EXT(int a,int b) {
	if( b == 0LL ) return MP(a,MP(1LL,0));
	pair< int , pair<int,int> > prim = EXT(b,a%b);
	pair< int , pair<int,int> > res;
	res.first = prim.first;
	res.second.first = prim.second.second;
	res.second.second = prim.second.first - (a/b) * prim.second.second;
	return res;
}







// #########################################################################################################################
// GEOMETRIA

struct POINT {
	LD x,y;
	POINT(LD xx=0,LD yy=0) { x = xx; y = yy; }
};

POINT operator+(POINT a,POINT b) { return POINT(a.x+b.x,a.y+b.y); }
POINT operator-(POINT a,POINT b) { return POINT(a.x-b.x,a.y-b.y); }

bool ZERO(LD x) { return ( -EPS <= x && x <= EPS ); }

LD det(POINT a,POINT b,POINT c=POINT()) {
	return (a.x-c.x)*(b.y-c.y) - (a.y-c.y)*(b.x-c.x);
}

LD skal(POINT a,POINT b,POINT c) {
	return (a.x-c.x)*(b.x-c.x) + (a.y-c.y)*(b.y-c.y);
}

LD dist(POINT &a,POINT &b) {
	return sqrtl(skal(b,b,a));
}

POINT rzutC_AB(POINT c,POINT a,POINT b) {
	LD wsp = skal(c,b,a)/skal(b,b,a);
	return POINT( a.x + wsp*(b.x-a.x), a.y + wsp*(b.y-a.y) );
}

LD dlrzutuC_AB(POINT c,POINT a,POINT b) {
	return skal(c,b,a)/dist(a,b);
}

POINT obrot(POINT s,POINT p,LD k) {
	LD sink = sinl(k);
	LD cosk = cosl(k);
	POINT v(p.x-s.x,p.y-s.y);
	return POINT(s.x + v.x*cosk - v.y*sink, s.y + v.x*sink + v.y*cosk);
}

// format (punkt wektor punkt, wektor)
POINT przet(POINT a,POINT b,POINT c,POINT d) {
	LD A1 = -b.y, B1 =  b.x, C1 = det(a,b);
	LD A2 = -d.y, B2 =  d.x, C2 = det(c,d);
	LD W  = det(POINT( A1, B1),POINT( A2, B2));
	LD Wx = det(POINT(-C1, B1),POINT(-C2, B2));
	LD Wy = det(POINT( A1,-C1),POINT( A2,-C2));
	return POINT(Wx/W,Wy/W);
}







// #########################################################################################################################
// MACIERZE

#define MODULOMATRIX 1000000007
#define MATRIXSIZE 100
struct matrix {
	int t[MATRIXSIZE][MATRIXSIZE];
	matrix() 
	{
		REP(i,MATRIXSIZE)
		REP(j,MATRIXSIZE)
			t[i][j] = 0;
	}	
	void zero()
	{
		REP(i,MATRIXSIZE)
		REP(j,MATRIXSIZE)
			t[i][j] = 0;
	}
	void jeden()
	{
		REP(i,MATRIXSIZE)
		REP(j,MATRIXSIZE)
			t[i][j] = 0;
		REP(i,MATRIXSIZE)
			t[i][i] = 1;
	}
};

matrix operator*(matrix A,matrix B) {
	matrix C;
	REP(i,MATRIXSIZE)
	REP(k,MATRIXSIZE)
	REP(j,MATRIXSIZE)
	{
		C[i][j] += A[i][k] * B[k][j];
		C[i][j] %= MODULOMATRIX;
	}	
}

matrix pot(matrix A,int w) {
	matrix result;
	result.jeden();
	while( w != 0 ) {
		if( w&1 ) result = result * A;
		A = A * A;
		w /= 2;
	}
	return result;
}












// #########################################################################################################################
// BIGNUMY
// Potrzebne makro REP,FOR,FOD
// Nalezy dodac typedef long long LL;
// UWAGA: dziala tylko dla liczb beznaku, dla liczb ze znakiem trzeba dodac zmienna znak oraz 
// pare ifow do operacji (zamienic dodawanie na odejmowanie itd)

#define BASE 1000000000 		// podstawa systemu, do modulowania
#define BASEDIG 9				// 10^BASEDIG podstawa
#define DIG 2300				// ile cyfr DIG*BASEDIG

struct BigInt {
	int t[DIG];
	int len;
	BigInt() {
		REP(i,DIG) t[i] = 0;
	}
};

BigInt operator + (BigInt,BigInt);		// sprawdzone SPOJ,MAIN
BigInt operator - (BigInt,BigInt);		// sprawdzone MAIN
BigInt operator * (BigInt,int);			// sprawdzone SPOJ
BigInt operator * (BigInt,BigInt);		// sprawdzone SPOJ, O(n^2)
BigInt operator / (BigInt,int);			// sprawdzone dla 2 na MAIN
int operator % (BigInt,int);			// powinno byc ok, bo jest jak na MAIN
void wypisz(BigInt,int);				// sprawdzone SPOJ,MAIN
BigInt wczytaj();						// sprawdzone SPOJ,MAIN
bool operator == (BigInt,int);
bool operator == (BigInt,BigInt);

BigInt operator + (BigInt a,BigInt b) {
	BigInt c;
	c.len = max(a.len,b.len);
	int rest = 0;
	REP(i,c.len) {
		c.t[i] = (a.t[i] + b.t[i] + rest) % BASE;
		rest = (a.t[i] + b.t[i] + rest) / BASE;
	}
	for( ; rest ; rest /= BASE )  c.t[c.len++] = rest % BASE;
	return c;
}

BigInt operator - (BigInt a,BigInt b) {
	BigInt c;
	c.len = max(a.len,b.len);
	int rest = 0;
	REP(i,c.len) {
		c.t[i] = ( a.t[i] - rest - b.t[i] + BASE ) % BASE;
		if( a.t[i] - rest - b.t[i] < 0 ) rest = 1;
		else rest = 0;
	}
	while( c.t[c.len-1] == 0 ) {
		if( c.len <= 1 ) break;
		c.len --;
	}
	return c;
}

BigInt operator * (BigInt a,int b) {
	BigInt c;
	c.len = a.len;
	LL rest = 0;
	REP(i,c.len) {
		c.t[i] = ( LL(a.t[i])*LL(b) + LL(rest) ) % BASE;
		rest = ( LL(a.t[i])*LL(b) + LL(rest) ) / BASE;
	}
	for( ; rest ; rest /= BASE )  c.t[c.len++] = rest % BASE;
	return c;
}

BigInt operator * (BigInt a,BigInt b) {
	BigInt c;
	c.len = 1;
	REP(i,b.len) {
		BigInt x = a * b.t[i];
		FOD(j,x.len-1,0)
			x.t[j+i] = x.t[j];
		REP(j,i)
			x.t[j] = 0;
		x.len += i;
		c = c + x;
	}
	while( c.t[c.len-1] == 0 ) {
		if( c.len <= 1 ) break;
		c.len --;
	}
	return c;
}

BigInt operator / (BigInt a,int b) {
	BigInt c;
	c.len = a.len;
	LL rest = 0;
	FOD(i,c.len-1,0) {
		c.t[i] = ( LL(BASE)*LL(rest) + LL(a.t[i]) ) / b;
		rest =  ( LL(BASE)*LL(rest) + LL(a.t[i]) ) % b;
	}
	while( c.t[c.len-1] == 0 ) {
		if( c.len <= 1 ) break;
		c.len --;
	}
	return c;
}

bool operator == (BigInt a,int b) {
	return ( a.len == 1 && a.t[0] == b );
}

bool operator == (BigInt a,BigInt b) {
	if( a.len != b.len ) return 0;
	REP(i,a.len)
		if( a.t[i] != b.t[i] )
			return 0;
	return 1;
}

int operator % (BigInt a,int b) {
	if( a.len==0 ) return 0;
	LL rest = a.t[a.len-1] % b;
	FOD(i,a.len-2,0)
		rest =  ( LL(BASE)*LL(rest) + LL(a.t[i]) ) % b;
	return rest;
}

void wypisz(BigInt a,int typ=0) {
	if( typ == 1 ) printf("LEN: %d\n",a.len);
	FOD(i,a.len-1,0) {
		if( i != a.len-1 ) printf("%0*d",BASEDIG,a.t[i]);
		else printf("%d",a.t[i]);
	}
	printf("\n");
}

BigInt wczytaj() {
	string s;
	cin >> s;
	int len = s.length();
	BigInt res;
	res.len = 0;
	int last = len;
	for(int i = len ; i > 0 ; i -= BASEDIG ) {
		int start = max(i - BASEDIG,0);
		int size = last - start;
		last = start;
		stringstream str(s.substr(start,size));
		str >> res.t[res.len++];
	}
	return res;
}





*/

