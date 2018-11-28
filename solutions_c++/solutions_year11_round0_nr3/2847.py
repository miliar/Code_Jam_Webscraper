#include <iostream>
#include <fstream>
#include <cstdlib>

using namespace std;
int solve();
bool combination_generator(int* array, int n, int r);

int main()
{
	ofstream ofs("output_c.txt");
	int turns;
	cin >> turns;
	for (int i = 1; i <= turns; ++i) {
		int result = solve();
		ofs << "Case #" << i << ": ";
		if (result == 0) {
			ofs << "NO" << endl;
		}
		else {
			ofs << result << endl;
		}
	}
	
	system("pause");
	return 0;
}

int solve()
{
	int candy_pieces;
	cin >> candy_pieces;
	int* candy = new int[candy_pieces+1];
	int total = 0;
	for (int i = 1; i <= candy_pieces; ++i) {
		cin >> candy[i];
		total += candy[i];
	}
	
	int max = 0;
	for (int i = 1; i <= candy_pieces / 2; ++i) {
		int* array = new int[i+1];
		for (int j = 1; j <= i; ++j) {
			array[j] = j;
		}
		do {
			int pile_left = 0;
			int pile_right = 0;
			int m = 1;
			for (int k = 1; k <= candy_pieces; ++k) {
				if (m > i) {
					while (k <= candy_pieces) {
						pile_right ^= candy[k];
						++k;
					}
					break;
				}
				if (k == array[m]) {
					pile_left ^= candy[k];
					++m;
				}
				else {
					pile_right ^= candy[k];
				}
			}
			if (pile_left == pile_right) {
				int sum = 0;
				for (int k = 1; k <= i; ++k) {
					sum += candy[array[k]];
				}
				sum = (sum < total / 2) ? total - sum : sum;
				if (sum > max) {
					max = sum;
				}
			} 
		} while (combination_generator(array, candy_pieces, i));
	}
	
	return max;
}

bool combination_generator(int* array, int n, int r)
{
	int i = r;
	while (array[i] == n - r + i) {
		--i;
		if (i == 0) {
			return false;
		}
	}
	
	++array[i];
	for (int j = i + 1; j <= r; ++j) {
		array[j] = array[i] + j - i;
	}
	return true;
}
	
