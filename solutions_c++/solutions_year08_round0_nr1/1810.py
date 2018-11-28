#include <iostream>
#include <vector>
#include <string>
#include <sstream> 
#include <algorithm> 
#include <map>
using namespace std;
typedef long long ll; 

#define FOR(i,a,b) for(int i=(a);i<(b);++i) 
#define REP(i,n) FOR(i,0,n) 
// abbreviation 
#define all(x) (x).begin(),(x).end() 
#define sz(x) int((x).size())

int main() {
	int tn;
	int S, Q;
	map<string,int> engine;
	vector<string> query;
	cin >> tn; string buf;
	int table[1000][100];
	for(int cc=1;cc<=tn;++cc) {
		cin >> S; getline(cin,buf);
		engine.clear();
		REP(i,S) {
			getline(cin, buf);
			engine[buf] = i;
		}

		cin >> Q; getline(cin,buf);
		query.resize(Q);
		vector<int> ennum(Q);
		REP(i,Q) { 
			getline(cin, query[i]);
			ennum[i] = engine[query[i]];
		}
		int ret = 987654321;
		REP(i,S) if(ennum[0]!=i) table[0][i] = 0; else table[0][i] = 987654321;
		FOR(i,1,Q) {
			REP(j,S) {
				if(ennum[i]==j) table[i][j] = 987654321;
				else { table[i][j] = table[i-1][j];
					REP(k,S) {
						if(j!=k) {
							table[i][j] <?= table[i-1][k] + 1;
						}
					}
				}
			}
		}
		if(Q>0) {
			REP(i,S) {
				ret <?= table[Q-1][i];
			}
		}
		else ret = 0;
		printf("Case #%d: ",cc);
		cout << ret;
		printf("\n");
	}	
}
