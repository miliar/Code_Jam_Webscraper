#include <algorithm>
#include <cmath>
#include <fstream>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

typedef __int64 ll;

ifstream in("in.txt");
ofstream out("out.txt");
void Init();
void SolveCase();

int main() {
  int N;
  in >> N;
  Init();
  for (int tc = 1; tc <= N; tc++) {
    cout << "Case #" << tc << endl;
    out << "Case #" << tc << ": ";
    SolveCase();
  }
  return 0;
}

const int kp = 10007;
vector<int> inverse(kp), fact(kp);

int Fact(int n) {
  int a = n % kp;
  int b = n / kp;
  int m = fact[a];
  if (b%2 == 1)
    m = kp-m;
  return m;
}

int NCK1(int n, int k) {
  int n1 = n/kp;
  int k1 = k/kp;
  int k2 = (n-k)/kp;
  if (n1 > k1+k2) return 0;
  
  int base;
  if (k1 == 0 || k2 == 0)
    base = 1;
  else
    base = NCK1(n1, k1);

  base = (base*Fact(n)) % kp;
  base = (base*inverse[Fact(k)]) % kp;
  base = (base*inverse[Fact(n-k)]) % kp;
  return base;
}

vector<vector<int> > memo(1000, vector<int>(1000, -1));
int NCK2(int n, int k) {
  if (memo[n][k] != -1)
    return memo[n][k];
  if (k == 0 || k == n)
    return 1;
  int x = NCK2(n-1, k-1) + NCK2(n-1, k);
  x %= kp;
  memo[n][k] = x;
  return memo[n][k];
}

int NCK(int n, int k) {
  int a1 = NCK1(n, k);
  //int a2 = NCK2(n, k);
  //if (a1 != a2) cout << "ERROR";
  return a1;
}

int routes(int x1, int y1, int x2, int y2) {
  if (x1 == x2 && y1 == y2)
    return 1;
  if (x2 < x1 || y2 < y1)
    return 0;
  int sum = y2-y1 + x2-x1;
  if (sum%3 != 0)
    return 0;
  int v1 = x2-x1 - sum/3;
  int v2 = y2-y1 - sum/3;
  //cout << v1 << " " << v2 << endl;
  if (v1 >= 0 && v2 >= 0)
    return NCK(v1+v2, v1);
  else
    return 0;
}

int Routes(int x1, int y1, int x2, int y2) {
  //cout << x1 << " " << y1 << " " << x2 << " " << y2 << endl;
  int x = routes(x1, y1, x2, y2);
  //cout << x << endl;
  return x;
}

int Pow(int n, int a) {
  if (a == 0)
    return 1;
  int z = Pow(n, a/2);
  z = (z*z) % kp;
  if (a % 2 == 1)
    z = (z*n) % kp;
  return z;
}

void Init() {
  for (int i = 1; i < kp; i++) {
    inverse[i] = Pow(i, kp-2);
    if (((i*inverse[i]) % kp) != 1)
      cout << "ERROR" << endl;
  }
  fact[0] = 1;
  for (int i = 1; i < kp; i++)
    fact[i] = (fact[i-1] * i) % kp;
}

void SolveCase() {
  int h, w, r;
  in >> h >> w >> r;
  vector<int> rx(r), ry(r);
  for (int i = 0; i < r; i++) {
    in >> ry[i] >> rx[i];
    rx[i]--;
    ry[i]--;
  }
  for (int i = 0; i < r; i++)
  for (int j = i+1; j < r; j++)
  if (rx[i] + ry[i] > rx[j] + ry[j]) {
    int temp;
    temp = rx[i]; rx[i] = rx[j]; rx[j] = temp;
    temp = ry[i]; ry[i] = ry[j]; ry[j] = temp;
  }

  int total = 0;
  for (int bm = 0; bm < (1<<r); bm++) {
    int par = 1;
    int temp = 1;
    int px = 0, py = 0;
    for (int i = 0; i < r; i++)
    if ( (bm & (1<<i)) > 0) {
      par *= -1;
      temp *= Routes(px, py, rx[i], ry[i]);
      temp %= kp;
      px = rx[i];
      py = ry[i];
      if (px+py > rx[i]+ry[i])
        cout << "ERROR" << endl;
    }
    temp *= Routes(px, py, w-1, h-1);
    //cout << "*** " << bm << " " << temp << endl;
    temp %= kp;
    total += temp*par;
    total %= kp;
    total += kp;
    total %= kp;
  }
  out << total << endl;
}
