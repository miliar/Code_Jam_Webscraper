#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstring>
#include <stdint.h>
#include <list>
#include <queue>
#include <stack>
#include <cstdio>
#include <cstdlib>
using namespace std;

void handleCase(int T)
{
	int N;
	int current_O = 1, current_B = 1;
	int next_O, next_B;
	int nsteps = 0, O_steps = 0, B_steps = 0;
	cin >> N;
	for (int i = 0; i < N; i++) {
		string inp;
		cin >> inp;
		if (inp == "O") {
			cin >> next_O;
			O_steps += abs(current_O - next_O);
			if (O_steps > nsteps) {
				O_steps++;
				nsteps = O_steps;
			} else {
				nsteps++;
				O_steps = nsteps;
			}
			current_O = next_O;
		} else if (inp == "B") {
			cin >> next_B;
			B_steps += abs(current_B - next_B);
			if (B_steps > nsteps) {
				B_steps++;
				nsteps = B_steps;
			} else {
				nsteps++;
				B_steps = nsteps;

			}
			current_B = next_B;
		} else {
			cerr << "Invalid input!!!";
			break;
		}
	}
	cout << "Case #" << T + 1<< ": " << nsteps << endl;

}

int main(int argc, char *argv[])
{
	int N;

	cin >> N;

	for (int i = 0; i < N; i++) {
		handleCase(i);
	}
	return 0;
}
