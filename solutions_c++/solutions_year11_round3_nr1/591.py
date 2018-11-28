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
	
	int t,r,c;
	string s;
	char d[60][60],ans[60][60];
	cin >> t;
	
	FOR(test,1,t+1)
	{
		cin >> r >> c;
		FOR(i,0,r)
		{	
			cin >> s;
			FOR(j,0,c)
				d[i][j]=s[j];
		}
		bool f=true;
		
		FOR(i,0,r)
			FOR(j,0,c)
			if (d[i][j]=='#')
			{
				if (j+1>=c || i+1>=r || d[i+1][j]!='#' || d[i+1][j+1]!='#' || d[i][j+1]!='#') {f=false; break;}
				else
				{
					d[i][j]='/';
					d[i][j+1]='\\';
					d[i+1][j]='\\';
					d[i+1][j+1]='/';
				}
			}
			cout << "Case #" << test << ":" << endl;
			if (!f) cout << "Impossible" << endl;
			else
				FOR(i,0,r)
				{
					FOR(j,0,c)
					cout << d[i][j];

				cout << endl;
				}
	}
	
	tme();
    return 0;
}