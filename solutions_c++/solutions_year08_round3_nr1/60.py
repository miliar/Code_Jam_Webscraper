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

/*vector<int> t, rank;
//int t[1001], rank[1001];

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
}*/

bool isu(long long x) {
	return x % 2 == 0 || x % 3 == 0 || x % 5 == 0 || x % 7 == 0;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int N;
	cin >> N;
	
	for (int i = 0; i < N; ++i) {
          int p;
          int k;
          int n;
		  cin >> p >> k >> n;
		  vector<int> a(n);
          
          for (int i=0; i<n; i++) cin >> a[i];
          if (n>k*p) {
               cout << "Impossible";
               continue;
          }
          sort(a.begin(), a.end());
          
		  vector<int> r(k);
		  for (int iii = 0; iii < k; ++iii)
			  r[iii] = p;
               
          long res = 0;
          int h = 1;
          int kk = 1;
          for (int i=n-1; i>=0; --i) {
               res += a[i]*h;
               kk++;
               if (kk>k) {
                    kk = 1;
                    h++;
               }
          }     
		cout << "Case #" << i + 1 << ": " << res << endl;
	}

	return 0;
}
