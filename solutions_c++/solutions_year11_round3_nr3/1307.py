#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <string>
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
#include <cstring> 
#include <ctime> 
using namespace std;
/*
#define PB push_back 
#define MP make_pair 
#define maxsize 1100
typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef map<string,int> msi;
*/
int gi() { int a; scanf( "%d", &a ); return a; }//GetInteger
char gc() { char a; scanf( "%c", &a ); return a; }//GetCharacter
double gd() { double a; scanf( "%lf", &a ); return a; }//GetDouble
char StrBuf[100005];
string gstr() { scanf( "%s", StrBuf ); return StrBuf; }//GetString
char* gs() { scanf( "%s", StrBuf ); return StrBuf; }//GetString
long long gll() { long long a; scanf( "%lld", &a ); return a; }//GetLongLongInteger

#define set(a,b) memset( a, b, sizeof( a ) ) 

#define max(a,b) (a)>(b)?(a):(b) 
#define min(a,b) (a)<(b)?(a):(b) 

#define FOR(i,a,b) for( (i)=(a); (i)<(int)(b); (i)++ ) //state i by yourselfe
#define rep(i,n) FOR(i,0,n)		//repeat
#define repstr(i,str) for( (i)=0 ;str[(i)]; ++(i) )
/*
#define SZ(v) ((int)(v).size()) 
*/
int  f[10001];
int cmp(const void *a,const void *b)
{
	return *(int *)a - *(int *)b;
}
int gcd(int a, int b)
{
    return b ? gcd(b, a % b) : a;
}
int lcm(int a,int b)
{
    return a*b/gcd(a, b);
}
void code(void)
{
/*input main code*/
	int n = gi(), l = gi(), h = gi(), i, j;
	rep(i, n)
	{
		f[i] = gi();
	}
	qsort(f, n, sizeof(int), cmp );
	FOR(i, l, h+1)
	{
		rep(j, n)
		{
			if(f[j]%i && i%f[j])
				break;
		}
		if(j==n) break;
	}
	if(l<=i && i<=h)
		printf(" %d\n", i);
	else
		printf(" NO\n" );
//printf(" \n" );
}
int main (void)
{
	freopen( "C-small-attempt0.in", "r", stdin );
	freopen( "output.txt", "w", stdout );
	int T, I;
	T = gi();
	rep(I, T)
	{
		printf("Case #%d:", I+1);
		code();
	}
	return 0;
}