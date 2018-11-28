#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int tests;

int n, k;
int on;

void read_test(){
	cin >> n >> k;
}

void solve_test(){
	on = ((k+1) % (1 << n) == 0);
}

void dump_sol(int i){
	cout << "Case #" << i << ": " ;
	cout << (on?"ON":"OFF") << endl;
}

int main(){
	cin >> tests;
	for(int i=0; i < tests; i++){
		read_test();
		solve_test();
		dump_sol(i+1);
	}
}
