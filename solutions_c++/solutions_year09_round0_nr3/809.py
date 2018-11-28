#include <iostream>
#include <iomanip>
using namespace std;

#define LARGE

#ifndef LARGE

const int TEXT_SIZE = 30;

#else

const int TEXT_SIZE = 500;

#endif

char text[TEXT_SIZE+1];
int result;
char pattern[] = "welcome to code jam";
int pattern_size = 19;
int pref[TEXT_SIZE][20];

void compute() {
	int text_size = strlen(text);

	for (int text_i = 0; text_i < text_size; text_i++) {
		pref[text_i][0] = 1;
	}

	for (int pref_i = 1; pref_i < 19; pref_i++) {
		pref[0][pref_i] = 0;
	}

	for (int pref_i = 1; pref_i <= 19; pref_i++) {
		for (int text_i = 1; text_i < text_size; text_i++) {
			pref[text_i][pref_i] = pref[text_i-1][pref_i];
			if (text[text_i-1] == pattern[pref_i-1]) {
				pref[text_i][pref_i] += pref[text_i-1][pref_i-1];
			}
			pref[text_i][pref_i] = pref[text_i][pref_i] % 10000;
		}
	}

	result = pref[text_size-1][19];
	if (text[text_size-1] == pattern[18]) {
		result += pref[text_size-1][18];
	}
}

int main() {
	cin.tie(NULL);
	int n;
	cin >> n;
	cin.getline(text,TEXT_SIZE+1);
	for (int i = 0; i < n; i++) {
		cin.getline(text,TEXT_SIZE+1);
		compute();
		result = result % 10000;
		cout << "Case #" << i + 1 << ": " << setfill('0')
		<< setw(4) << result << "\n";
	}
	cout.flush();
	return 0;
}
