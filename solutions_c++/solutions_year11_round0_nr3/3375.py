//#include <sstream>
#include "stdio.h"
#include <string>
#include <algorithm>
#define dprintf if(false) printf

using namespace std;

int best_value = 0;
long long pow2[] = {1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824, 2147483648, 4294967296, 8589934592, 17179869184, 34359738368, 68719476736, 137438953472, 274877906944, 549755813888, 1099511627776, 2199023255552, 4398046511104, 8796093022208, 17592186044416, 35184372088832, 70368744177664, 140737488355328, 281474976710656, 562949953421312, 1125899906842624, 2251799813685248, 4503599627370496, 9007199254740992, 18014398509481984, 36028797018963968, 72057594037927936, 144115188075855872, 288230376151711744, 576460752303423488, 1152921504606846976, 2305843009213693952, 4611686018427387904};

int pow();

string toBin(int a) {
	bool begun = false;
	string str = "";

	for(int i=62; i>=0; i--) {
		if(pow2[i] <= a) {
			begun = true;
			a-=pow2[i];
			str+='1';
		}
		else if(begun) {
			str+='0';
		}
	}

	return str;
}

int add(int a, int b) {
	int answer = 0;
	string stra = toBin(a);
	string strb = toBin(b);
	//cout << "a:" << stra << "  b:" << strb << endl;
	string::iterator ita = stra.end();
	string::iterator itb = strb.end();
	ita--;
	itb--;

	for(int e=0; (ita >= stra.begin()) || (itb >= strb.begin()); e++, ita--, itb--) {
		int result = 0;
		if(ita >= stra.begin()) {
			if(*ita == '1') {
				result++;
			}
		}

		if(itb >= strb.begin()) {
			if(*itb == '1') {
				result++;
			}
		}

		//cout << "e:"<<e<<", result:"<<result<<endl;

		answer += pow2[e]*(result%2);
	}

	return answer;
}

void rek(int curr_value, int curr_sum, int other_value, int other_sum, int* current, int* end) {
	dprintf("Value: %d, sum: %d, other_sum: %d, current: %d\n", curr_value, curr_sum, other_sum, *current);

	if(curr_value+(end-current)*(*current) < best_value) {
		dprintf("Kan inte bli best\b");
		return;
	}

	if(current == end) {
		if((curr_sum == other_sum) && (other_value != 0) && (curr_value != 0)) {
			if(curr_value > best_value) {
				best_value = curr_value;
				dprintf("new best\n");
			}// else {
			//	dprintf("Too small.\n");
			//}
		}
		else {
			dprintf("Summorna överrensstämmer ej.\n");
		}
		return;
	}
	dprintf("Chooses %d\n", *current);
	rek(curr_value + *current, add(curr_sum, *current), other_value - *current, add(other_sum, *current), current+1, end);
	dprintf("Unchooses %d\n", *current);
	rek(curr_value, curr_sum, other_value, other_sum, current+1, end);

}

int main() {
	freopen("candy.in", "r", stdin);
	freopen("candy.out", "w", stdout);
	int nr_cases;
	scanf("%d", &nr_cases);

	for(int i = 0; i<nr_cases; i++) {
		best_value = -1;
		int n;
		int other_sum = 0;
		int other_value = 0;
		scanf("%d", &n);

		int candies[n];

		for(int j=0; j<n; j++) {
			scanf("%d", &candies[j]);
			other_sum = add(other_sum, candies[j]);
			other_value += candies[j];
		}

		sort(candies, &candies[n]);
		reverse(candies, &candies[n]);

		rek(0, 0, other_value, other_sum, candies, &candies[n]);

		if(best_value == -1)
			printf("Case #%d: NO\n", i+1);
		else
			printf("Case #%d: %d\n", i+1, best_value);
	}

	return 0;
}
