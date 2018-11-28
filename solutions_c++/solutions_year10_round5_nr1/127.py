#include <iostream>
#include <cmath>
#include <vector>
#include <string>
#include <cstring>
#include <algorithm>
#include <memory.h>
#include <set>
#include <map>
#include <cstdio>
using namespace std;
#define pb push_back
#define all(c) c.begin(), c.end()
typedef long long int64;

struct Point
{
	int x;
	int y;
	Point(int x_, int y_): x(x_), y(y_)
	{ }
};

template<class T> T sqr(const T& t) {return t * t;}
template<class T> T abs(const T& t) {return ((t > 0) ? (t) : (-t));}

void initialize()
{
    freopen("A.in", "r", stdin);
    freopen("_.out", "w", stdout);
}

vector<int> primes;
void createPrimes()
{
	const size_t LEN = (int)1e7;
	vector<bool> mas(LEN, true);
	mas[0] = mas[1] = false;
	for (int i = 2; i < LEN; ++i) {
		if (mas[i]) {
			primes.pb(i);
			for (int j = i + i; j < LEN; j += i) {
				mas[j] = false;
			}
		}
	}
}

int lengthOfNumber(int num){
	int res = 0;
	while (num > 0) {
		res += 1;
		num /= 10;
	}
	return res;
}

const int MAX = 20;
int mas[MAX];

int len, n;

long long deg(long long a, long long d, long long p)
{
	long long b = a;
	long long res = 1;
	while (d > 0) {
		if (d & 1) {
			res = (res * b) % p;
		}
		b = (b * b) % p;
		d >>= 1;
	}
	return res;
}

long long obr(long long num, long long p)
{
	return deg(num, p - 2, p);
}

bool check(long long p, long long* next)
{
	if (n <= 2) {
		return false;
	}
	long long A = (((mas[2] - mas[1] + p) % p) * obr((mas[1] - mas[0] + p) % p, p)) % p;
	long long B = (mas[1] - (A * mas[0]) % p + p) % p;
	for (int i = 0; i + 1 < n; ++i) {
		if ((A * mas[i] + B) % p != mas[i + 1]) return false;
	}
	*next = (A * mas[n - 1] + B) % p;
	return true;
}

set<int> result;
void stupid(long long p)
{
	for (int A = 0; A < p; ++A) {
		int B = ((mas[1] - ((A * mas[0]) % p)) + p) % p;
		bool ok = true;
		for (int i = 0; i + 1 < n; ++i) {
			if ((A * mas[i] + B) % p != mas[i + 1]) ok = false;
		}
		if (ok) {
			result.insert((A * mas[n - 1] + B) % p);
		}
	}
}

int main()
{
    initialize();

	createPrimes();

	int T;
	cin >> T;
	for (int tt = 1; tt <= T; ++tt) {
		cerr << "tt = " << tt << endl;
		int maxNumber = 0;

		cin >> len >> n;
		for (int i = 0; i < n; ++i) {
			cin >> mas[i];
			maxNumber = max(maxNumber, mas[i]);
		}

		long long res;
		//if (n == 1) res = -1;
		//else {
		//result.clear();
		long long next;
		int ok = 0;
		for (int i = 0; i < primes.size(); ++i) {
			if (lengthOfNumber(primes[i]) > len) break;
			if (primes[i] <= maxNumber) continue;
			//if (check(primes[i], &next) != stupid(primes[i], &next)) {
			//	cerr << "P = " << primes[i] << endl;
			//	cerr << "ERR: " << check(primes[i], &next) << " " << stupid(primes[i], &next) << endl;
			//}
//			stupid(primes[i]);
			if (check(primes[i], &next)) {
				if (ok > 0 && res != next) {
					ok += 10;
				}
				else {
					res = next;
					ok = 1;
				}
			}
		}
		//if (result.size() != 1) res = -1;
		//else res = *(result.begin());
		//}

		//if (res == -1) {
		//	printf("Case #%d: I don't know.\n", tt);
		//}
		//else {
		//	printf("Case #%d: %d\n", tt, res);
		//}

		if (ok == 1) {
			printf("Case #%d: %d\n", tt, res);
		}
		else { 
			if (n == 2 && mas[0] == mas[1]) {
				printf("Case #%d: %d\n", tt, mas[0]);
			}
			else {
				printf("Case #%d: I don't know.\n", tt);
			}
		}
	}

    return 0;
}