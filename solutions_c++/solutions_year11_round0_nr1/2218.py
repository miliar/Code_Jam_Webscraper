#include <iostream>

using namespace std;

int bots(int N, char R[], int P[]) {
 	int i;
	int O = 1, B = 1;
	int freeOmoves = 0, freeBmoves = 0;
	int total = 0, diff;
	for (i=0; i < N; ++i) {
		if (R[i]=='O') {
			diff = abs(P[i] - O) - freeOmoves;
			if (diff < 0)
				diff = 0;
			//cout << "O(+" << diff << ") ";
			total += diff+1;
			freeBmoves += diff+1;
			freeOmoves = 0;
			O = P[i];
		} else {
			diff = abs(P[i] - B) - freeBmoves;
			if (diff < 0)
				diff = 0;
			total += diff+1;
			//cout << "B(+" << diff << ") ";
			freeOmoves += diff+1;
			freeBmoves = 0;
			B = P[i];
		}
	}
	return total;

}

int main() {

  int T, N, K, B;
  cin >> T;
  int P[100];
  char R[100];
  for (int c=0; c < T; ++c) {
	cin >> N;
	for (int j = 0; j < N; ++j) {
		cin >> R[j];
		cin >> P[j];
	}
	   
	cout << "Case #" << c+1 << ": ";
	int t = bots(N, R, P);
	cout << t << "\n";
  }

}
