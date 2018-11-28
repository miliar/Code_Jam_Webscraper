#include <cmath>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <ctime>
#include <sstream>
#include <iomanip>
#include <map>
#include <set>
#include <complex>

using namespace std;

typedef vector<int> VI;
typedef vector<string> VS;
typedef set<int> SI;
typedef set<string> SS;
typedef long long ll;
typedef unsigned long long ull;

#define REP(i,n) for(int i=0;i<(n);++i)
#define DREP(i,n) for(int i=(n)-1;i>=0;--i)
#define FOR(i,n,m) for(int i=(n);i<(m);++i)
#define DFOR(i,n,m) for(int i=(n);i>=(m);--i)
#define FOREACH(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define LOOP for(;;)
#define zero(n) memset((n),0,sizeof(n))
#define RMB(x) (x).erase((x).begin())
#define RME(x) (x).pop_back()
#define SORT(x) sort((x).begin(),(x).end())
#define REVERSE(x) reverse((x).begin(),(x).end())
#define PB push_back
#define ISS istringstream
#define OSS ostringstream

#define BIT(i) (1<<i)

int AddFunny(int a, int b)
{
	return (a^b);

}

int main ( void )
{
	int T,N;
	ll choice = 0, tmp;
	VI C;
	ll ans = 0, tmpans1, tmpans2, funnyans1, funnyans2;
	ll testval = 0;
	ll testval2;

	cin >> T;
	REP(i,T){
		cin >> N;
		choice = 0;
		C.clear();
		testval = 0;
		testval2 = 0;
		tmpans1 = 0; tmpans2 = 0; ans = 0;
		REP(j,N){ cin >> tmp; C.PB(tmp); }
		
		SORT(C); REVERSE(C);
		REP(j,N){
			testval2 += C[j]; testval ^= C[j];
		}
		if ( testval != 0 ) {
			cout<<"Case #"<<(i+1)<<": NO"<<endl;
			continue;
		}

		REP(j,N){
			testval2 = 0; testval = 0;
			REP(j,N){
				testval2 += C[j]; testval ^= C[j];
			}
			if ( testval != 0 ) { continue; }
			ans = max(ans,testval2-C[0]);
//			cout<<"—\‘z: "<<testval2-C[0]<<endl;
			C.PB(C[0]);
			RMB(C);
		}
//		cout<<"—\‘z: "<<ans<<endl;
		cout << "Case #"<<(i+1)<<": "<<ans<<endl;
		continue;
//
//		ans = 0;
//		
//		REP(j,BIT(N)-1){
//			if ( j == 0 ) continue;
//			choice=j;
//			tmpans1 = 0; tmpans2 = 0; funnyans1 = 0; funnyans2 = 0;
//			REP(k,N){
//				if((choice & BIT(k))==BIT(k)){
//					tmpans1 += C[k];
//					funnyans2 = AddFunny(funnyans2,C[k]);
//				} else {
//					tmpans2 += C[k];
//					funnyans1 = AddFunny(funnyans1,C[k]);
//				}
//			}
//			if ( funnyans1 == funnyans2 ) {
//				ans = max(max(tmpans1,ans),tmpans2);
//			}
//		}
//
//		if ( ans != 0 ) {
//			cout<<"Case #"<<(i+1)<<": "<<ans<<endl;
//		} else {
//			cout << "Invalid" << endl;
////			cout<<"Case #"<<(i+1)<<": NO"<<endl;
//		}

	}

	return 0;

}