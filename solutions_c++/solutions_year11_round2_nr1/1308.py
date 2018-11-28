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
	
	int t,n;
	string s;
	int d[120][120];
	double wp[120];
	double owp[120];
	double oowp[120];
	double rpi[120];

	scanf("%d",&t);
	
	FOR(i,1,t+1)	
	{
		scanf("%d",&n);
		FOR(j,0,n)
		{
			cin >> s;
			FOR(k,0,n)
			{
				if (s[k]=='.') d[j][k]=-1;
				if (s[k]=='1') d[j][k]=1;
				if (s[k]=='0') d[j][k]=0;
			}
		}
		
		FOR(k,0,n)
		{
			double g=0;
			double w=0;
			FOR(j,0,n)
			{
				if (d[k][j]!=-1) g++;
				if (d[k][j]==1) w++;
			}
			wp[k]=w/g;
		}
	
		FOR(k,0,n)
		{
			double g=0;
			double w=0;
			
			FOR(j,0,n)
			{
				if (d[k][j]!=-1)
				{
					g++;

					double g1=0;
					double w1=0;
					
					FOR(l,0,n)
					{
						if (d[j][l]!=-1 && l!=k) g1++;
						if (d[j][l]==1 && l!=k) w1++;
					}
					
					w+=w1/g1;
				}
			}
			owp[k]=w/g;
		}
		
		FOR(k,0,n)
		{
			double g=0;
			double w=0;
			
			FOR(j,0,n)
			{
				if (d[k][j]!=-1) g++;
				if (d[k][j]!=-1) w+=owp[j];
			}
			oowp[k]=w/g;
		}

		cout << "Case #" << i << ":"<< endl;
		FOR(k,0,n)
		{
			rpi[k]=0.25 * wp[k] + 0.50 * owp[k] + 0.25 * oowp[k];
			printf("%.10lf\n",rpi[k]);
		}
	}
	
	
	tme();
    return 0;
}