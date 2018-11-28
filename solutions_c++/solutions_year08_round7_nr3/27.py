#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int M, Q;
double P[31][4];
int C;
double result[9999];

void trial(int k, double current) {
	if(k == Q) {
		result[C ++] = current;
		return;
	}
	for(int i=0; i<4; i++)
		trial(k+1, current * P[k][i]);
}

int main(int argc, char* argv[]) {
	int n;
	cin >>n;
	for(int i=0; i<n; i++) {
		cin >>M >>Q;
		for(int j=0; j<Q; j++)
			for(int k=0; k<4; k++)
				cin >>P[j][k];
		C = 0;
		trial(0, 1);
		sort(result, result + C);
		double prob = 0;
		int start = C-M;
		if(start < 0) start = 0;
		for(int j = start; j < C; j++)
			prob += result[j];
		cout <<"Case #" <<i+1 <<": " <<prob <<endl;
	}
	return 0;
}