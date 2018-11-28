#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <list>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <complex>
#include <cstdio>
#include <cassert>
#include <cmath>
#include <numeric>
#include "regex.h"

#define DEBUG(x) cerr << '>' << #x << ": " << x << endl;
#define CLEAR(x,c) memset(x,c,sizeof(x))
#define FOR(i,a,b) for(int i=(a),_b=(b);i<_b;i++)
#define FORD(i,a,b) for(int i=(b)-1,_b=(a);i>=_b;i--)
#define FORF(i,a,b,c) for(double i=(a),_b=(b);i<_b;i+=c)
#define FORL(i,a,b) for(long long i=(a),_b=(b);i<_b;i++)
#define FORC(i, n) for (typeof (n.begin()) i = n.begin() ; i != n.end() ; i++)
#define sz size()
#define mp make_pair
#define X first
#define Y second
#define pb push_back
#define SORT(x) sort(all(x))
#define REVERSE(x) reverse(all(x))
#define CLEAR(x,c) memset(x,c,sizeof(x))
#define all(x) (x).begin(),(x).end()
#define SWAP(a,b) a^=b; b^=a; a^=b

#define pi acos(-1.)
#define eps 1e-7
#define aprox(a,b) (fabs((a)-(b))<eps)
#define FIND_MAX(type) (type)(~(1 << ((sizeof(type) * 8) - 1)))

template<typename T> inline T sqr(T a) { return a*a; }
//template<typename T> inline int Size(const T& c) { return (int)c.size(); }
template<typename T> inline void checkMin(T& a, T b) { if (b < a) a = b; }
template<typename T> inline void checkMax(T& a, T b) { if (b > a) a = b; }
template<typename T> inline bool isSet(T number, int bit) { return (number&(T(1)<<bit)) != 0; }
template<class T> T abs(T x){return x>0 ? x:(-x);}
/*template<class T> T& operator >?= (T& x, T y) {if(y>x) x=y; return x;}
template<class T> T& operator <?= (T& x, T y) {if(y<x) x=y; return x;}
template<class T> T operator >? (T x, T y) {return x>y?x:y;}
template<class T> T operator <? (T x, T y) {return x<y?x:y;}*/

using namespace std;

template<typename T, typename S> T cast(S s) {
   stringstream ss;
   ss << s;
   T res;
   ss >> res;
   return res;
}

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef vector<long> VL;


int main(){
   int casos;
   cin >> casos;
   FOR(caso,0,casos){
      string numeros;
      cin >> numeros;
      string original = numeros;
      next_permutation(all(numeros));
      
      if (original >= numeros){
         int i = 0;
         cout << "Case #" << (caso+1) << ": ";
         int menor = 10;
         FOR(i,0,numeros.sz) if (numeros[i]!= '0' )checkMin(menor,numeros[i]-'0');
         //cerr << "Menor " << menor << " " << numeros << endl;
         FOR(i,0,numeros.sz) if (numeros[i] == menor+'0') {numeros.erase(i,1); DEBUG(i);break;}
         //cout << "numeros " << numeros << endl;
         SORT(numeros);
         cout << menor << "0" << numeros << endl;
      }else{
         cout << "Case #" << (caso+1) << ": " << numeros << endl;
      }
   }
   return 0;
}


