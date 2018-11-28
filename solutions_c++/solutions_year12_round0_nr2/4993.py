#include <iostream>
#include <stdlib.h>
#include <string>
#include <string.h>

using namespace std;

int main() {
	int tests;
	int round = 0;
	cin >> tests;
	int result[105];

	while(round < tests) {
		int num;
		int suprise;
		int best;

		cin >> num;
		cin >> suprise;
		cin >> best;
		int * employer = new int[num];
		int total = 0;
		int maybe = 0;
		for(int i = 0; i < num; i ++) {
			cin >> employer[i];
			if (employer[i] >= best * 3 - 2) {
				total ++;
			}
			else if (employer[i] >= best * 3 -4 && best * 3 - 4 > 0) {
				if (maybe < suprise)
					maybe ++;
			}
		}
		result[round] = total + maybe;
		round ++;
		delete employer;
	}

	for (int i = 0 ; i < round; i ++) {
		cout << "Case #" << (i+1) << ": " << result[i] << endl;
	}

	system("PAUSE");
	return 0;
}