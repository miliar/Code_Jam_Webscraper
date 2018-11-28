#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <vector>
#include <deque>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <intrin.h>
#include <iostream>
#include <sstream>
#include <boost/typeof/typeof.hpp>

using namespace std;
typedef char s8;typedef unsigned char u8;typedef short s16;typedef unsigned short u16;
typedef int s32;typedef unsigned int u32;typedef long long s64;typedef unsigned long long u64;
typedef float f32;typedef double f64;
typedef vector<int> vi; typedef deque<int> di; typedef vector<string> vs; typedef pair<int,int> pii; typedef map<string,int> msi; typedef pair<f64, f64> pff;
typedef list<string> ls; typedef vector<pii> vii; typedef deque<pii> dii; typedef deque<pff> dff; typedef list<int> li;

#define fo(a,b,c) for(a=(b);a<(c);++a)
#define fr(a,b) fo(a,0,(b))
#define fi(a) fr(i,(a))
#define fj(a) fr(j,(a))
#define fk(a) fr(k,(a))
#define fl(a) fr(l,(a))
#define fit(a,b) for(a ::iterator it = (b).begin(); it != (b).end(); it++)
#define fall(a) fit(BOOST_TYPEOF(a), a)

#define INF 0x3f3f3f3f
#define avg(x, y) ((x&y)+((x^y)>>1))
#define mp(x, y) make_pair(x, y)
#define pb push_back
#define pf push_front
#define pq priority_queue
#define LEN(x) ((s32)x.length())
#define LENA(x) (sizeof(x) / sizeof(x[0]))
#define st(a,b) memset( a, b, sizeof( a ) )
#define SIZE(x) ((s32)x.size())
#define pr printf
#define PR(x) do { cout << x << " "; } while(false)
#define PRL(x) do { cout << x << "\n"; } while(false)
#define BR do { printf("\n"); } while(false)
int ni() { int x; scanf( "%d", &x ); return x; } f32 nf() { f32 x; scanf( "%f", &x ); return x; }  f64 nd() { f64 x; scanf( "%lf", &x ); return x; } 
char sbuf[100005]; string ns() { scanf( "%s", sbuf ); return sbuf; }  char nc() { scanf("%s", sbuf); return sbuf[0]; }  s64 nl() { s64 x; scanf( "%lld", &x ); return x; } 
inline u32 clz(u32 n) { unsigned long x; _BitScanForward(&x, n); return (x); } inline u32 log2(u32 n) { unsigned long x; _BitScanReverse(&x, n); return (x); }
#define NI ni()
#define NF nf()
#define ND nd()
#define NS ns()
#define NC nc()
#define NL nl()
#define all(a) a.begin(), a.end()
template<class T> inline void gmin(T &a,T b){if(b<a) a=b;}template<class T> inline void gmin(T &a, int &i, T b, int i2){if(b<a){a=b;i=i2;}}
template<class T> inline void gmax(T &a,T b){if(b>a) a=b;}template<class T> inline void gmax(T &a, int &i, T b, int i2){if(b>a){a=b;i=i2;}}
template<class T> T gcd(T a, T b) { for(;;) { if(a == 0) return b; b %= a; if(b == 0) return a; a %= b; } }
template<class T> T lcm(T a, T b) { a /= gcd(a, b); if((1 << ((sizeof(T) * 8 - 1) - 1)) / b < a) return -1; return a * b; }
template<class T> T clamp(const T &x, T a, T b) { if(a > b) { swap(a, b); } return x <= a?a:(x > b)?b:x; }
template <class T> void out( T a, T b ) { bool f = true; for( T i = a; i != b; ++ i ) { if(!f) printf(" "); f = false; cout << * i; } printf("\n"); }
template <class T> void outl( T a, T b ) { for( T i = a; i != b; ++ i ) { cout << * i << "\n"; } }

#define N 1001

int q[501][501];

int n;

#define V(cur, mn, siz) (((cur) << 1) - (((mn) << 1) + (siz) - 1))

bool chk(int x, int y, int size)
{
	int i,j,k;
	int ysum = 0, xsum = 0;
	fo(i, x + 1, x + size - 1)
	{
		int cy = y;
		ysum += V(cy, y, size) * q[cy][i];
		xsum += V(i, x, size) * q[cy][i];
		cy = y + size - 1;
		ysum += V(cy, y, size) * q[cy][i];
		xsum += V(i, x, size) * q[cy][i];
	}
	fo(j, y + 1, y + size - 1)
	{
		fo(i, x, x + size)
		{
			ysum += V(j, y, size) * q[j][i];
			xsum += V(i, x, size) * q[j][i];
		}
	}

	return (xsum == 0 && ysum == 0);
}

int main()
{
	int i, j, k, l;

	//freopen("B.in","r",stdin);
	freopen("B-small-attempt0.in","r",stdin);freopen("B-small-attempt0.out","w",stdout);
	//freopen("B-small-attempt1.in","r",stdin);freopen("B-small-attempt1.out","w",stdout);
	//freopen("B-small-attempt2.in","r",stdin);freopen("B-small-attempt2.out","w",stdout);
	//freopen("B-large.in","r",stdin);freopen("B-large.ans","w",stdout);

	for(s32 cId = 1, cNum = NI; cId <= cNum; cId++)
	{
		printf("Case #%d: ", cId);
		st(q, 0);
		int Y = NI; int X = NI;
		int d = NI;
		fi(Y)
		{
			string s = NS;
			fj(X)
			{
				q[i][j] = s[j] - '0';
			}
		}

		bool ok = false;

		int size = min(X, Y);
		while(size >= 3)
		{
			fi(X - (size - 1))
			{
				fj(Y - (size - 1))
				{
					if(chk(i, j, size))
					{
						ok = true;
						PR(size);
						goto end;
					}
				}
			}
		

			if(ok) break;
			size--;
		}

		if(!ok)
		{
			pr("IMPOSSIBLE");
		}

end:
		

		BR;
		fflush(stdout);
	}

	return 0;
}