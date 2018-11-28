#include<iostream>
using namespace std;

int mod(int a) {
    if (a<0) return -a;
	return a;
}

int move(int p, int &apos, int &await, int &bwait) {
    int pressTime = mod(p - apos) + 1;
	pressTime -= await;
	if(pressTime < 1) pressTime = 1;
	bwait += pressTime;
	await = 0;
	apos = p;
	return pressTime;
}

int main() {
	int T, C=1;
	cin >> T;
	
	while(T--) {
	    int N, P;
		char R;
		int opos=1, bpos=1, owait=0, bwait=0, time=0;
		cin >> N;
		
		while(N--) {
		    cin >> R >> P;
			
			switch(R) {
			    case 'O' :
				    time += move(P, opos, owait, bwait);
					break;
				case 'B' :
				    time += move(P, bpos, bwait, owait);
					break;
			}
		}
		
		cout << "Case #" << C++ << ": " << time << endl;
	}
}
