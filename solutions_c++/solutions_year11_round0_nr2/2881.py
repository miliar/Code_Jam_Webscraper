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
	int t;
	int C, D, N;
	vector<char> k1, k2, k3;
	vector<char> o1, o2;
	string tmp, inv;
	vector<char> ans;

	cin >> t;

	REP(i,t){
		k1.clear(); k2.clear(); k3.clear(); o1.clear(); o2.clear(); ans.clear();
		cin >> C; if ( C != 0 ) cin >> tmp; else tmp = "";
		REP(j,tmp.length()){
			k1.PB(tmp[j]); k2.PB(tmp[j+1]); k3.PB(tmp[j+2]);
			j+=2;
		}
		cin >> D; if ( D != 0 ) cin >> tmp; else tmp = "";
		REP(j,tmp.length()){
			o1.PB(tmp[j]); o2.PB(tmp[j+1]);
			j++;
		}

		cin >> N; cin >> tmp;
		REP(j,tmp.length()){
			if ( ans.size() < 1 ) {
				ans.PB(tmp[j]);
			} else {
				ans.PB(tmp[j]);
				while(ans.size()>1){
					int flg = 0;
					REP(z,k1.size()){
						if ( ( k1[z] == ans[ans.size()-2] && k2[z] == ans[ans.size()-1] ) ||
							( k1[z] == ans[ans.size()-1] && k2[z] == ans[ans.size()-2] ) ) {
								RME(ans);
								ans[ans.size()-1] = k3[z];
								flg = 1; break;
						}
					}
					if ( flg == 0 ) break;
				}
				while(ans.size()>1){
					int flag = 0;
					REP(z,ans.size()-1){
						if(flag==1)break;
						REP(y,o1.size()){
							if ( o1[y]==ans[z] ) {
								if ( ans[ans.size()-1] == o2[y] ) {
									ans.clear(); flag=1; break;
									//vector<char> newans;
									//REP(x,z){
									//	newans.PB(ans[x]);
									//}
									//ans = newans; flag = 1; break;
								}
							} else if ( o2[y]==ans[z] ) {
								if ( ans[ans.size()-1] == o1[y] ) {
									ans.clear(); flag=1; break;
									//vector<char> newans;
									//REP(x,z){
									//	newans.PB(ans[x]);
									//}
									//ans = newans; flag = 1; break;
								}
							}
						}
					}
					if ( flag == 0 ) break;
				}
			}
		}

		cout << "Case #" << (i+1) << ": [";
		REP(z,ans.size()){
			cout << ans[z];
			if ( z+1 != ans.size() ) {
				cout << ", ";
			}
		}
		cout << "]" << endl;

	}

	return 0;

}