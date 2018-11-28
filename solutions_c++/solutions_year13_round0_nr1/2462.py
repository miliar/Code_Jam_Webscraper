#pragma comment(linker, "/STACK:268435456")
//#ifdef TEDDY_BEARS
//#pragma hdrstop
//#endif
#define _CRT_SECURE_NO_WARNINGS
#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <deque>
#include <queue>
#include <list>
#include <stack>
#include <cstring>
#include <cstdlib>
#include <complex>
#include <ctime>
#include <bitset>
#include <iomanip>
#include <sstream>
#include <hash_map>

using namespace std;
const double pi = 3.1415926535897932384626433832795;
template<class T> T min(T &a, T &b) { return (a<b) ? a : b; }
template<class T> T max(T &a, T &b) { return (a>b) ? a : b; }
template<class T> T sqr(T a) { return a*a; }
template<class T> T abs(T &a) { return (a<0) ? (-a) : a; }
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<int,int> ii;

// int
inline void read   (int &x) { scanf ("%d",   &x); }
inline void readln (int &x) { scanf ("%d\n", &x); }
inline void write  (int  x) { printf("%d",    x); }
inline void writeln(int  x) { printf("%d\n",  x); }
// long long
#ifdef _WIN32
inline void read   (ll &x) { scanf ("%I64d",   &x); }
inline void readln (ll &x) { scanf ("%I64d\n", &x); }
inline void write  (ll  x) { printf("%I64d",    x); }
inline void writeln(ll  x) { printf("%I64d\n",  x); }
#else
inline void read   (ll &x) { scanf ("%lld",   &x); }
inline void readln (ll &x) { scanf ("%lld\n", &x); }
inline void write  (ll  x) { printf("%lld",    x); }
inline void writeln(ll  x) { printf("%lld\n",  x); }
#endif
// double
inline void read   (double &x) { scanf ("%lf",     &x); }
inline void readln (double &x) { scanf ("%lf\n",   &x); }
inline void write  (double  x) { printf("%.15lf",   x); }
inline void writeln(double  x) { printf("%.15lf\n", x); }
// string
inline void read   (char* s) { scanf ("%s"  , s); }
inline void readln (char* s) { scanf ("%s\n", s); }
inline void write  (const char* s) { printf("%s"  , s); }
inline void writeln(char* s) { printf("%s\n", s); }
// read methods
inline int    readInt()    {    int x; read(x); return x; }
inline ll     readLong()   {     ll x; read(x); return x; }
inline double readDouble() { double x; read(x); return x; }

void showTime() {
//#ifdef TEDDY_BEARS
	cerr << "Time = " << double(clock()) / CLOCKS_PER_SEC << endl;
//#endif
}

#define all(v) (v).begin(),(v).end()
#define sz(v) ((int)((v).size()))
#define PB push_back
#define MP make_pair
#define CLR(a) memset((a),0,sizeof(a))
#define FILL(a,x) memset((a),(x),sizeof(a))
#define CPY(dst,src) memcpy(dst,src,sizeof(src));
#define fori(i,n) for(int i=0;i<((int)(n));i++)
#define forab(i,a,b) for(int i=((int)(a));i<=((int)(b));i++)
#define forba(i,b,a) for(int i=((int)(b));i>=((int)(a));i--)

#ifdef TEDDY_BEARS
#define show(x) { cerr << #x << " = " << x << endl; }
#define showPair(x) { cerr << #x << " = (" << x.first << "," << x.second << ")" << endl; }
#define showArr(a,n) { cerr << #a << " ="; fori(i,n) cerr << " " << a[i]; cerr << endl; }
#define showArrPair(a,n) { cerr << #a << " ="; fori(i,n) cerr << " (" << a[i].first << "," << a[i].second << ")"; cerr << endl; }
#define showVect(v) { cerr << #v << " ="; fori(i,sz(v)) cerr << " " << v[i]; cerr << endl; }
#define showVectPair(v) { cerr << #v << " ="; fori(i,sz(v)) cerr << " (" << v[i].first << "," << v[i].second << ")"; cerr << endl; }
#else
#define show(x)
#define showPair(x)
#define showArr(a,n)
#define showArrPair(a,n)
#define showVect(v)
#define showVectPair(v)
#endif

inline void prepareInputOutput()
{
#ifdef TEDDY_BEARS
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#else
	//#define FILENAME "drunk"
	//freopen(FILENAME".in", "r", stdin);
	//freopen(FILENAME".out", "w", stdout);
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
#endif
}
//------------------------------------------------------------------------------

const int N = 4;
char a[N+1][N+1];

bool win(char who)
{
	bool w;
	fori(i,N)
	{
		w = true;
		fori(j,N)
			if(a[i][j] != who && a[i][j] != 'T')
				w = false;
		if(w)
			return true;
	}
	fori(j,N)
	{
		w = true;
		fori(i,N)
			if(a[i][j] != who && a[i][j] != 'T')
				w = false;
		if(w)
			return true;
	}
	w = true;
	fori(i,N)
		if(a[i][i] != who && a[i][i] != 'T')
			w = false;
	if(w)
		return true;
	w = true;
	fori(i,N)
		if(a[i][N-i-1] != who && a[i][N-i-1] != 'T')
			w = false;
	if(w)
		return true;
	return false;
}

int main()
{
	prepareInputOutput();
	int testCnt;
	cin >> testCnt;
	fori(testNo,testCnt)
	{
		printf("Case #%d: ", testNo+1);
		fori(i,N)
			cin >> a[i];
		if(win('X'))
			cout << "X won";
		else if(win('O'))
			cout << "O won";
		else
		{
			bool over = true;
			fori(i,N)
				fori(j,N)
					if(a[i][j] == '.')
						over = false;
			if(over)
				cout << "Draw";
			else
				cout << "Game has not completed";
		}
		cout << endl;
	}
}