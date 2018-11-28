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
typedef vector<int> vi; typedef deque<int> di; typedef vector<string> vs; typedef pair<int,int> pii; typedef map<string,int> msi; typedef pair<f64, f64> pff;
typedef list<string> ls; typedef vector<pii> vii; typedef deque<pii> dii; typedef deque<pff> dff;

#define fo(a,b,c) for( a = ( b ); a < ( c ); ++ a )
#define fr(a,b) fo( a, 0, ( b ) )
#define fi(a) fr( i, ( a ) )
#define fj(a) fr( j, ( a ) )
#define fk(a) fr( k, ( a ) )
#define fit(a,b) for(a ::iterator it = (b).begin(); it != (b).end(); it++)

#define INF 0x3f3f3f3f
#define avg(x, y) ((x&y)+((x^y)>>1))
#define mp(x, y) make_pair(x, y)
#define pb push_back
#define pf push_front
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

struct stu { pff area; f64 wst; };
typedef deque<stu> dst;
//f64 worst[201];

int main()
{
	int i, j, k, n, cNum;

//	freopen("B.in","r",stdin);
	freopen("B-small-attempt0.in","r",stdin);freopen("B-small-attempt0.out","w",stdout);
//	freopen("B-small-practice.in","r",stdin);freopen("B-small-p1.out","w",stdout);
//	freopen("B-small-attempt2.in","r",stdin);freopen("B-small-attempt2.out","w",stdout);
//	freopen("B-large.in","r",stdin);freopen("B-large.ans","w",stdout);

	cNum = NI;

	for(s32 cId = 1; cId <= cNum; cId++)
	{
		printf("Case #%d: ", cId);
		//st(worst, 0);
		n = NI; int c = NI;
		int tot = 0;
		vii v;
		fi(n)
		{
			int po = NI, numm = NI;
			v.pb(mp(po, numm));
			tot += numm;
		}
		sort(v.begin(), v.end());

		dst ar;
		dst done;

		fi(n)
		{
			pii x = v[i];
			stu y;
			f64 area = (f64)(x.second) * c * 0.5;
			y.wst = (f64)(x.second - 1) * 0.5 * c; 
			//if(x.second == 1) { worst[i] = 0.0f; } else {
			//	worst[i] = (area - c) / (x.second - (x.second & 1)); }
			//pff y; y.first = x.first - area; y.second = x.first + area;
			y.area.first = x.first - area; y.area.second = x.first + area;
			ar.pb(y);
			//ar.pb(y);
		}

		while(ar.size() > 1)
		{
			stu a = ar.front();
			ar.pop_front();
			stu b = ar.front();
			ar.pop_front();

			if(a.area.second > b.area.first)
			{
				f64 diff = a.area.second - b.area.first;
				stu x;
				f64 wd = a.wst - b.wst;
				wd = min(wd, diff);
				if(wd > 0.0f)
				{
					diff -= wd;
					b.wst += wd;
					b.area.first += wd;
					b.area.second += wd;
				}
				else if(wd < 0.0f)
				{
					diff += wd;
					a.wst -= wd;
					a.area.first -= wd;
					a.area.second -= wd;
				}
				if(diff > 0.0)
				{
					diff *= 0.5;
					a.wst += diff;
					b.wst += diff;
					a.area.first -= diff;
					a.area.second -= diff;
					b.area.first += diff;
					b.area.second += diff;
				}

				x.wst = max(a.wst, b.wst);
				x.area.first = a.area.first;
				x.area.second = b.area.second;
				ar.push_front(x);

			}
			else
			{
				done.pb(a);
				ar.push_front(b);
			}
		}

		if(ar.size() == 1)
		{
			done.pb(ar.front());
		}

		f64 mx = 0.0;

		fit(dst, done)
		{
			if((*it).wst > mx)
			{
				mx = (*it).wst;
			}
		}
		PR(mx);
		

		//int d = v.back() - v.front();
		//int want = c * tot;
		BR;
		fflush(stdout);
	}

	return 0;
}
