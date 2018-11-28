#include<iostream>
#include<algorithm>	
#include<map>
#include<string>

#define INF ((1 << 30) - 1)

using namespace std;

int DP[1001][100];
map<string,int> sEngines;

int main() {
	int N, Q, S, s, idx, ms;
	string name;
	
	cin >> N;
	
	for(int ni = 0; ni < N; ni++) {
		cin >> S;
		getline(cin, name);
		
		sEngines.clear();
		
		for(int si = 0; si < S; si++) {
			getline(cin, name);
			sEngines[name] = si;
		}
	
		cin >> Q;
		getline(cin, name);
		
		memset(DP, -1, sizeof(DP));
		
		for(int i = 0; i < S; i++) {
			DP[0][i] = 0;
		}
		
		for(int qi = 0; qi < Q; qi++) {
			getline(cin, name);
			idx = sEngines[name];
			
			for(int i = 0; i < S; i++) {
				if(idx == i) {
					DP[qi+1][idx] = INF;
				} else {
					DP[qi+1][i] = min(DP[qi][i], DP[qi][idx] + 1);
				}
			}
		}
		
		ms = INF;
		
		for(int i = 0; i < S; i++) {
			ms = min(ms, DP[Q][i]);
		}
		
		cout << "Case #" << (ni+1) << ": " << ms << endl;
	}
}
