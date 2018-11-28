#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main () {
	freopen("E:/algo/A-large.in","r",stdin);
	freopen("E:/algo/A_out.txt","w",stdout);

	int testNumber = 0;
	scanf("%d", &testNumber);
	for (int testIndex = 0; testIndex < testNumber; testIndex++) {
		int plugNum = 0;
		int snapNum = 0;
		scanf ("%d %d", &plugNum, &snapNum);
		int cycle = 1 << plugNum;
		if ((snapNum % cycle) == cycle - 1) {
			printf ("Case #%d: ON\n", testIndex + 1);
		} else {
			printf ("Case #%d: OFF\n", testIndex + 1);
		}
	}
	fflush(stdout);
	return 0;
}