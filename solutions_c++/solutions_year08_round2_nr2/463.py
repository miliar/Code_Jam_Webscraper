#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>
using namespace std;

typedef long long int64;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;

#define _CRT_SECURE_NO_WARNINGS
#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define Ford(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define Rep(i,n) for (int i(0),_n(n); i < _n; ++i)
#define Repd(i,n) for (int i((n)-1); i >= 0; --i)
#define Fill(a,c) memset(&a, c, sizeof(a))
#define MP(x, y) make_pair((x), (y))
#define All(v) (v).begin(), (v).end()

template<typename T, typename S> T cast(S s) {
	stringstream ss;
	ss << s;
	T res;
	ss >> res;
	return res;
}

template<typename T> inline T sqr(T a) { return a*a; }
template<typename T> inline int Size(const T& c) { return (int)c.size(); }
template<typename T> inline void checkMin(T& a, T b) { if (b < a) a = b; }
template<typename T> inline void checkMax(T& a, T b) { if (b > a) a = b; }

char buf[1024*1024];

int GCD(int a, int b)
{
 while( 1 )
 {
  a = a % b;
  if( a == 0 )
   return b;
  b = b % a;
  if( b == 0 )
   return a;
 }
}

int primesub(int f) {
 for (int i = f/2; i>1; i--) {
  if (0==f%i)
   return primesub(i);
  }
  return f;
}

int prime(int a, int b) {
 int f = GCD(a, b);
 return primesub(f);
}

int main() {
 freopen("B-small-attempt0.in", "rt", stdin);
 freopen("B-small-attempt0.out", "wt", stdout);
 gets(buf);
 For(test, 1, atoi(buf)) {
  int res = 0;
  int A, B, P; 
  scanf("%d %d %d", &A, &B, &P);
  int s[1+B-A];
  for (int i = 0; i<1+B-A; i++) 
   s[i]=i;
  for (int i = A; i<B; i++) {
   for (int j = i+1; j<=B; j++) {
    int set1 = s[i-A];
    int set2 = s[j-A];
    if (set1!=set2) {
     if (P<=prime(i, j)) {
      for (int i = 0; i<1+B-A; i++) 
       if (s[i]==set2) s[i]=set1;
     } 
    }
   }
  } 
  int c[1+B-A];
  for (int i = 0; i<1+B-A; i++) c[i]=0;
  for (int i = 0; i<1+B-A; i++) { 
   if (0==c[s[i]]) {
    c[s[i]]=1;
    res+=1;
   } 
  }
  printf("Case #%d: %i\n", test, res);
 }
 exit(0);
}

