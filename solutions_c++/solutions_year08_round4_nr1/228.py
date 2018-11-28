#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

#define mset(c, val) memset((c), (val), sizeof((c)))
#define all(v) v.begin(), v.end()
#define INF 1000000000
#define EPS 1e-10

typedef vector<int> vi;
typedef long long lint;

	ifstream fin("input.txt");
	ofstream fout("output.txt");

	int test, tnum;

	int memo[16384][2];
	int answer;
	int n, nl, v;

	int val[16384];
	int maychange[16384];

	void readdata()
	{
		mset(val, 0);
		mset(maychange, 0);
		fin >> n >> v;
		nl = (n - 1) / 2;
		for (int i = 0; i < nl; i++) {
			fin >> val[i] >> maychange[i];
		}
		for (int i = 0; i < (n - nl); i++) {
			fin >> val[i + nl];
		}
	}

	void outputdata()
	{
		if (answer < 0)
            fout << "Case #" << (test + 1) << ": IMPOSSIBLE" << endl;
		else
            fout << "Case #" << (test + 1) << ": " << answer << endl;
	}

	void init()
	{
		mset(memo, -1);
	}

	int comb(int s1, int s2) {
		if (s1 < 0 || s2 < 0)
			return -100;
		return s1 + s2;
	}
	
	int promo(int res, int cur) {
		if (cur >= 0) {
			if (res < 0)
				return cur;
			if (res >= 0 && cur < res)
				return cur;
		}
		return res;
	}

	int f(int pos, int value) {
		int &res = memo[pos][value];
		if (res == -1) {
			if (pos >= nl) {
				if (val[pos] == value)
					return 0;
				else
					return -100;
			} else {
				int addand = 0, addor = 0;
				bool isand = false, isor = false;
				if (val[pos] == 1) {
					isand = true;
					if (maychange[pos]) {
						isor = true;
						addor = 1;
					}
				}
				if (val[pos] == 0) {
					isor = true;
					if (maychange[pos]) {
						isand = true;
						addand = 1;
					}
				}

				///
				int s1, s2, s;
				if (isand) {
					if (value == 1) {
						s1 = f(2 * pos + 1, 1); s2 = f(2 * pos + 2, 1);
						s = comb(s1, s2);
						res = promo(res, s + addand);
					} else {
						s1 = f(2 * pos + 1, 0); s2 = f(2 * pos + 2, 1);
						s = comb(s1, s2);
						res = promo(res, s + addand);
						s1 = f(2 * pos + 1, 1); s2 = f(2 * pos + 2, 0);
						s = comb(s1, s2);
						res = promo(res, s + addand);
						s1 = f(2 * pos + 1, 0); s2 = f(2 * pos + 2, 0);
						s = comb(s1, s2);
						res = promo(res, s + addand);
					}
				}
				if (isor) {
					if (value == 0) {
						s1 = f(2 * pos + 1, 0); s2 = f(2 * pos + 2, 0);
						s = comb(s1, s2);
						res = promo(res, s + addor);
					} else {
						s1 = f(2 * pos + 1, 0); s2 = f(2 * pos + 2, 1);
						s = comb(s1, s2);
						res = promo(res, s + addor);
						s1 = f(2 * pos + 1, 1); s2 = f(2 * pos + 2, 0);
						s = comb(s1, s2);
						res = promo(res, s + addor);
						s1 = f(2 * pos + 1, 1); s2 = f(2 * pos + 2, 1);
						s = comb(s1, s2);
						res = promo(res, s + addor);
					}
				}

				if (res == -1)
					res = -100;

			}
		}
		return res;
	}

	void run()
	{
		answer = f(0, v);
	}

int main()
{
	fin >> tnum;
	for (test = 0; test < tnum; test++) {
		readdata();
		init();
		run();
		outputdata();
	}
	return 0;
}
