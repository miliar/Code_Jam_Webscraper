#include <algorithm>
#include <sstream>
#include <iostream>
#include <map>
#include <cstring>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <iostream>
#include <fstream>
using namespace std;

#define rep(i,n) for(int i = 0;i<n;i++)
#define FOR(i,s,e) for (int i = int(s); i != int(e); i++)
#define FORIT(i,c) for (typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define ISEQ(c) (c).begin(), (c).end()

using std::cerr;
using std::cout;
using std::endl;
using std::string;
using std::vector;
char mapping[30];

int main() {
	int T;
	cin >> T;
	rep(cnt,T){
		vector<int> scores;
		int N,S,P;
		unsigned long ans = 0;
		cin >> N >> S >> P;
		rep(j,N){
			int t;
			cin >> t;
			scores.push_back(t);
		}
		rep(i,N){
			if(scores[i] == 0 && P == 0){
				ans++;
				continue;
			}else if(scores[i] == 0 && P != 0){
				continue;
			}
			if(scores[i] % 3 == 2){
				int n = scores[i] / 3;
				if(n + 1 >= P){
					ans++;
				}else if(n + 2 >= P && S>0){
					ans++;
					S--;
				}
			}else if(scores[i] % 3 == 1){
				int n = scores[i] / 3;
				if(n + 1 >= P){
					ans++;
				}
			}else{
				int n = scores[i] / 3;
				if(n >= P){
					ans++;
				}else if(n + 1 >= P && S>0){
					ans++;
					S--;
				}
			}
		}
		cout << "Case #" << cnt+1 << ": " << ans << endl;
	}
    return 0;
}

