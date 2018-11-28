/*
 * http://code.google.com/codejam/contest/1460488/dashboard#s=p2
 * Problem C. Recycled Numbers
 */

#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <set>
#include <algorithm>
#include <functional>
#include <assert.h>

using namespace std;

#define MAX_B 2000000

int from_digit(const vector<int>& digit)
{
	int n = 0;
	for (int i=0; i<digit.size(); i++) {
		if (i > 0) {
			int a = digit[i];
			for (int j=0; j<i; j++) {
				a *= 10;
			}
			n += a;
		} else
			n += digit[i];
	}
	return n;
}

void to_digit(int n, vector<int>& digit)
{
	while (n > 0) {
		int mod = n % 10;
		digit.push_back(mod);
		n /= 10;
	}
}

int solve()
{
	int A, B;
	cin >> A >> B;

	set<pair<int, int> > memo;
	for (int n=A; n<=B; n++) {
		vector<int> digit;
		to_digit(n, digit);
		for (int i=0; i<digit.size(); i++) {
			vector<int> m_digit(digit.size());
			for (int j=0; j<digit.size(); j++) {
				m_digit[j%digit.size()] = digit[(i+j+1)%digit.size()];
			}
			if (m_digit[digit.size()-1] != 0) { //skip leading zero.
				int m = from_digit(m_digit);
				if (n < m && m <= B) {
					memo.insert(make_pair(n, m));
					//cerr << n << ", " << m << endl;
				}
			}
		}
	}

	return memo.size();
}

int main()
{
	int T;
	cin >> T;
	for (int i=1; i<=T; i++) {
		cout << "Case #" << i << ": " << solve() << endl;
	}
	return 0;
}
