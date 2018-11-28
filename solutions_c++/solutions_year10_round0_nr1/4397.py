// GoogleJam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>

using namespace std;

bool snappersA[31];
bool snappersB[31];

void snapper(int id)
{
	int n, k;
	cin >> n >> k;

	bool * snappers = snappersA, * oldsnappers = snappersB, *tmp;
	bool power;

	for (int i = 0; i < n; ++i) {
		snappers[i] = false;
		oldsnappers[i] = false;
	}
	for (int j = 0; j < k; ++j) {
		power = true;
		int i = 0;
		while (power && (i < n)) {
			snappers[i] = !oldsnappers[i];
			power = oldsnappers[i];
			/*for (int r = 0; r < n; ++r) {
				cout << oldsnappers[r];
			}
			cout << " ";
			for (int r = 0; r < n; ++r) {
				cout << snappers[r];
			}
			cout << endl;*/
			++i;
		}
		for (; i < n; ++i) {
			snappers[i] = oldsnappers[i];
		}
		//cout << "-----" << i << endl;
		tmp = oldsnappers;
		oldsnappers = snappers;
		snappers = tmp;
	}
	power = true;
	for (int i = 0; power && (i < n); ++i) {
		power = oldsnappers[i];
	}
	cout << "Case #" << (id + 1) << ": " << (power? "ON": "OFF") << endl;
}

int _tmain(int argc, _TCHAR* argv[])
{
	int cases;
	cin >> cases;

	for (int i = 0; i < cases; ++i) {
	  snapper(i);
	}

	return 0;
}

