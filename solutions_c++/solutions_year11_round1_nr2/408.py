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
	int N, M;
	VS dict;
	VS ans;
	string tmp;
	string let;

	int DEBUG = 0;

	cin >> t;
	REP(i,t){
		cin >> N >> M;
		dict.clear();
		ans.clear();
		REP(j,N){
			cin >> tmp;
			dict.PB(tmp);
		}
		REP(j,M){
			int pt = -1;
			cin >> let;

			ans.PB("");

			REP(k,N){
				if(DEBUG){ cout << "-----------------------------" << endl; }
				if(DEBUG){ cout << "Choosed word: " << dict[k] << endl; }
				int now_pt = 0;
				string now_let = let;
				vector<char> let_koho;
				int wlen = dict[k].length();
				VS s_dict;
				REP(y,N){
					if ( dict[y].length() == wlen ) {
						s_dict.PB(dict[y]);
					}
				}

				REP(l,now_let.length()){
					let_koho.clear();
					REP(y,s_dict.size()){
						REP(x,s_dict[y].length()) {
							let_koho.PB(s_dict[y][x]);
						}
						unique(let_koho.begin(),let_koho.end());
					}

					REP(y,now_let.length()){
						if ( find(let_koho.begin(),let_koho.end(),now_let[y]) == let_koho.end() ) {
							now_let[y] = ' ';
						}
					}


					if ( now_let[l] == ' ' ) continue;
					VS new_dict;

					// now_let check
					if(DEBUG) cout << "now_let: " << now_let << endl;

					// s_dict check
					if(DEBUG){
						cout << "[" << (l+1) << "] s_dict: ";
						REP(z,s_dict.size()){ cout << s_dict[z] << " ";}
						cout << endl;
						cout << "choise: " << now_let[l] << endl;
						cout << endl;
					}


					int f_flag = 0;
					REP(n,dict[k].length()){
						if ( dict[k][n] == now_let[l] ) {
							f_flag = 1;
							break;
						}
					}
					if ( f_flag == 0 ) { now_pt++; }

					if(DEBUG){ cout << "f_flag: " << f_flag << endl; }

					if ( f_flag == 1 ) {
						REP(m,s_dict.size()){
							int flag = 0;

							if ( f_flag == 1 ) {
								REP(n,s_dict[m].length()){
									if ( ( s_dict[m][n] == now_let[l] && dict[k][n] != now_let[l] ) || 
										( s_dict[m][n] != now_let[l] && dict[k][n] == now_let[l] ) ) {
											flag = 1; break;
									}
								}
							}
							if ( flag == 0 ) {
								new_dict.PB(s_dict[m]);
							}

						}
					} else {
						REP(m,s_dict.size()){
							int flag = 0;
							REP(n,s_dict[m].length()){
								if ( s_dict[m][n] == now_let[l] ) {
									flag = 1; break;
								}
							}
							if ( flag == 0 ) {
								new_dict.PB(s_dict[m]);
							}
						}
					}


					s_dict = new_dict;

					if(DEBUG){
						cout << "now_pt: "<< now_pt << " (max:" << pt << ")" << endl;
					}

					if ( new_dict.size() == 1 ) {
						if ( pt < now_pt ) { pt = now_pt; ans[j] = new_dict[0]; }
						if(DEBUG){ cout << "found: " << new_dict[0] << endl; cout << "---------------" << endl; }

						break;
					}

				}

			}

		}
	
		cout << "Case #" << (i+1) << ": ";
		REP(j,ans.size()){
			cout << ans[j];
			if ( j != ans.size()-1 ) cout << " ";
		}
		cout << endl;
		if ( DEBUG ) { cout << "================================================" << endl; }
	}

	return 0;

}