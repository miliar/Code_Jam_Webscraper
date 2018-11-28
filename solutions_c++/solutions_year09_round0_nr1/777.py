#include <iostream>
using namespace std;

#define LARGE

#ifndef LARGE

const int MAX_L = 10;
const int MAX_D = 25;

#else

const int MAX_L = 15;
const int MAX_D = 5000;

#endif

char dictionary[MAX_D][MAX_L+1];
int L, D;
char word[1000];
int n_matches;
int match[MAX_D];
int n_letters = 0;
char letters[40];

void init() {
	for (int i = 0; i < D; i++) {
		match[i] = 1;
	}
}

void get_letters(int& i) {
	if (word[i] == '(') {
		n_letters = 0;
		i++;
		while (word[i] != ')') {
			letters[n_letters++] = word[i];
			i++;
		}
	} else {
		n_letters = 1;
		letters[0] = word[i];
	}
	i++;
}

void compute() {
	int word_i = 0;
	for (int i = 0; i < L; i++) {
		get_letters(word_i);
		//cout << "n_letters: " << n_letters << ", "
		//<< letters[0] << ", " << letters[1] << "\n";
		for (int j = 0; j < D; j++) {
			if (match[j]) {
				match[j] = 0;
				for (int k = 0; k < n_letters; k++) {
					//cout << "dictionary: " << dictionary[j][i]
					//<< ", letters: " << letters[k] << "\n";
					if (dictionary[j][i] == letters[k]) {
						match[j] = 1;
						break;
					}
				}
				//cout << "match: " << match[j] << "\n";
			}
		}
	}
	n_matches = 0;
	for (int i = 0; i < D; i++) {
		if (match[i]) {
			n_matches++;
		}
	}
}

int main() {
	int n;
	cin >> L >> D >> n;
	for (int i = 0; i < D; i++) {
		cin >> dictionary[i];
	}
	for (int i = 0; i < n; i++) {
		cin >> word;
		init();
		compute();
		cout << "Case #" << i + 1 << ": " << n_matches << "\n";
	}
	cout.flush();
	return 0;
}
