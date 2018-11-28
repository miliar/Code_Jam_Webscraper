#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <climits>
#include <ctime>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
#include <deque>
#include <list>
#include <queue>
#include <set>
#include <map>
#include <limits>

using namespace std;

vector<int> primes;

void eratosthenes(int n) {
  vector<bool> isprime(n + 1, true);
  for (int i = 2; i <= n; i++) {
    if (!isprime[i]) continue;
    primes.push_back(i);
    for (int j = i * i; j <= n; j += i) isprime[j] = false;
  }
}

struct Factor {
  Factor() {}
  Factor(int x, int p) : x(x), p(p) {}
  int x;
  int p;
};

typedef vector<Factor> FactNum;

void factorization(int x, FactNum& xf) {
  xf.clear();
  for (int i = 2; i <= x; i++) {
    if (x % i == 0) {
      xf.push_back(Factor(i, 0));
      do {
        xf.back().p++;
        x /= i;
      } while (x % i == 0);
    }
  }
}

void ppcm(const FactNum& f1, const FactNum& f2, FactNum& f) {
  int i = 0, j = 0, n1 = f1.size(), n2 = f2.size();
  f.clear();
  while (i < n1 || j < n2) {
    if (i < n1 && (j == n2 || f1[i].x < f2[j].x)) {
      f.push_back(f1[i]);
      i++;
    }
    else if (j < n2 && (i == n1 || f2[j].x < f1[i].x)) {
      f.push_back(f2[j]);
      j++;
    }
    else {
      assert(f1[i].x == f2[j].x);
      f.push_back(Factor(f1[i].x, max(f1[i].p, f2[j].p)));
      i++; j++;
    }
  }
}

bool isEqual(const FactNum& f1, const FactNum& f2) {
  if (f1.size() != f2.size()) return false;
  for (size_t i = 0; i < f1.size(); i++) {
    if (f1[i].x != f2[i].x || f1[i].p != f2[i].p) return false;
  }
  return true;
}

ostream& operator<<(ostream& os, const Factor& f) {
  return os << f.x << "^" << f.p;
}

ostream& operator<<(ostream& os, const FactNum& f) {
  if (f.empty())
    os << "1";
  else {
    os << f[0];
    for (int i = 1; i < (int) f.size(); i++) {
      os << "*" << f[i];
    }
  }
  return os;
}


FactNum tmp;
vector<int> tmp2;

double getValue(int i, FactNum& f) {
  for (int j = 0; j < (int) f.size(); j++) {
    for (int k = 0; k < f[j].p; k++) {
      if (i % f[j].x != 0) break;
      i /= f[j].x;
    }
  }
  factorization(i, tmp);
  tmp2.clear();
  for (int j = 0; j < (int) tmp.size(); j++) {
    tmp2.push_back(tmp[j].p);
  }
  sort(tmp2.begin(), tmp2.end());
  double x = 0;
  for (int j = 0; j < (int) tmp2.size(); j++) {
    x = x * 0.1 + tmp2[j];
  }
  return x;
}



FactNum allNums[1100];
bool freeNum[1100];


int main() {
  int nCases;
  FactNum curPrice, newPrice, ifact;
  
  /*eratosthenes(1000);
  
  for (int i = 0; i < (int) primes.size(); i++) {
    cout << primes[i] << endl;
  }*/
  
  for (int i = 2; i <= 1000; i++) {
    factorization(i, allNums[i]);
  }
  
  scanf("%d", &nCases);
  for (int iCase = 1; iCase <= nCases; iCase++) {
    int x;
    scanf("%d", &x);
    int nCalls1 = 1;
    curPrice.clear();
    for (int i = 2; i <= x; i++) {
      ppcm(curPrice, allNums[i], newPrice);
      //cout << "curPrice1=" << curPrice << endl;
      if (!isEqual(curPrice, newPrice)) {
        nCalls1++;
        curPrice.swap(newPrice);
      }
    }

    for (int i = 1; i <= x; i++) {
      freeNum[i] = true;
    }
    
    int nCalls2 = (x >= 2 ? 0 : 1);
    curPrice.clear();
    if (x >= 2) {
      while (true) {
        double maxValue = 0;
        int maxI = 0;
        for (int i = 2; i <= x; i++) {
          if (!freeNum[i]) continue;
          int iVal = getValue(i, curPrice);
          if (iVal > maxValue) {
            maxValue = iVal;
            maxI = i;
          }
        }
        //cout << "maxI=" << maxI << " maxValue=" << maxValue << endl;
        if (maxValue == 0) break;
        ppcm(curPrice, allNums[maxI], newPrice);
        assert(!isEqual(curPrice, newPrice));
        curPrice.swap(newPrice);
        nCalls2++;
        freeNum[maxI] = 0;
      }
    }
    
    if (x == 1)
      printf("Case #%i: 0\n", iCase);
    else
      printf("Case #%i: %i\n", iCase, nCalls1 - nCalls2);
  }
  return 0;
}
