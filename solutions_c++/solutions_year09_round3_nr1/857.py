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

//Rapida potencia
template< class Int>
Int fastPow( Int a , int b){
    if (b == 0) return 1;
    if ( b == 1 ) return a;
    if ( b&1 ) return a*fastPow(a,b-1);
    return fastPow(a*a,b/2);
}


int main(){
   int casos;
   cin >> casos;
   FOR(caso,0,casos){
      string numero;
      cin >> numero;
      int cantidadDistinto = 0;
      bool contado[300];
      CLEAR(contado,0);
      FOR(i,0,numero.sz){
         if (!contado[numero[i]]){
            contado[numero[i]] = 1;
            cantidadDistinto++;
         }
      }
      map<char,int> mapa;
      mapa[numero[0]] = 1;
      int asignado = 0;
      FOR(i,1,numero.sz){
         if (!(mapa.count(numero[i])>0)){
            mapa[numero[i]] = asignado++;
            if (asignado == 1) ++ asignado;
         }
      }
      VI resultado;
      FOR(i,0,numero.sz){
         resultado.pb(mapa[numero[i]]);
      }

      if (cantidadDistinto == 1) ++cantidadDistinto;
      //FOR(i,0,resultado.sz) cerr << resultado[i] << endl;
      LL respuesta = 0;
      for(int i = resultado.sz-1 ; i>=0;i--){
         //cerr << "fastPow(cantidadDistinto,i)" << fastPow(cantidadDistinto,resultado.sz-1-i) << endl;
         //cerr << "resultado[resultado.sz-i-1]"  << resultado[i] << endl;
         respuesta += fastPow(cantidadDistinto,resultado.sz-1-i)*resultado[i];
         //cerr << respuesta << endl;
      }
      cout << "Case #" << (caso+1) << ": " << respuesta << endl;
   }
   return 0;
}


