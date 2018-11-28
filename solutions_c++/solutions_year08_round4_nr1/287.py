
#include <iostream>
#include <vector>
typedef long long LL;
using namespace std;

int tbl[10001][2];
int gate[10001][2];
#define IMPOSSIBLE (1000000)

int is_valid(int type, int ans, int v1, int v2){
	return ans == (type ? (v1&v2) : (v1|v2));
}
int dfs(int id, int trg){
	int &ans = tbl[id][trg];
	if(ans != -1) return ans;
	ans = IMPOSSIBLE;
	for(int gate_type = 0; gate_type < 2; gate_type++){
		if(gate[id][0] != gate_type && !gate[id][1]) continue;
		int penalty = gate[id][0] != gate_type;
		for(int t1 = 0; t1<2; t1++)
			for(int t2=0; t2<2; t2++){
				if(!is_valid(gate_type, trg, t1,t2)) continue;
				int v1 = dfs(id*2, t1);
				int v2 = dfs(id*2+1, t2);
				if(v1 == IMPOSSIBLE || v2 == IMPOSSIBLE) continue;
				ans = min(ans, penalty + v1 + v2);
			}
	}
	return ans;
}


int main(void){
	int cases;
	cin >> cases;
	for(int case_no=1; case_no<=cases; case_no++){
		int M, V;
		cin >> M >> V;
		int nGate = (M-1)/2;
		memset(tbl, 0xFF, sizeof(tbl));
		for(int i=1; i<=nGate; i++)
			cin >> gate[i][0] >> gate[i][1];
		for(int i=nGate+1; i<=M; i++){
			int t;
			cin >> t;
			tbl[i][t] = 0;
			tbl[i][1-t] = IMPOSSIBLE;
		}
		int ans = dfs(1, V);
		cout << "Case #"<<case_no<<": ";
		if(ans == IMPOSSIBLE){
			cout << "IMPOSSIBLE";
		}else{
			cout << ans;
		}
		cout << endl;
	}
	return 0;
}
