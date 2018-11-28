#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <complex>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <complex>
#include <stdio.h>
#include <cstdlib>
#include <memory.h>
#ifdef SAMMAX
#include <ctime>
clock_t beg;
#endif

const double pi = 3.1415926535897932384626433832795;

//#pragma comment(linker, "/stack:1000000000")
#define sz size()
#define mp make_pair
#define pb push_back
#define ALL(a) (a).begin(), (a).end()
#define MEMS(a,b) memset(a,b,sizeof(a))
#define sqr(a) ((a)*(a))
#define HAS(a,b) ((a).find(b)!=(a).end())
#define MAX(a,b) ((a>=b)?a:b)
#define MIN(a,b) ((a<=b)?a:b)
#define ABS(a) ((a<0)?-(a):a)
#define FOR(i,a,b) for (int i=(a);i<(b);++i)
#define FORD(i,a,b) for (int i=(a);i>(b);--i)
#define VVI vector < vector <int> >
#define VI vector <int>
#define LL long long
#define U unsigned
#define pnt pair <int,int>
int gcd(int a,int b){if (a==0) return b;return gcd(b%a,a);}

using namespace std;

void ifd() 
{
	#ifdef SAMMAX 
	freopen("in.txt","r",stdin); 
	freopen("out.txt","w",stdout); 
	beg = clock();
	#else

	#endif
}
void tme()
{
	#ifdef SAMMAX
		fprintf(stderr,"*** Total time: %.3lf ***\n",1.0*(clock()-beg)/CLOCKS_PER_SEC);
	#endif
}


int main() 
{
	ifd();
	
	int t,n,b;
	vector <int> a;
	cin >> t;
	
	FOR(i,1,t+1)
	{
		a.clear();
		cin >> n;
		FOR(j,0,n)
		{
			cin >> b;
			a.push_back(b);
		}
		int cnt=0;

		FOR(j,0,n)
			if (a[j]!=j+1) cnt++;
		//if (cnt%2==0) 
			printf("Case #%d: %d.000000\n",i,cnt);
		//else printf("Case #%d: %d.000000\n",i,cnt+1);
	}
        
	tme();
    return 0;
}