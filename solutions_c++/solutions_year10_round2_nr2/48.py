#include <iostream>
#include <vector>
#include <algorithm>

#define VI vector<int>

using namespace std;

int tests;

long long N,K,B,T;
vector<pair<long long,long long> > chicks;

long long res;

void read_test(){
	cin >> N >> K >> B >> T;
	chicks.resize(N);
	for(int i=0; i<N; i++)
		cin >> chicks[i].first;
	for(int i=0; i<N; i++)
		cin >> chicks[i].second;
}

void solve_test(){
	int done = 0;
	int blockers = 0;
	res = 0;
	for(int i=N-1; i >= 0 && done < K; i--){
		if (chicks[i].first + chicks[i].second*T < B)
			blockers++;
		else{
			res += blockers;
			done++;	
		}	
	}
	if (done < K)
		res = -1;
}

void dump_sol(int i){
	cout << "Case #" << i << ": " ;
	if (res != -1)		
		cout << res << endl;
	else
		cout << "IMPOSSIBLE" << endl; 
}

int main(){
	cin >> tests;
	for(int i=0; i < tests; i++){
		read_test();
		solve_test();
		dump_sol(i+1);
	}
}
