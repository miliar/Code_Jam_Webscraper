#include <vector>
#include <algorithm>
#include <iostream>
#include <stdint.h>
#include <string>
#include <cmath>
#include <cstring>
#include <cassert>

using namespace std;

bool oppose[26][26];
char combine[26][26];

inline uint32_t Trans(char c) {
	return c - 'A';
}

void Solve(int32_t t) {
	memset(oppose, 0, sizeof(oppose));
	memset(combine, 0, sizeof(combine));
	
	uint32_t c, d;
	string s, s2, s3;
	
	cin >> c;
	for (uint32_t i = 0; i < c; i++) {
		cin >> s;
		combine[Trans(s[0])][Trans(s[1])] = s[2];
		combine[Trans(s[1])][Trans(s[0])] = s[2];
	}
	
	cin >> d;
	for (uint32_t i = 0; i < d; i++) {
		cin >> s;
		oppose[Trans(s[0])][Trans(s[1])] = true;
		oppose[Trans(s[1])][Trans(s[0])] = true;
	}
	
	cin >> c;
	cin >> s;
	s2 = s;

	int32_t i = 0;
	do {
		s3 += s[i];
		int32_t a = Trans(s[i]);
		if (i > 0 && combine[a][Trans(s[i - 1])] != 0) {
			s.replace(i - 1, 2, 1, combine[a][Trans(s[i - 1])]);
			i -= 1;
		}
		else {
			for (int32_t j = i - 1; j >= 0; j--) {
				if (oppose[a][Trans(s[j])]) {
					s.erase(0, i + 1);
					i = -1;
					break;
				}
			}
		}
		i++;
	} while (i < s.length());
	assert(s2 == s3);
	s2 = s;
	
	cout << "Case #" << t << ": [";
	for (uint32_t i = 0; i < s2.length(); i++) {
		cout << s2[i] << (i < s2.length() - 1 ? ", " : "");
	}
	cout << "]" << endl;
}

int main() {
	int32_t t;
	cin >> t;

	for (int32_t i = 1; i <= t; i++) {
		Solve(i);
	}
	
	return 0;
}

