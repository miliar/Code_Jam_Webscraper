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
int tests;
cin >> tests;
for (int eee=1;eee<=tests;++eee){
 
 long long n, m, X, Y, Z;
 long long d[2000], a[2000], g[2000];
  cin >> n >> m >> X >> Y >> Z;
  for (int j = 0; j < m; ++j) {
   cin >> g[j];
  }
  for (int j = 0; j < n; ++j) {
   a[j] = g[j % m];
   g[j % m] = (X * g[j % m] + Y * (j + 1)) % Z;
  }
  d[0]=1;
  for (int i=1;i<n;++i){
	d[i]=1;
	for (int j=0;j<i;++j)if (a[j]<a[i]){
		d[i]+=d[j]%1000000007LL;
		d[i]%=1000000007LL;
	}
  }
  long long res=0;
  for(int i=0;i<n;++i){
	res+=d[i]%1000000007LL;
	res%=1000000007LL;
  }

  cout << "Case #" << eee << ": " << res << endl;

}
 return 0;
}