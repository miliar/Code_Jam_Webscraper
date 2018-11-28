#include <iostream>
#define _USE_MATH_DEFINES
#include <cmath>
#include <vector>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <sstream>
#include <cstdio>
#include <cstdlib>

using namespace std;

//vector<int> t, rank;
int t[1001], rank[1001];

int find(int x) {
	if (t[x] != x)
		t[x] = find(t[x]);
	return t[x];
}

void union_(int x, int y) {
	x = find(x);
	y = find(y);
	if (x == y)
		return;
	if (rank[x] > rank[y])
		t[y] = x;
	else {
		t[x] = y;
		++rank[y];
	}
}

bool isprime(int x) {
	if (x < 2)
		return false;
	if (x == 2)
		return true;
	if (x % 2 == 0)
		return false;
	for (int i = 3; i * i <= x; i += 2) {
		if (x % i == 0)
			return false;
	}
	return true;
}

vector<int> primes;

int prf(int a, int b) {
	int i;
	for (i = primes.size() - 1; i >= 0; --i) {
		if (a % primes[i] == 0 && b % primes[i] == 0)
			return primes[i];
	}
	return -1;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int N;
	cin >> N;
	
	for (int i = 0; i < 2000; ++i) {
		if (isprime(i))
			primes.push_back(i);
	}
	for (int i = 0; i < N; ++i) {
		long long A, B, P;
		cin >> A >> B >> P;
		for (int j = A, k = 0; j <= B; ++j, ++k) {
			t[j] = k;
			//t[j] = k;
		}
		memset(rank, 0, sizeof(rank));
		for (int j = A; j <= B; ++j) {
			for (int k = A; k <= B; ++k) {
				if (t[j] != t[k] && prf(j, k) >= P) {
					//union_(j, k);
					int m = t[k], mm = t[j];
					for (int w = A; w <= B; ++w) {
						if (t[w] == m)
							t[w] = mm;
					}
				}
			}
		}
		/*int n = (int)(B - A + 1);
		vector<long long> d(n);
		t = vector<int>(n);
		rank = vector<int>(n);
		for (int j = 0; j < n; ++j)
			t[j] = j;
		for (long long x = A; x <= B; x++) {
			int j = (int) (x - A);
			d[j] = x;
		}
		long long st = 2;
		for (long long x = A; x <= B; x++) {
			int i = (int) (x - A);
			long long p = st;
			while (d[i] > 1) {
				if (d[i] % p == 0) {
                    st = p;
                    for (long long y = x; y <= B; y += p) {
                         if (p >= P)
							union_(i, (int)(y - A));
                         while (d[(int)(y-A)] % p == 0)
							 d[(int)(y-A)] /= p;
                    }
               }
               if (p * p > d[i])
				   p = d[i];
			   else
				   ++p;
          }
          
		}*/
		set<int> s;
		for (int j = A; j <= B; ++j) {
			s.insert(t[j]);
		}
		cout << "Case #" << i + 1 << ": " << s.size() << endl;
	}

	return 0;
}
