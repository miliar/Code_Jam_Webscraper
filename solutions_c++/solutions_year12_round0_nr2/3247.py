#include <iostream> 
#include <algorithm> 
#include <vector> 
#include <cstdio> 
#include <string> 
#include <bitset> 
#include <cmath> 
#include <list> 
#include <cstdlib> 
#include <map> 
#include <cstring> 
#include <set> 
#include <stack> 
#include <sstream> 
#include <queue> 
#include <deque> 
#include <ctime> 

using namespace std; 

#define debug(x) cout<<#x<<" = "<<x<<"\n" 
#define REP(i,n) for(int (i)=0;(i)<(n);(i)++) 
#define PI 3.1415926535897932385 
#define INF (1<<29) 
#define EPS (1e-7) 
#define pb push_back 
#define sz size() 
#define ln length() 
#define mp make_pair 
#define all(a) a.begin(),a.end() 
#define fill(ar,val) memset(ar,val,sizeof ar) 
#define sqr(x) ((x)*(x)) 
#define min(a,b) ((a)<(b)?(a):(b)) 
#define max(a,b) ((a)>(b)?(a):(b)) 
#define FORE(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++) 

typedef long long LL; 
typedef long double LD; 
typedef vector<int> VI; 

int main()
{
	int t,ti;
	cin >> t;
	int n,s,p;
	
	for ( int test = 1; test <= t; test++ ) {
		cin >> n >> s >> p;
		int ans = 0;
		int vals = 3 * p - 4;
		int valn = 3 * p - 2;
		valn = (valn >= p ) ? valn:p;
		vals = ( vals >= p ) ? vals:p;
		
		REP(i,n) {
			cin >> ti;
			if ( ti < valn && ti >= vals && s > 0 ) {
				ans++;
				--s;
				continue;
			}
			
			if ( ti >= valn ) ans++;
			
		}
		
		cout << "Case #"<<test<<": " << ans << endl;
	}
	
	return 0;
}
