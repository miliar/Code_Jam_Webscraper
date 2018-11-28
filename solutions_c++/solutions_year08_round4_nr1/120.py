#include<set>
#include<iostream>
using namespace std;

int type[10005];
int isleaf[10005];
int ischange[10005];
int value[10005];

int N;

int a(int x, int y){
	return !x||!y?0:1;
}
int o(int x, int y){
	return !x&&!y?0:1;
}

int INF = 1e9;
int table[10005][2];

int get(int index, int v){
	
	if(isleaf[index])return v == value[index] ? 0 : INF;
	if(table[index][v] != -1)return table[index][v];
	
	int best = INF;
	for(int i = 0 ; i < 2 ; i++)	//or, and
		for(int j = 0 ; j < 2 ; j++)
			for(int k = 0 ; k < 2 ; k++){
								
				int cv = i==0?o(j,k):a(j,k);
				if(cv != v)continue;
				if(type[index] != i && !ischange[index])continue;
				
				int current = type[index] == i ? 0 : 1;

				int c1 = get(2*index, j);
				int c2 = get(2*index+1, k);
				current += c1 + c2;
				best = min(best, current);
			}
	return table[index][v] = best;
}

int main(){

	//freopen("1.in", "rt", stdin);
	//freopen("A-small.in", "rt", stdin);
	//freopen("A-small.out", "wt", stdout);
	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);
	
	int tt; cin >> tt;
	for(int t = 0 ; t < tt ; t++){
		
		int V;
		cin >> N >> V;
		memset(type, -1, sizeof type);
		memset(isleaf, 0, sizeof isleaf);
		memset(ischange, 0, sizeof ischange);
		memset(value, -1, sizeof value);
		
		int i, j;
		for(i = 1 ; i <= (N-1)/2 ; i++){
			int x, y; cin >> x >> y;
			type[i] = x;
			ischange[i] = y;
		}
		for(j = 0 ; j < (N+1)/2 ; j++){
			cin >> value[i];
			isleaf[i] = true;
			i++;
		}
		
		memset(table, -1, sizeof table);
		int r = get(1, V);
		cout << "Case #" << t+1 << ": ";
		if(r == INF)cout << "IMPOSSIBLE" << endl;
		else cout << r << endl;
	}

	return 0;	
}
