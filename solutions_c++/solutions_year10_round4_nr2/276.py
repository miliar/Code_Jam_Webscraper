#include<cstring>
#include<algorithm>
#include<iostream>
#include<vector>
#include<cstdio>
#include<set>
using  namespace std;
typedef long long ll;
int debe[10000];
int zzz;
int permit[10000];
ll inf = 1LL << 60;
ll dp[3000][20];
ll costo[3000];
bool seen[3000][20];
ll calcula(int node, int from, int to, int jugados){
	if(from == to){
		if(debe[from] > jugados) return inf;
		else return 0;
	}
	if(seen[node][jugados]) return dp[node][jugados];
	ll res = inf;
	int mid = (from + to) / 2;
	//juega
	res = min(res, costo[node] + calcula(node * 2 + 1, from, mid, jugados + 1) 
				   + calcula(node * 2 + 2, mid + 1, to, jugados + 1));
	//no juega
	res = min(res, calcula(node * 2 + 1, from, mid, jugados) 
		     + calcula(node * 2 + 2, mid + 1, to, jugados));
	seen[node][jugados] = true;
	return dp[node][jugados] = res;	
}
int main(){
	int casos; cin >> casos;
	for(int t = 1; t <= casos; t++){
		int P; cin >> P;
		for(int i = 0; i < (1 << P); i++) scanf("%d", &permit[i]);
			
		vector<vector<int> > vec(P);
		int chen=0;
		for(int i = 0; i < P; i++){
			int sz = 1 << (P - 1 - i);
			vec[i] = vector<int> (sz);
			for(int j = 0; j < sz; j++) scanf("%d", &vec[i][j]);
		}
		int nodo = 0;
		for(int i = vec.size() - 1; i >= 0; i--){
			for(int j = 0; j < vec[i].size(); j++)
				costo[nodo++] = vec[i][j];
		}
	//	for(int i = 0; i < nodo; i++) cout << costo[i] << endl;
		
		for(int i = 0; i < (1 << P); i++){
			int avanza = P - permit[i];
			debe[i] = avanza;
		}		
		memset(seen, 0, sizeof seen);
		ll res = calcula(0, 0, (1 << P) - 1, 0);
		
		printf("Case #%d: %lld\n", t, res);
	}
}
