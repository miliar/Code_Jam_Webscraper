
#include <iostream>
#include <vector>
#include <map>
#include <set>
using namespace std;
#define fu(i,m,n) for(int i=m; i<n; i++)


int main(void) {
	int T;
	cin >> T;
	fu(ts,1,T+1) {
		//map<string,int> engines;
		cout << "Case #" << ts << ":";
		int N,M;
		cin >> N >> M;
		vector<int> malted(N);
		vector<int> fixed(N);
		vector<set<int> > left(M);
		vector<vector<int> > right(M);
		fu(i,0,M) {
			int T;
			cin >> T;
			fu(t,0,T) {
				int X,Y;
				cin >> X >> Y;
				if(Y) right[i].push_back(X-1);
				else left[i].insert(X-1);
			}
		}
		bool good=true;
		fu(i,0,N) fu(j,0,M) if(good) {
			if(left[j].size()==0 && right[j].size()) {
				int ma=right[j][0];
				if(fixed[ma]) {
					continue;
				}
				//cout << "Malting " << ma << endl;
				fixed[ma]=1;
				malted[ma]=true;
				fu(j,0,M) {
					left[j].erase(ma);
					if(left[j].size()==0 && right[j].size()==0) {// && fixed[right[j][0]] && !malted[right[j][0]]) {
						good=false;
						break;
					}
				}
				break;
			}
		}
		//fu(i,0,M) cout << cust[0][i] << " " << cust[1][i] << endl;
		if(!good) {
			cout << " IMPOSSIBLE" << endl;
		} else {
			fu(i,0,N) cout << " " << malted[i];
			cout << endl;
		}
	}
}
