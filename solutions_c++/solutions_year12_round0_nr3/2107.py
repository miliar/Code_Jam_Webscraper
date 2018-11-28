#include <fstream>
#include <iostream>
#include <string>

using namespace std;

int R(int digits, int X, int dA[], int dB[], int d[], bool offset = false) {

	bool below = false, above = false, self = false, stopSelf = false;
	int i0 = 0, i = (offset ? X : 0), j = (offset ? 0 : X);
	while(d[i] != -1 && i0 < digits) {
		if(dA[i0] < d[i] && !below) below = true;
		if(dA[i0] > d[i] && !below) { /*cout << "A" << endl;*/ return 0; }
		if(d[j] == -1) stopSelf = true;
		if(d[j] != -1 && d[j] > d[i] && !self && !stopSelf) { if(offset)  self = true; else { /*cout << "X" << endl;*/ return 0; } }
		if(d[j] != -1 && d[j] < d[i] && !self && !stopSelf) { if(!offset) self = true; else { /*cout << "Y" << endl;*/ return 0; } }
		if(dB[i0] > d[i] && !above) above = true;
		if(dB[i0] < d[i] && !above) { /*cout << "B" << endl;*/ return 0; }
		i0++; i = (i+1) % digits; j = (j+1) % digits;
		//cout << "[" << i0 << "," << i << "," << j << "]" << endl;
	}
	int oldset = i;
	if(i0 == digits) {
		if(!self) return 0;
		if(offset) {
			/*cout << "YES ";
			for(i = 0; i < digits; i++)
				cout << d[i] << " ";
			cout << endl;*/
			for(int Y = 1; Y < X; Y++) {
				bool match = true;
				for(int k = 0; match && (k < digits); k++)
					if(d[(k+X)%digits] != d[(k+Y)%digits]) match = false;
				if(match) return 0;
			}
			return 1;
		} else
			return R(digits, X, dA, dB, d, true);
	} else {
		int r = 0;
		int min = (below ? 0 : dA[i0]), max = (above ? 9 : dB[i0]);
		if(!stopSelf && !self && offset && d[j] != -1)  min = (min < d[j]) ? d[j] : min;
		if(!stopSelf && !self && !offset && d[j] != -1) max = (max > d[j]) ? d[j] : max;

		//if(d[0] == 4 && d[1] == -1) cout << min << " ---------- " << max << "- " << above << below << endl;

		for(d[oldset] = min; d[oldset] <= max; d[oldset]++)
			r += R(digits, X, dA, dB, d, offset);
		d[oldset] = -1;
		return r;
	}
}

int main(int argc, char ** argv) {
	ifstream input(argv[1]);
	ofstream out("output.out");
	int noIn;
	string s;

	input >> noIn;
	getline(input, s);

	for(int i = 1; i <= noIn; i++) {
		out << "Case #" << i << ": ";
		
		int A, B;
		input >> A >> B;
		int digits = 1, temp = 9;
		while(temp < A) { temp = 10*temp + 9; digits++; }
		cout << A << " -> " << B << " [" << digits << "] ";

		int d[digits], dA[digits], dB[digits];
		for(int j = digits-1; j >= 0; j--) {
			dA[j] = A%10; dB[j] = B%10; A /= 10; B /= 10;
			d[j] = -1;
		}

		int t = 0;
		for(int X = 1; X < digits; X++) {
			t += R(digits, X, dA, dB, d);
		}
		
		cout << t << endl;
		out << t << endl;
	}

}
