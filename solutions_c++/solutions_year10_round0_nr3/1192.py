#include <iostream>
#include <vector>
#include <algorithm>

#define VI vector<int>

using namespace std;

int tests;

int rides, cap, n;
VI groups;

int res;

void read_test(){
	cin >> rides >> cap >> n;
	groups = VI(n);
	for(int i=0; i<n; i++)
		cin >> groups[i];
}

void solve_test(){
	int s = 0;
	for(int i=0; i<n; i++) s += groups[i];
	if (s <= cap){
		res = rides*s;
		return;		
	}

	res = 0;
	int i=0;
	for(int ride=0; ride < rides; ride++){
		s = 0;
		while (s <= cap){
			s += groups[i];
			i = (i+1)%n;
		}
		i = (i+n-1)%n;
		s -= groups[i];
		res += s;
	}
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
