#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

string arr[200];

bool row_sym[200];
bool col_sym[200];

int abs(int a) {
	if (a > 0) return a;
	return 0 - a;
}

int min (int a, int b) {
	if (a < b) return a;
	return b;
}

int max(int a, int b) {
	if (a > b) return a;
	return b;
}


int main () {
	int testCases;
	cin >> testCases;
	for(int testCase = 1; testCase <= testCases; testCase++)
	{
		int k;
		cin >> k;
		for(int i = 1; i <= 2 * k - 1; i++) {
			arr[i] = string(abs(k - i) + 1, ' ');
			for(int j = 1; j <= i && j <= (2 * k - i); j++) {
				char ch;
				cin >> ch;
				arr[i] += string(1, ch) + " ";
			}
			arr[i] = arr[i].substr(0, arr[i].size() - 1);
			arr[i] += string(abs(k-i), ' ');
		}
		
		for(int i = 1; i <= 2 * k - 1; i++) {
			row_sym[i] = true;
			for(int j1 = max(1, 2 * i - 2 * k + 1), j2 = min(2 * i - 1, 2 * k - 1); j1 < j2; j1++, j2--) {
				for(int c = 1; c <= 2 * k - 1; c++) {
					if (arr[j1][c] != ' ' && arr[j2][c] != ' ' && arr[j1][c] != arr[j2][c]) {
						row_sym[i] = false;
						break;
					}
				}
				if(!row_sym[i])
					break;
			}
		}
		for(int i = 1; i <= 2 * k - 1; i++) {
			col_sym[i] = true;
			for(int j1 = max(1, 2 * i - 2 * k + 1), j2 = min(2 * i - 1, 2 * k - 1); j1 < j2; j1++, j2--) {
				for(int c = 1; c <= 2 * k - 1; c++) {
					if (arr[c][j1] != ' ' && arr[c][j2] != ' ' && arr[c][j1] != arr[c][j2]) {
						col_sym[i] = false;
						break;
					}
				}
				if(!col_sym[i])
					break;
			}
		}
		
		int min_cost = 10 * k;
		for (int i = 1; i <= 2 * k - 1; i++) {
			for (int j = 1; j <= 2 * k - 1; j++) {
				if (row_sym[i] && col_sym[j]) {
					min_cost = min(min_cost, k + abs(k - i) + abs(k - j));
				}
			}
		}
		
		cout << "Case #" << testCase << ": " << min_cost * min_cost - k * k		<< endl;
		
		
	}
	
	return 0;
}
