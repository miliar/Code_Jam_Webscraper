#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <functional>
#include <iostream>
#include <set>
#include <string>
#include <vector>
using namespace std;

int main()
{
	long long int inps, moves, i, o, b, num, res, k, buf, j;
	vector < pair <char, long long int> > vec;
	char c;

	cin >> inps;

	for (j = 1; j <= inps; j++) {
		cin >> moves;

		vec.clear();

		o = 1;
		b = 1;

		for (i = 0; i < moves; i++) {
			cin >> c;
			cin >> num;

			if (c == 'O'){
				vec.push_back(make_pair(c, abs(num - o) + 1));
				o = num;
			}
			else {
				vec.push_back(make_pair(c, abs(num - b) + 1));
				b = num;
			}
		}

		res = 0;
		o = 0;
		b = 0;

		for (i = 0; i < vec.size(); i++) {
			if (vec[i].first == 'B') {
				if (vec[i].second <= o) {
					res += 1;
					b += 1;
				}
				else {
					res += vec[i].second - o;
					b += vec[i].second - o;
				}
				o = 0;
			}
			else {
				if (vec[i].second <= b) {
				res += 1;
				o += 1;
				}
				else {
					res += vec[i].second - b;
					o += vec[i].second - b;
				}
				b = 0;
			}
		}
		cout << "Case #";
		cout << j;
		cout << ": ";
		cout << res << endl;

	}

	return 0;
}
