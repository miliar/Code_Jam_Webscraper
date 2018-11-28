#include <iostream>
#include <cstdio>
#include <fstream>
using namespace std;
#define abs(a) ((a)>0?(a):-(a))

int lastpos[2], lasttime[2];

int main() {
	int T, N;
	cin >> T;
	for (int t=1; t<=T; t++) {
		lastpos[0]=1;
		lastpos[1]=1;
		lasttime[0]=0;
		lasttime[1]=0;
		int time=0;
		cin >> N;
		for (int n=1; n<=N; n++) {
			char c;
			int pos;
			cin >> c >> pos;
			int robot=(c=='O'?0:1);
			int delay= abs(pos-lastpos[robot])+1;
			if (delay <= time-lasttime[robot]) {
				lasttime[robot]=time;
				lastpos[robot]=pos;
				time++;
			}
			else {
				time=lasttime[robot]+delay;
				lasttime[robot]=time;
				lastpos[robot]=pos;
				time++;
			}
		}
		
		cout << "Case #" << t << ": " << time-1 << endl;
	}
	
		
	return 0;
}

