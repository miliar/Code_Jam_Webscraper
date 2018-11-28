#include<iostream>
using namespace std;

int S, Q;
string names[102], queries[1001];

int table[1001][102];
int get(int index, int prev){
	
	if(index >= Q)return 0;
	if(table[index][prev] != -1)return table[index][prev];
	
	int best = 1e9;
	//stay
	if(queries[index] != names[prev])
		best = min(best, get(index+1, prev));	
	
	//change
	for(int i = 0 ; i < S ; i++)
		if(queries[index] != names[i])
			best = min(best, 1+get(index+1, i));
	
	return table[index][prev] = best;
}

int main(){
	
	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);	
	
	int tt; cin >> tt;
	char ch;
	
	for(int t = 0 ;t < tt ; t++){
		cin >> S;
		cin.get(ch);

		int i;
		for(i = 0 ; i < S ; i++)
			getline(cin, names[i]);
			
		cin >> Q;
		cin.get(ch);
		for(i = 0 ; i < Q ; i++)
			getline(cin, queries[i]);
		
		names[S] = queries[0];
		memset(table, -1, sizeof table);
		
		int r = Q == 0 ? 0 : get(0, S)-1;
		cout << "Case #" << t+1 << ": " << r << endl;
	}
	
	return 0;
}
