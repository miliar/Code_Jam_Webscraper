/*
ID: Plagapong
LANG: C++
TASK: C
*/

#include<iostream>
#include<fstream>
#include<algorithm>
#define INF 999999999

using namespace std;
ifstream fin;
ofstream fout;

long long n;
long long pliz[100000], ptop = 0;

bool isPrime(long long x) {
  if (x == 2) return true;
  if (~x & 1) return false;
  for (int i = 3; i * i <= x; i += 2)
	if (x % i == 0) return false;
  return true;
}

void preComp() {
  for (long long i = 2; i <= 1200000; i++)
	if (isPrime(i))
	  pliz[ptop++] = i;
  cout << ptop << endl;
}

int howMany(long long x, long long p) {
  int ans = 0;
  while (x >= p * p) {
	ans++;
	x /= p;
  }
  return ans;
}

int cnt[100000];

void clearVars() {
  // Clear variables
  fill(cnt, cnt + 1000, 0);
}

void process() {
  // Code here!
  fin >> n;
  if (n == 1) {
	fout << 0;
	return;
  }
  int i;
  for (i = 0; i < ptop; i++) {
	cnt[i] = howMany(n, pliz[i]);
	//cout << cnt[i] << endl;
	if (!cnt[i]) break;
  }
  // max prime is i-1
  int ans = 0;
  for (int j = 0; j < i; j++)
	ans += cnt[j];
  ans += 1;
  fout << ans;
}

int main(int argc, const char* argv[]) {
  if (argc != 3) {
	cout << "Please indicate input and output" << endl;
	exit(0);
  }
  fin.open(argv[1]);
  fout.open(argv[2]);
  preComp();
  int times;
  fin >> times;
  for (int i = 1; i <= times; i++) {
	fout << "Case #" << i << ": ";
	clearVars();
	process();
	fout << endl;
  }
  fin.close();
  fout.close();
  return 0;
}
