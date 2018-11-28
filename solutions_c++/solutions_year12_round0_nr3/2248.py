#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <stack>
#include <map>
using namespace std;

#define REP(i,n) for(int i=0; i < (n); i++)
#define REP2(i,s,n) for(int i=(s); i < (n); i++)

int main()
{
	int TESTCASES; cin >> TESTCASES;
	for (int CASE = 1; CASE <= TESTCASES; CASE++)
	{
		int A, B; cin >> A >> B;
		long long r = 0;

		vector<int> m;

		REP2(n, A, B)
		{
			m.clear();
			m.push_back(n);
			int x;
			if (n < 10) {
			} else if (n < 100) {
				x = n/10 + n % 10 * 10; if (x >= A && x <= B && x > n && find(m.begin(), m.end(), x) == m.end()) { r++; m.push_back(x); }
			} else if (n < 1000) {
				x = n/10 + n % 10 * 100; if (x >= A && x <= B && x > n && find(m.begin(), m.end(), x) == m.end()) { r++; m.push_back(x); }
				x = n/100 + n % 100 * 10; if (x >= A && x <= B && x > n && find(m.begin(), m.end(), x) == m.end()) { r++; m.push_back(x); }
			} else if (n < 10000) {
				x = n/10 + n % 10 * 1000; if (x >= A && x <= B && x > n && find(m.begin(), m.end(), x) == m.end()) { r++; m.push_back(x); }
				x = n/100 + n % 100 * 100; if (x >= A && x <= B && x > n && find(m.begin(), m.end(), x) == m.end()) { r++; m.push_back(x);}
				x = n/1000 + n % 1000 * 10; if (x >= A && x <= B && x > n && find(m.begin(), m.end(), x) == m.end()) { r++; m.push_back(x); }
			} else if (n < 100000) {
				x = n/10 + n % 10 * 10000; if (x >= A && x <= B && x > n && find(m.begin(), m.end(), x) == m.end()) { r++; m.push_back(x);}
				x = n/100 + n % 100 * 1000; if (x >= A && x <= B && x > n && find(m.begin(), m.end(), x) == m.end()) { r++; m.push_back(x); }
				x = n/1000 + n % 1000 * 100; if (x >= A && x <= B && x > n && find(m.begin(), m.end(), x) == m.end()) { r++; m.push_back(x);}
				x = n/10000 + n % 10000 * 10; if (x >= A && x <= B && x > n && find(m.begin(), m.end(), x) == m.end()) { r++; m.push_back(x); }
			} else if (n < 1000000) {
				x = n/10 + n % 10 * 100000; if (x >= A && x <= B && x > n && find(m.begin(), m.end(), x) == m.end()) { r++; m.push_back(x);}
				x = n/100 + n % 100 * 10000; if (x >= A && x <= B && x > n && find(m.begin(), m.end(), x) == m.end()) { r++; m.push_back(x); }
				x = n/1000 + n % 1000 * 1000; if (x >= A && x <= B && x > n && find(m.begin(), m.end(), x) == m.end()) { r++; m.push_back(x); }
				x = n/10000 + n % 10000 * 100; if (x >= A && x <= B && x > n && find(m.begin(), m.end(), x) == m.end()) { r++; m.push_back(x);}
				x = n/100000 + n % 100000 * 10; if (x >= A && x <= B && x > n && find(m.begin(), m.end(), x) == m.end()) { r++; m.push_back(x); }
			} else if (n < 10000000) {
				x = n/10 + n % 10 * 1000000; if (x >= A && x <= B && x > n && find(m.begin(), m.end(), x) == m.end()) { r++; m.push_back(x); }
				x = n/100 + n % 100 * 100000; if (x >= A && x <= B && x > n && find(m.begin(), m.end(), x) == m.end()) { r++; m.push_back(x); }
				x = n/1000 + n % 1000 * 10000; if (x >= A && x <= B && x > n && find(m.begin(), m.end(), x) == m.end()) { r++; m.push_back(x); }
				x = n/10000 + n % 10000 * 1000; if (x >= A && x <= B && x > n && find(m.begin(), m.end(), x) == m.end()) { r++; m.push_back(x); }
				x = n/100000 + n % 100000 * 100; if (x >= A && x <= B && x > n && find(m.begin(), m.end(), x) == m.end()) { r++; m.push_back(x); }
				x = n/1000000 + n % 1000000 * 10; if (x >= A && x <= B && x > n && find(m.begin(), m.end(), x) == m.end()) { r++; m.push_back(x); }
			}
		}

		cout << "Case #" << CASE << ": " << r << endl;
	}

	return 0;
}