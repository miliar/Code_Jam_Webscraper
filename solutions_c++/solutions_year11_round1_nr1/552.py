#include <iostream>
#include <cstdlib>
#include <cstring>

using namespace std;

typedef long long int64;

int64 N, Pd, Pg;

int64 gcd(int64 a, int64 b) {
      if (b == 0) {
         return a;
      }
      return gcd(b, a % b);
}

bool solve() {
     /*
     int64 cm = gcd(Pg, 100);
     int64 x = N / (100 / cm) * (100 / cm);
     int64 a = x * Pg / 100;
     cm = gcd(Pd, 100);
     int64 y = 100 / cm;
     int64 b = y * Pd / 100;
     return x >= y && a >= b;
     */
     int64 cm = gcd(Pd, 100);
     int64 y = 100 / cm;
     if (y > N) {
        return false;      
     }
     if (Pg == 0) {
        return Pd == 0;       
     }
     if (Pg == 100) {
        return Pd == 100;       
     }
     
     if (Pd == 0) {
        if (Pg == 100) {
           return false;
        }
     }
     return true;
}

int main() {
    int T;
    freopen("C://outS1.txt", "w", stdout);
    scanf("%d", &T);
    int cse = 0;
    while (T--) {
        cse++;
        cin >> N >> Pd >> Pg;
        bool ret = solve();
        printf("Case #%d: %s\n", cse, ret ? "Possible" : "Broken");
    }
    //system("pause");
    return 0;
}

