/**
 * file: dancing_with_the_googlers.cpp
 * Author: Maoliang <kceiwH@gmail.com>
 * Created Time: Fri 13 Apr 2012 11:01:03 PM EDT
 * Description: 
 */

#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
	int num_of_case;
	cin >> num_of_case;
	
	for (int i = 0; i < num_of_case; ++i) {
		unsigned int num_of_googlers;
		cin >> num_of_googlers;
		unsigned int num_of_surprising;
		cin >> num_of_surprising;
		unsigned int at_least_point;
		cin >> at_least_point;
		unsigned int num_surprising_with_point = 0;
		// both surprising and non-surprising
		unsigned int num_with_point = 0; 
		for (int j = 0; j < num_of_googlers; ++j) {
			unsigned int point;
			cin >> point;
			/**
			 * total point: possible points
			 * 3n: {n, n, n}, {n-1, n, n+1}
			 * 3n+1: {n, n, n+1}, {n-1,n+1,n+1}
			 * 3n+2: {n, n+1, n+1}, {n, n, n+2}
			 * For each total point, there must be one surprising 
			 * point and one non-surprising.
			 */
			unsigned int average_point = point / 3;
			unsigned int point_remain = point - 3 * average_point;

			switch (point_remain) {
			case 0:
				if (average_point >= at_least_point) {
					++num_with_point;
				}
				if (average_point > 0 &&
					average_point + 1 >= at_least_point) {
					++num_surprising_with_point;
				}
			break;
			case 1:
				if (average_point + 1 >= at_least_point) {
					++num_with_point;
					if (average_point > 0) {
						++num_surprising_with_point;
					}
				}
			break;
			case 2:
				if (average_point + 1 >= at_least_point) {
					++num_with_point;
				}
				if (average_point + 2 >= at_least_point) {
					++num_surprising_with_point;
				}
			break;
			}
		}

		if (at_least_point == 0) {
			cout << "Case #" << i + 1 << ": "
				<< num_of_googlers << endl;
			continue;
		}

		if (num_surprising_with_point <= num_of_surprising) {
			cout << "Case #" << i + 1 << ": "
				<< num_surprising_with_point << endl;
		} else {
			unsigned difference_in_surprising =
				num_surprising_with_point
				- num_of_surprising;
			if (num_with_point >= difference_in_surprising) {
				cout << "Case #" << i + 1 << ": "
					<< num_surprising_with_point << endl;
			} else {
				cout << "Case #" << i + 1 << ": "
					 << num_with_point
						+ num_of_surprising
					<< endl;
			}

		}
	}

	return 0;
}

