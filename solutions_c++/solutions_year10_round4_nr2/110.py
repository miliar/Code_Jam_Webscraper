#include <iostream>
#include <vector>
#include <algorithm>

#define VI vector<int>
#define INFTY 4294967296LL

using namespace std;

int tests;

int P,T;
vector<int> constraints;
vector<int> prices;

long long res;

void read_test(){
	cin >> P;
	T = (1 << P);
	constraints = VI(T,0);
	for(int i=0; i < T; i++)
		cin >> constraints[i];
	prices = VI(T-1,0);
	int pos = T - 1;
	for(int i=P-1; i>=0; i--){
		pos -= (1 << i);
		for(int j=0; j < (1 << i); j++)
			cin >> prices[pos+j];
	}
/*	
	for(int i=0; i < (1 << P)-1; i++)
		cout << prices[i] << " ";
	cout << endl;
*/
}

void solve_test(){
	vector<vector<long long> > dyn(2*T-1,vector<long long>(11,0));
	for(int i=0;i<T;i++)
	for(int j=0;j<=10;j++)
		dyn[T-1+i][j] = (constraints[i] >= j)?0:INFTY;
 	
	for(int i=T-2; i>=0; i--){
		int l = 2*i+1;
		int r = 2*i+2;
		for(int j=0; j<=10;j++){
			dyn[i][j] = dyn[l][j]+dyn[r][j]+prices[i];
			if (j < 10)
				dyn[i][j] = min(dyn[i][j],dyn[l][j+1]+dyn[r][j+1]);
		}
	}
	res = dyn[0][0];
}

void dump_sol(int i){
	cout << "Case #" << i << ": " ;
	cout << res << endl;
}

int main(){
	cin >> tests;
	for(int i=0; i < tests; i++){
		read_test();
		solve_test();
		dump_sol(i+1);
	}
}
