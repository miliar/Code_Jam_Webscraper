#include <iostream>
#include <fstream>

using namespace std;

void line(int p, int S, int *total, int N) {
	int y = 0;
	int min = p+(p-1)*2;
	int minS = min-2;

	if(min < 0) min = p;
	if(minS < 0) minS = p;

	for(int i=0;i<N;i++) {
		if(total[i] >= min) {
			y++;
		} else if(S && total[i] >= minS) {
			S--;
			y++;
		}
	}
	cout << y << endl;
}

int main() {
	fstream file;
	file.open("B-large.in", fstream::in);

	int T;
	file >> T;

	for(int i=1;i<=T;i++) {
		int N, S, p;
		file >> N;
		file >> S;
		file >> p;

		int total[N];
		for(int j=0;j<N;j++) file >> total[j];

		cout << "Case #" << i << ": ";
		line(p,S,total,N);
	}
}
