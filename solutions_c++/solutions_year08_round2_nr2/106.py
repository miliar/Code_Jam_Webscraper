#include <algorithm>
#include <string>
#include <vector>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <cstring>
#include <cctype>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <list>
#include <functional>
#include <numeric>
#include <bitset>
#include <ext/hash_set>
#include <ext/hash_map>
#include <stdexcept>
using namespace std;
using namespace __gnu_cxx;
#define foreach(i,c) for(__typeof((c).begin()) i=(c).begin();i!=(c).end();++i)
template<class a,class b>
ostream& operator<<(ostream& os,pair<a,b> p) {os<<"("<<p.first<<","<<p.second<<")";return os;}
template<typename T>
ostream& operator<<(ostream& os, vector<T> vec) {os<<"{";foreach(i,vec) {os<<*i; if (i != --vec.end()) os<<",";}os<<"}";return os;}
template<typename T,typename _A=allocator<T> >
struct dvect: public vector<T,_A> { dvect(size_t n=0,const T& val=T()):vector<T,_A>(n,val) {}
  template<typename _InputIterator> dvect(_InputIterator f,_InputIterator l):vector<T,_A>(f,l) {}
  dvect(const vector<T, _A>& v) : vector<T, _A>(v) {}
  const T& operator[](int n) const throw();  T& operator[](int n) throw(); };
template<typename T,typename _A>
const T& dvect<T, _A>::operator[](int n) const throw() {
  try {return this->at(n);}
  catch(out_of_range e) {cerr << "Vector index out of bounds: "<<n<<endl;
    cerr<< " size: " << this->size()<< endl << " index: " << n << endl;
    cerr<<e.what()<<endl;
    cerr << *this << endl;
    throw;
  }
}
template<typename T,typename _A>
T& dvect<T, _A>::operator[](int n) throw(){
  return const_cast<T&>(const_cast<const dvect*>(this)->operator[](n));
}
#define vector dvect

typedef long long ll;
const int infinito = 1000000000;

const int maxn = 1001;

#define raizn 1001
#define maxn (raizn * raizn)  // máximo número a comprobar

int 
  menorfac[maxn + 1],  // menor factor primo que divide a n
  queda[maxn + 1];     // mayor factor de n primo con menorfac[n]
vector<int> primo;

/* Calcula los valores de menorfac y queda, para 1 <= i <= maxn, en O(maxn·log maxn)
 * Supone que menorfac está inicializado a 0 (ya que es global) 
 * Los primos son los que cumplan menorfac[i] = i, i != 1;
 * las potencias de primos cumplen queda[i] = 1  */
void hazcriba() {
  int n, i, j;
  queda[1] = 1;
  for (n = 2; n <= maxn; n++) {
    queda[n] = 1;
    if (n & 1) menorfac[n] = n; 
    else {
      menorfac[n] = 2;
      queda[n] = n;
      while (!(queda[n] & 1)) queda[n] >>= 1;
    }
  }
 
  for (n = 3; n <= raizn; n += 2) if (menorfac[n] == n)
    for (i = n; (j = n * i) <= maxn; i += 2) if (menorfac[j] == j) {
      menorfac[j] = n;
      queda[j] = i;
      while (queda[j] % n == 0) queda[j] /= n;
    }
  
  // Saca los primos (opcional)
  primo.clear();
  primo.push_back(2);
  for (n = 3; n <= maxn; n++) if (menorfac[n] == n) primo.push_back(n);
}

const int mtam = 1000000 + 1;
int padre[mtam], rango[mtam];
bool criba[mtam];

int find(int a) {
  if (a == padre[a]) return a; return padre[a] = find(padre[a]);
}

void merge(int a, int b) {
  a = padre[a]; b = padre[b];
  if (a == b) return;
  if (rango[a] < rango[b]) padre[a] = b;
  else {
    padre[b] = a;
    if (rango[a] == rango[b]) rango[a]++;
  }
}
bool esprimo(int n) {
  for (int i = 2; i < n; ++i)
    if (n % i == 0) return false;
  return true;
}

int main() {
  int casos;
  hazcriba();
  scanf("%i\n", &casos);
  for (int caso = 1; caso <= casos; ++caso) {
    printf("Case #%i: ", caso);
    ll a, b, p;
    scanf("%lli%lli%lli", &a, &b, &p);
    for (int i = 0; i <= b - a; ++i) {
      padre[i] = i; 
      rango[i] = 0;
    }

    fill(&criba[0], &criba[b - a + 1], true);
    vector<ll> pr;
    for (int i = 0; i < primo.size() && primo[i] <= b; ++i) {
      if (primo[i] >= p) 
        pr.push_back(primo[i]);
      ll j = (a + primo[i] - 1) / primo[i] * primo[i];
      for (; j <= b; j += primo[i])
        criba[j - a] = false;
    }
    for (int i = 0; i <= b - a; ++i)
      if (criba[i]) pr.push_back((ll)i + a);

    for (int i = 0; i < pr.size(); ++i)
      if (pr[i] >= p) {
        ll j = (a + pr[i] - 1) / pr[i] * pr[i], antj = -1;
        for (; j <= b; j += pr[i]) {
          if (antj >= 0) merge(find(antj - a), find(j - a));
          antj = j;
        }
      }
    int res = 0;
    for (int i = 0; i <= b - a; ++i)
      if (padre[i] == i) ++res;
    printf("%i\n", res);
  }
  return 0;
}
