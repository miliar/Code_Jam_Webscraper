#include <iostream>
#include <vector>
using namespace std;

const int MAX_N = 100;
int datanum;
char T[MAX_N];
int N[MAX_N];
int p;
int caseno;

int getNextB(){
	for(int i=p ; i<datanum ; i++){
		if(T[i]=='B') return N[i];
	}
	return -1;
}

int getNextO(){
	for(int i=p ; i<datanum ; i++){
		if(T[i]=='O') return N[i];
	}
	return -1;
}


void solve(){

	int step = 0;
	int orangep = 1;
	int bluep = 1;

	p=0;
	char c = T[p];
	int n = N[p];
	
	while(p < datanum){

		// next button is orange
		if(c=='O'){
			//orange robot
			if(n==orangep){
				p++;
				c = T[p];
				n = N[p];
			}
			else if(n>orangep){
				orangep++;
			}
			else orangep--;

			//blue robot
			int k = getNextB();
			if     (k>bluep) bluep++;
			else if(k<bluep) bluep--;

		}
		// next button is blue
		else{
			//blue robot
			if(n==bluep){
				p++;
				c = T[p];
				n = N[p];
			}
			else if(n>bluep){
				bluep++;
			}
			else bluep--;

			//orange robot
			int k = getNextO();
			if      (k>orangep) orangep++;
			else if (k<orangep) orangep--;

		}
		step++;
	}

	cout << "Case #" << caseno << ": " << step << endl;
}

int main(){
	int casenum;
	cin >> casenum;

	for(caseno=1 ; caseno <= casenum ; caseno++){

		cin >> datanum;
		for(int i=0 ; i<datanum ; i++){
			cin >> T[i];
			cin >> N[i];
		}

		solve();
	}
}