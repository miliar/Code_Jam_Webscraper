#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <sstream>
#include <algorithm>
#include <functional>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <cassert>
using namespace std;

/*========================================Templates=============================================*/
#define REP(i,n)			for(int i=0;i<(n);++i)
#define FOR(i,a,b)		for(int i=(a);i<=(b);++i)
#define FOREACH(i,c)		for(__typeof((c).begin()) i=(c).begin();i!=(c).end();++i)
#define ALL(x)			(x).begin(),(x).end()
#define S(n)				scanf("%d",&n)
#define DB(x)			cout<<#x<<" : "<<x<<endl;

typedef long long LL;
typedef unsigned long long ULL;
typedef unsigned int UINT;
/*==============================================================================================*/

double D;
int N,A;
double acc;


int main()
{
	int tc;
	cin >> tc;
	for (int cas = 1; cas <= tc; cas += 1)
	{
		cin >> D;
		cin >> N >> A;
		
		vector<double> T, X;
		for (int i = 0; i < N; i += 1)
		{
			double t,x;
			cin >> t >> x;
			T.push_back(t);
			X.push_back(x);
		}			
		
		printf("Case #%d:\n",cas);
		
		for (int i = 0; i < A; i += 1)
		{
			cin >> acc;
			double t1 = sqrt( 2 * D / acc );				
			double t2;
			if ( N == 1 )
				printf("%f\n",t1);
			else
			{
				t2 = T[N-2] + ( T[N-1] - T[N-2] ) / ( X[N-1] - X[N-2] ) * ( D - X[N-2] );
				printf("%f\n", max(t1,t2) ); 
			}
		}
	}
}




