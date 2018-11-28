#include <iostream>
using namespace std;

int main() {
	int r[31];
	
	r[2] = 27;
	r[3] = 143;
	r[4] = 751;
	r[5] = 935;
	r[6] = 607;
	r[7] = 903;
	r[8] = 991;
	r[9] = 335;
	r[10] = 47;
	r[11] = 943;
	r[12] = 471;
	r[13] = 55;
	r[14] = 447;
	r[15] = 463;
	r[16] = 991;
	r[17] = 95;
	r[18] = 607;
	r[19] = 263;
	r[20] = 151;
	r[21] = 855;
	r[22] = 527;
	r[23] = 743;
	r[24] = 351;
	r[25] = 135;
	r[26] = 407;
	r[27] = 903;
	r[28] = 791;
	r[29] = 135;
	r[30] = 647;
	
	int casen;
	cin >> casen;
	for(int casei=1;casei<=casen;casei++) {
		int a;
		cin >> a;
		printf("Case #%d: %03d\n", casei,r[a]);
	}
	
	
	
	
	return 0;
}
