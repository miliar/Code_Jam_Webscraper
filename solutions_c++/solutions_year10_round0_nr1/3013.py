#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	int T, t, N, K, x, state;
	int clicks[32];

	ifstream myfile ("input.in");
	ofstream output ("output.txt", ios::trunc);
	myfile >> T;

	clicks[1]=1;
	for (x=2;x<=30;x++) {
		clicks[x] = clicks[x-1] * 2 + 1;
		cout << x << "   " << clicks[x] << "\n";
	}

	for (t=1;t<=T;t++) {
		myfile >> N >> K;
		state = 0;
		if ((K+1) % (clicks[N] + 1) == 0) state =1;

		if (state == 0) output << "Case #" << t << ": "<< "OFF" << "\n";
		else output << "Case #" << t << ": "<< "ON" << "\n";
	}
	return 0;
}
