#ifdef O_O
#include "a.h"
#else
#include <cstdio>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <ctime>
#endif

using namespace std;

#define PB push_back
#define MP make_pair
typedef __int64 LL;
#define ALL(x)x.begin(),x.end()
#define FOR(a,b)for(int a=0;a<b;a++)
#define FORR(a,b,c)for(int a=b;a<=c;a++)
#define FOR1(a,b)for(int a=1;a<=b;a++)
#define CLR(a,b)memset(a,b,sizeof(a))
#define CPY(a,b)memcpy(a,b,sizeof(a))
#define tr(i,c)for(typeof((c).begin())i=(c).begin();i!=(c).end();i++)


template <class T> inline bool do_max(T&a,T b) {
	if(a<b) { a=b; return true; } else return false;
}

template <class T> inline bool do_min(T&a,T b) {
	if(b<a) { a=b; return true; } else return false;
}

template <class T> ostream&operator , (ostream &r,T t) {
	r << ' ' << t ;
	return r;
}

using namespace std;

char a[128][128];
bool canrow[128],cancol[128];

bool diff(char a,char b) {
    if(a==' ' || b==' ') return  false;
    return a!=b;
}

int main()
{
//    freopen("c:/gcj/a.1","rt",stdin);
	int tests;
	scanf("%d\n",&tests);
	FORR(testno,1,tests) {
		cout << "Case #"<< testno << ": ";

		int r;
		scanf("%d",&r);

		int live=0;

		CLR(a,0);
		while(r--) {
			int	x2,y2,x1,y1;
			scanf("%d %d %d %d",&x1,&y1,&x2,&y2);
			FORR(x,x1,x2) FORR(y,y1,y2) { if(!a[y][x]) {a[y][x]=1; live++;} }

		}

		int x1=1,x2=100,y1=1,y2=100;
		int t=0;
		while(live) {
			t++;
			for(int y=y2;y>=y1;y--) 
			for(int x=x2;x>=x1;x--) {
				if(!a[y][x]) {
					if(a[y-1][x] & a[y][x-1]) { live++; a[y][x]=1; }
				} else {
					if(a[y-1][x] | a[y][x-1]) ; else { live--; a[y][x]=0; }
				}
			}
		}

		cout << t << endl;
	}

	return 0;
}