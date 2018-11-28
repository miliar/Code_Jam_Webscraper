#include <iostream>
#include <vector>
#include <map>
#include <utility>
#include <set>
using namespace std;


int getDigits(int N) {
	int cnt = 0;
	while (N > 0) {
		N = N /10;
		cnt++;
	}
	return cnt;
}
int power10[10] = {1, 10,100,1000,10000,100000,1000000,10000000};

void valid(int totDigits, int N, int A, int B, set<pair<int,int> >& uniq) {
	int cnt = 0;
	
	// test every permutation
	for (int i = 1; i < totDigits; ++i) {
		//   i...N-1,0...i-1
		int powersTen = power10[i];
		int lastN = N % powersTen;
		if (lastN != 0) {
			int firstN = N / powersTen;
			int newNumber = firstN + lastN*power10[totDigits- i];
			if (newNumber > N && newNumber <=B && newNumber >= A) {
				uniq.insert(pair<int,int>(N, newNumber));
			}
		}
	}
}

int main() {
	int n_cases;
	cin >> n_cases;
	int A, B;
	for (int c = 1; c <= n_cases; ++c) {
		cin	>> A >> B;
		int nrDigits = getDigits(A);
		set<pair<int, int> > uniq;
		for (int i = A; i <= B; ++i) {
			valid(nrDigits, i, A, B, uniq);
		}
		cout << "Case #" << c << ": " <<uniq.size() << endl;	
	}
}