#include <stdio.h>
#include <stdlib.h>
#include <gmpxx.h>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

mpz_class gcd(const mpz_class &a, const mpz_class &b) {
 if (b == 0) return a;
 return gcd(b, a%b);
}

int caseno;

void doit() {
 vector<mpz_class> z;
 int n;
 scanf("%i", &n);
 char buf[4096];
 while(n--) {
  scanf("%s", buf);
  z.push_back(mpz_class(buf));
 }
 sort(z.begin(), z.end());
 mpz_class g = 0;
 for (int i = 1; i < z.size(); i++)
  g = gcd(g, z[i]-z[0]);
 mpz_class ans = z[0] % g;
 ans = g - ans;
 printf("Case #%i: ", ++caseno); fflush(stdout);
 cout << ans << endl;
 cout.flush();
}

int main() {
 int n;
 scanf("%i", &n);
 while(n--) doit();
}
