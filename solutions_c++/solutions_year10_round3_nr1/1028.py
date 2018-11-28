#include <iostream>
#include <iomanip>
#include <cmath>
#include <vector>
#include <cstdlib>

#define REP(x,a,n) for(int x=(a); x<(n); x++)
#define rep(x,n) REP(x,0,n)

using namespace std;

class Wire {
	public:
	int A, B;
};

Wire wires[1000];

int compare(const void* a, const void* b) {
	return ((Wire*)b)->A - ((Wire*)a)->A;
}

void main2() {
	int N;
	cin >> N;

	rep(i,N) {
		cin >> wires[i].A >> wires[i].B;
	}

	qsort(wires, N, sizeof(Wire), compare);

	int inters = 0;
	rep(i,N-1) {
		int Ai = wires[i].A, Bi = wires[i].B;
		REP(j,i+1,N) {
			int Aj = wires[j].A, Bj = wires[j].B;
			if(Bj > Bi) inters++;
		}
	}
	cout << inters;
}

int main() {
	int T, caseno = 1;
	cin >> T;

	while(caseno <= T) {
		cout << "Case #" << caseno++ << ": ";
		main2();
		cout << endl;
	}
	return 0;
}
