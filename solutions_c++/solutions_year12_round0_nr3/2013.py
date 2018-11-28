#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

#define SIZE 10000000

bool marked[SIZE];

int check (int small, int large, int number) {
	if (number < 10)
		return 0;

	char buf1[20], buf2[20];
	itoa(number, buf1, 10);
	int len = strlen(buf1);
	strncpy(buf2, buf1, len);
	strncpy(buf2 + len, buf1, len);

	char* e = buf2 + len * 2 - 1;
	*e = '\0';

	int result = 1;
	marked[number] = true;
	for (int i = len - 1; i >= 0; --i) {
		int x = atoi(buf2 + i);
		if (x >= small && x <= large && marked[x] == false) {
//			cout << "		" << number << "," << buf2 + i << "," << buf2 << endl;
			marked[x] = true;
			++result;
		}
		*(--e) = '\0';
	}

//	cout << "	" << number << " = " << result << endl;
	return result * (result - 1 >= 0 ? result - 1: 0) / 2;
}

void Problem_3 () {
	//clock_t t1 = clock();
	//cout << t1 << endl;
	int cases;
	cin >> cases;
	for (int k = 1; k <= cases; ++k) {
		//clock_t t2 = clock();
		int small, large;
		cin >> small >> large;

//		cout << "***" << small << ", " << large << endl;
		for (int i = small; i <= large; ++i)
			marked[i] = false;

		int result = 0;
		for (int i = small; i <= large; ++i) {
			if (marked[i]) continue;
			result += check(small, large, i);
		}
		
		cout << "Case #" << k << ": " << result << endl;
		//cout << (clock() - t2) / CLOCKS_PER_SEC << endl;
	}
	//cout << clock() - t1 << endl;
}

int main () {
	Problem_3();
	return 0;
}