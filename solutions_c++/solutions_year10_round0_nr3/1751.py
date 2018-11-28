
#include <fstream>
//#include <iostream>
using namespace std;
ifstream cin;
ofstream cout;
int main() {
	
	cin.open("C-large.in");
	cout.open("C-large.out");

	int T;
	cin >> T;
	int R,K,N;
	int A[1000];
	int Tag[1000];
	for (int i=1; i<=T; i++) {
		long long totalno=0;
		cin >> R >> K >> N;
		for (int j=0; j<N; j++) {
			cin >> A[j];
			totalno += A[j];
			Tag[j] = 0;
		}
		long long count=0;
		int rounds = 0;
		int curpos = 0;
		long long ppl=0;
		while (Tag[curpos] != 1 && rounds<R) {
			Tag[curpos] = 1;
			while (true) {
				count += A[curpos];
				if (count > K || count > totalno) { count-= A[curpos]; rounds++; break;} else { curpos = (++curpos%N); }
			}
			ppl += count;
			count = 0;
		}
		cout << "Case #"<<i<<": ";
		//now that it has stabilized
		//if rounds are R send else
		if (rounds == R) cout << ppl; else {
			//get stable value
			long long pp2=0;
			long long rounds2 =0;
			int initpos = curpos;
			bool fx = false;
			while (curpos != initpos || fx == false) {
				fx = true;
				while (true) {
					count += A[curpos];
					if (count > K || count > totalno) { count-= A[curpos]; rounds2++; break;} else { curpos = (++curpos%N); }
				}
				pp2 += count;
				count = 0;
			}
			//stable number of rounds is rounds2
			//stable number of ppl / X rounds is pp2
			long long ppl2 = ((long long)((R-rounds)/rounds2))*pp2 + ppl;
			for (int j=0; j<((R-rounds)%rounds2); j++) {
				while (true) {
					count += A[curpos];
					if (count > K || count > totalno) { count-= A[curpos]; break;} else { curpos = (++curpos%N); }
				}
				ppl2+= count;
				count =0;
			}
			cout << ppl2;
		}
		cout << endl;
	}
}