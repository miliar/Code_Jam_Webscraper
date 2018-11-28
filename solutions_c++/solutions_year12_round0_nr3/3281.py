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
	int t,hi,l1,l2;
	int A,B;
	cin >> t;
	string s1,s2,s3,s4,s5;
	for ( int test = 1; test <= t; test++ ) {
		cin >> A >> B;
		int ans = 0;
		
		for ( int i = A; i <= B-1; i++ ) {
			stringstream out1;
			out1 << i;
			s1 = out1.str();
			//sort(all(s1));
			for ( int j = i+1; j <= B; j++ ) {
				stringstream out2;
				out2 << j;
				s2 = out2.str();
				//sort(all(s2));
				if ( (l1 = s1.sz) == (l2 = s2.sz) ) {
					for ( hi = l1-1; hi >= 0; hi-- ) {
						s3 = s1.substr(hi);
						s4 = s1.substr(0,hi);
						s5 = s3+s4;
						//debug(s1);
						//debug(s2);
						//debug(s3);
						//debug(s4);
						//debug(s5);
						if ( s5 == s2 ) 
						{
						ans++; break;
						}
					}
				}
				
					
						
				
				
				
			}
		}
	
		cout << "Case #" << test << ": " << ans << endl;
	}
	
	return 0;
}
				
		
