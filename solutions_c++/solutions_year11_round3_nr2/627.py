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


int main ( void )
{
	int T;
	ll L, t, N, C;
	int tmp;
	ll ans;
	ll minans;
	int DEBUG = 0;
	int DEBUG2 = 0;
	VI a;

	cin >> T;
	REP(i,T){
		a.clear();
		ans = 0;
		minans = 1000000000000;
		
		cin >> L >> t >> N >> C;
		REP(j,C){
			cin >> tmp;
			a.PB(tmp);
		}

		// no booster
		REP(j,N){
			ans = ans + a[j%C];
		}
		ans *= 2;
		minans = ans;
		
		if ( L == 0 ) {
			minans = ans;

		} else if ( L == 1 ) {
			REP(j,N){
				ll tmpans = ans;
				ll cost = t;
				ll elapse = 0;
				REP(k,j){
					elapse = elapse + a[k%C]*2;
				}
				ll moreneed = cost - elapse;
				if ( moreneed <= 0 ) {
					// completed
					tmpans = tmpans - a[j%C];

				} else {
					// not completed
					if ( moreneed >= a[j%C]*2 ) {
						// not good
					} else {
						if(DEBUG){
							if (  (a[j%C]*2-moreneed)%2 != 0 ) {
								cout << "WARNING!" << endl;
							}
						}
						tmpans = tmpans - (a[j%C]*2-moreneed)/2;
					}

				}
				minans = min(minans, tmpans);
				
			}

		} else if ( L == 2 ) {
			int stt;
			REP(j,N){
				FOR(z,j+1,N){
					ll tmpans = ans;
					ll cost = t;
					ll elapse = 0;
					int shorttm = 0;
					REP(k,j){
						elapse = elapse + a[k%C]*2;
					}
					ll moreneed = cost - elapse;
					if ( moreneed <= 0 ) {
						// completed
						tmpans = tmpans - a[j%C];
						shorttm = a[j%C];

					} else {
						// not completed
						if ( moreneed >= a[j%C]*2 ) {
							// not good
						} else {
							if(DEBUG){
								if (  (a[j%C]*2-moreneed)%2 != 0 ) {
									cout << "WARNING!" << endl;
								} else {
//									cout << "OK" << endl;
								}
							}
							tmpans = tmpans - (a[j%C]*2-moreneed)/2;
							shorttm = (a[j%C]*2-moreneed)/2;
							if ( (a[j%C]*2-moreneed)%2 == 1 ) {
								stt = 1;
							} else {
								stt = 0;
							}
						}

					}

					elapse = 0;
					REP(k,z){
						elapse = elapse + a[k%C]*2;
					}
					elapse -= shorttm;
					moreneed = cost - elapse;
					if ( moreneed <= 0 ) {
						// completed
						tmpans = tmpans - a[z%C];
						shorttm = a[z%C];

					} else {
						// not completed
						if ( moreneed >= a[z%C]*2 ) {
							// not good
						} else {
							if(DEBUG){
								if ( (a[z%C]*2-moreneed)%2 != 0 ) {
									cout << "WARNING!" << endl;
								} else {
//									cout << "OK" << endl;
								}
							}
							tmpans = tmpans - (a[z%C]*2-moreneed)/2;
							shorttm = (a[z%C]*2-moreneed)/2;
							if ( stt == 1 && (a[z%C]*2-moreneed)%2 == 1 ) {
								tmpans--;
								if(DEBUG2){
									cout << "HIT!!" << endl;
								}
							}
						}

					}


					minans = min(minans, tmpans);
				}				
			}
		}


		cout << "Case #" << (i+1) << ": " << minans << endl;

	}

	return 0;

}