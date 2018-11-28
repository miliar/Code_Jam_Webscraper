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
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <ctime> 
using namespace std; 
  
#define VAR(a,b) __typeof(b) a=(b) 
#define FOR(i,a,b) for (int _n(b), i(a); i < _n ; i++) 
#define FORK(i,a,b,k) for (int _n(b), i(a); i < _n ; i+=k) 
#define FORD(i,a,b) for ( int i=(a),_b=(b); i>=_b; --i) 
#define FORE(it,c) for(VAR(it,(c).begin());it!=(c).end(); ++it) 
#define REP(i,n) FOR(i,0,n) 
#define ALL(c) (c).begin(), (c).end() 
#define CLEAR(x,with) memset(x,with,sizeof(x)) 
#define SZ(c) (c).size()
#define INPUT "A-large.in"
#define OUTPUT "A-large.out"

typedef long long LL; 


int main()
{
	int T;
	FILE *fp = fopen(INPUT,"r");
	FILE *out = fopen(OUTPUT,"w");
	fscanf(fp,"%d",&T);
	int L[1000][2];
	int n;
	int count;
	for (int TT=1; TT<=T;++TT)
	{
		count=0;

		fscanf(fp,"%d",&n);
		REP(i , n)
		{
			fscanf(fp,"%d%d",&L[i][0],&L[i][1]);
		}

		for (int i =0 ; i < n-1 ;++i)
		{
			for (int j = i+1; j < n ;++j)
			{
				if ( (L[i][0]-L[j][0]) * (L[i][1]-L[j][1]) <0 ) 
					count++;
			}
		}
		fprintf(out,"Case #%d: ",TT);
			
		fprintf(out,"%d\n",count);
	}
	fclose(out);
	fclose(fp);
	return 0;
}