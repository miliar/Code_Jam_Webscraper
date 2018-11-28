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

using namespace std;
typedef char s8;typedef unsigned char u8;typedef short s16;typedef unsigned short u16;
typedef int s32;typedef unsigned int u32;typedef long long s64;typedef unsigned long long u64;
typedef float f32;typedef double f64;
typedef vector<int> vi; typedef deque<int> di; typedef vector<string> vs; typedef pair<int,int> pii; typedef map<string,int> msi;

#define fo(a,b,c) for( a = ( b ); a < ( c ); ++ a )
#define fr(a,b) fo( a, 0, ( b ) )
#define fi(a) fr( i, ( a ) )
#define fj(a) fr( j, ( a ) )
#define fk(a) fr( k, ( a ) )

#define INF 0x3f3f3f3f
#define avg(x, y) ((x&y)+((x^y)>>1))
#define mp(x, y) make_pair(x, y)
#define pb push_back
#define pq priority_queue
#define LEN(x) ((s32)x.length())
#define st(a,b) memset(a, b, sizeof(a))
#define SIZE(x) ((s32)x.size())
#define PR(x) do { cout << x << " "; } while(false)
#define PRL(x) do { cout << x << "\n"; } while(false)
#define BR do { printf("\n"); } while(false)
int ni() { int x; scanf( "%d", &x ); return x; } f32 nf() { f32 x; scanf( "%f", &x ); return x; }  f64 nd() { f64 x; scanf( "%lf", &x ); return x; } 
char sbuf[100005]; string ns() { scanf( "%s", sbuf ); return sbuf; }  char nc() { scanf("%s", sbuf); return sbuf[0]; }  s64 nl() { s64 x; scanf( "%lld", &x ); return x; } 
inline u32 clz(u32 n) { unsigned long x; _BitScanForward(&x, n); return (x); } inline u32 ctz(u32 n) { unsigned long x; _BitScanReverse(&x, n); return (x); }
#define NI ni()
#define NF nf()
#define ND nd()
#define NS ns()
#define NC nc()
#define NL nl()
template<class T> T clamp(const T &x, T a, T b) { if(a > b) { swap(a, b); } return x <= a?a:(x > b)?b:x; }
template<class T> void out( T a, T b ) { bool f = true; for( T i = a; i != b; ++ i ) { if(!f) pr(" "); f = false; cout << * i; } pr("\n"); }
template<class T> void outl( T a, T b ) { for( T i = a; i != b; ++ i ) { cout << * i << "\n"; } }
struct state { state(int x_, int y_, int c_) : x(x_), y(y_), c(c_) {} int c; int x; int y; }; bool operator <(const state &a, const state &b) { return a.c < b.c; }
struct rstate { rstate(int x_, int y_, int c_) : x(x_), y(y_), c(c_) {} int c; int x; int y; }; bool operator <(const rstate &a, const rstate &b) { return b.c < a.c; }

int main()
{
	int i, j, k, n, cNum;

	//freopen("A.in","r",stdin);
//	freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
//	freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
	freopen("A-small-attempt2.in","r",stdin);freopen("A-small-attempt2.out","w",stdout);
//	freopen("A-large.in","r",stdin);freopen("A-large.ans","w",stdout);

	cNum = NI;

	vector<vi> v;
	fi(101)
	{
		vi tmp;
		fj(i)
		{
			if(j == 0 || i == 0) continue;
			f32 f = (f32)i;
			f32 f2 = (100 * (f32)j / f);
			s32 aa = (s32)f2;

			if((f2 - static_cast<f32>(aa)) < 0.00001f)
			{
				tmp.pb(aa);
			}
		}
		v.pb(tmp);
	}

	for(s32 cId = 1; cId <= cNum; cId++)
	{
		printf("Case #%d: ", cId);

		//n = NI; fi(n)
		{
			n = NI;
			int d = NI;
			int g = NI;

			bool poss = false;
			bool possD = (d == 100 || d == 0), possG = (g == 100 || g == 0);

			if(g == 100 && d < 100 || g == 0 && d > 0)
			{
				possG = false;
			}
			else
			{
				possG = true;

				int mx = min(100, n);
				int atleast = INF;

				fi(100)
				{
					vi m = v[i];

					fj(SIZE(m))
					{
						int num = m[j];

						if(num == d && i <= mx)
						{
							if(!possD)
							{
								i--;
								possD = true;
							}
						}

						if(possD && num == g)
						{
							possG = true;
							break;
						}
					}
				}


			}
			
			poss = possD && possG;
			if(poss)
			{
				printf("Possible");
			}
			else
			{
				printf("Broken");
			}			
		}
	
		BR;
		fflush(stdout);
	}

	return 0;
}
