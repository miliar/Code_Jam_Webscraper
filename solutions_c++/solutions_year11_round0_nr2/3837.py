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
	char combine[26][26];
	char  opposed[26];
	int  present[26];
	char current_list[101];
	char new_list[101];
	int C, D, N, new_N;
	string input_string;
	for (int i = 0; i < 26; i++) {
		present[i] = 0;
		opposed[i] = 0;
		for (int j = 0; j < 26; j++) {
			combine[i][j] = 0;
		}
	}
	cin >> C;
	for (int i = 0; i < C; i++) {
		cin >> input_string;
		combine[input_string[0] - 'A'][input_string[1] - 'A'] = combine[input_string[1] - 'A'][input_string[0] - 'A'] = input_string[2];
	}
	cin >> D;
	for (int i = 0; i < D; i++) {
		cin >> input_string;
		opposed[input_string[0] - 'A'] = input_string[1];
		opposed[input_string[1] - 'A'] = input_string[0];	
	}
	cin >> N;
	cin >> current_list;
	new_N = 0;
	for (int i = 0; i < N; i++) {
		if (new_N == 0) {
			new_list[0] = current_list[i];
			char opposite = opposed[current_list[i] - 'A'];
			if (opposite != 0) {
				present[opposite - 'A'] += 1;
			}
			new_N++;
		} else if (combine[new_list[new_N - 1] - 'A'][current_list[i] - 'A'] != 0) {
			char opposite = opposed[new_list[new_N - 1] - 'A'];
			if (opposite != 0) {
				present[opposite - 'A']--;
			}
			new_list[new_N - 1] = combine[new_list[new_N - 1] - 'A'][current_list[i] - 'A'];
		} else if (present[current_list[i] - 'A']) {
			for (int i = 0; i < 26; i++) {
				present[i] = 0;
			}
			new_N = 0;
		} else {
			new_list[new_N++] = current_list[i];
			char opposite = opposed[current_list[i] - 'A'];
			if (opposite != 0) {
				present[opposite - 'A'] += 1;
			}
		}
	}
	cout << "Case #" << T + 1 << ": [";
	for (int i = 0; i < new_N; i++) {
		cout << new_list[i] << ((i == (new_N - 1))?"":", ");
	}
	cout << "]" << endl;
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
