/**
 * file: recycled_numbers.cpp
 * Author: Maoliang <kceiwH@gmail.com>
 * Created Time: Sat 14 Apr 2012 03:55:28 PM EDT
 * Description: 
 */

#include <iostream>
#include <cmath>
#include <set>

using namespace std;

int main(int argc, char *argv[])
{
	unsigned num_case;
	cin >> num_case;
	set< unsigned > recycled_nums;
	
	for (unsigned i = 0; i < num_case; ++i) {
		unsigned first;
		unsigned last;
		cin >> first >> last;

		unsigned num_recycled = 0;
		for (unsigned j = first; j <= last; ++j) {
			unsigned num_digits = 0;
			unsigned tmp = 1;
			do {
				tmp *= 10;
				++num_digits;
			} while (j / tmp > 0);

			tmp /= 10;

			recycled_nums.clear();
			for (unsigned k = 10; true;
				k *= 10, tmp /= 10) {
				unsigned quotient = j / k;
				if (quotient == 0) {
					break;
				}

				unsigned remainder = j - k * quotient;
				unsigned new_num = remainder *
					tmp + quotient;
				if (new_num == j) {
					continue;
				}
				if (new_num <= last && new_num >= first) {
					recycled_nums.insert(new_num);
				}
			}

			num_recycled += recycled_nums.size();
		}

		cout << "Case #" << i + 1 << ": "
			<< num_recycled / 2 << endl;
	}

	return 0;
}

