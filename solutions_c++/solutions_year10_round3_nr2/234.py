#include <iostream>
#include <cmath>


using namespace std;

int worst(int l,int p,int c) {
	//if (c * l >= p)
	//	return 0;
	//long long middle = floor(sqrt((double) l * (double) p));
	//return max(worst(l,middle,c),worst(middle,p,c)) + 1;
	double x = (double) p / (double) l;
	int n = ceil(log(x) / log((double)c));
	return ceil(log((double) n) / log(2.0));
}

int main() {
	int T;
	cin >> T;
	for (int nc = 1;nc <= T;++nc) {
		int L,P,C;
		cin >> L >> P >> C;
		cout << "Case #" << nc << ": " << worst(L,P,C) << endl;
	}
	return 0;
}