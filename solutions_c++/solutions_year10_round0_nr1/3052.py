#include <iostream>
#include <vector>
#include <fstream>


using namespace std;

int n[10];
int state[10];

int k;

bool result[10000];

inline void clear() {
	for(int i=0; i<10; ++i) {
		n[i] = 0;
		state[i] = 0;
	}
}


bool solve(int num, int k) {
	clear();
	
	if(k == 0) return 0;
	
	state[0] = 1;
	
	for(int i=0; i<k; ++i) {
		for(int j=0; j<num; ++j) {
			if(state[j] == 1) {
				if(n[j]) n[j] = 0;
				else n[j] = 1;
			};
		
			if(j!=0) {
				if(state[j-1] == 1 && n[j-1] == 1) state[j] = 1;
				else state[j] = 0;
			}
		}
	}
	
	bool on = true;
	for(int i=0; i<num; ++i) {
		if(n[i] != 1) on = false;
	}
	return on;
}
	

int main() {
	int num;
	ifstream file("A-small-attempt0.in");
	file>>num;
	
	for(int i=0; i<num; ++i) {
		int nt, kt;
		file>>nt;
		file>>kt;
		
		result[i] = solve(nt, kt);
	}
	
	ofstream ofile("A-small-attempt0.out");
	for(int i=0; i<num; ++i) {
		ofile<<"Case #"<<i+1<<": ";
		if(result[i]) ofile<<"ON"<<endl;
		else ofile<<"OFF"<<endl;
	}
}
