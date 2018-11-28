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
	
	int t,n,p; char c;
	int time,t1,t2,pos1,pos2,time1,time2;

	scanf("%d",&t);

	FOR(i,1,t+1)
	{
		scanf("%d",&n);
		
		time1=time2=t1=t2=0;
		pos1=pos2=1;

		FOR(j,0,n)
		{
			cin >> c >> p;
			
			if (c=='O')
			{
				int move=ABS(p-pos1);
				
				if (move+time1>=t2)
				{
					time1+=move+1;
					t1=time1;
				}
				else
				{
					time1=t2+1;
					t1=time1;
				}
				pos1=p;
			}
			
			else
			{
				int move=ABS(p-pos2);
				
				if (move+time2>=t1)
				{
					time2+=move+1;
					t2=time2;
				}
				else
				{
					time2=t1+1;
					t2=time2;
				}
				pos2=p;
			}

		}
		
		time=MAX(time1,time2);
		printf("Case #%d: %d\n",i,time);
	}
        
	tme();
    return 0;
}