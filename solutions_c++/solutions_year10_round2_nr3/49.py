#include <iostream>
#include <vector>
#include <algorithm>

#define VI vector<int>

using namespace std;

int tests;


long long res;
long long n;

#define N_MAX 501
#define MOD 100003

vector<long long> total(N_MAX,0);

void gen_answers(){
	long long binom[N_MAX][N_MAX];
	for(int i=0; i < N_MAX; i++){
		binom[i][0] = 1;
		for(int j=1; j < i; j++)
			binom[i][j] = (binom[i-1][j-1]+binom[i-1][j]) % MOD;
		binom[i][i] = 1;
	} 
	
	long long dyn[N_MAX][N_MAX];	
	for(int i=0; i < N_MAX; i++)
	for(int j=0; j < N_MAX; j++)
		dyn[i][j] = 0;
	
	dyn[1][0] = 1;
	for(int i=2; i < N_MAX; i++){
		for(int j=1; j < i; j++){
			dyn[i][j] = 0;
			for(int k=0; k < j;k++)
				if (j-k <= i-j)
					dyn[i][j] = (dyn[i][j] + (dyn[j][k] * binom[i-j-1][j-k-1]) % MOD) % MOD;
			//cout << i << " " << j << " " << dyn[i][j] << endl;
			total[i] = (total[i] + dyn[i][j]) % MOD;
		}
	//cout << i << " " << total[i] << endl; 	
	}
}

void read_test(){
	cin >> n;
}

void solve_test(){
	res = total[n];
}

void dump_sol(int i){
	cout << "Case #" << i << ": " ;
	cout << res << endl;
}

int main(){
	gen_answers();
	cin >> tests;
	for(int i=0; i < tests; i++){
		read_test();
		solve_test();
		dump_sol(i+1);
	}
}
