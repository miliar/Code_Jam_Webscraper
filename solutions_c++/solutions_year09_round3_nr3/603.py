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

#define INF 1125899906842624LL

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


int cantidad(vector<bool> estado, int punto){
   //cerr << " Liberado " << punto << endl;
   int respuesta = 0;
   for (int i = punto+1 ; i < estado.sz ; i++){
      if (estado[i]) ++respuesta;
      else break;
   }
   for (int i = punto-1 ; i >= 0 ; i--){
      if (estado[i]) ++respuesta;
      else break;
   }
   //cerr << respuesta << endl;
   return respuesta;
}


map< pair< vector<bool>, VI > , LL > memoria;

LL funcion(vector<bool> estado, VI porLiberar){
   /*cerr <<"Estado ";
   FOR(i,0,estado.sz) cerr << estado[i] << " ";
   cerr << endl;
   FOR(i,0,porLiberar.sz){
      cerr << porLiberar[i] <<" ";
   }cerr << endl;*/
   SORT(porLiberar);
   if ( memoria.find( mp(estado,porLiberar) ) != memoria.end() ) return memoria[mp(estado,porLiberar)];
   LL respuesta = INF;
   if (porLiberar.empty()) return 0;
   FOR(i,0,porLiberar.sz){
      estado[porLiberar[i]] = 0;
      int temp = porLiberar[i];
      VI porLiberarN;
      FOR(j,0,porLiberar.sz){
         if (i != j) porLiberarN.pb(porLiberar[j]);
      }
      checkMin(respuesta,funcion(estado,porLiberarN) + cantidad(estado,porLiberar[i]));
      estado[porLiberar[i]] = 1;
   }
   return respuesta;
}

int main(){
   int casos;
   cin >> casos;
   FOR(caso,0,casos){
      memoria.clear();
      int cantidad , porlibCant;
      cin >> cantidad >> porlibCant;
      vector<bool> estado(cantidad,1);
      VI porLiberar;
      FOR(i,0,porlibCant){
         int temp;
         cin >> temp;
         porLiberar.pb(temp-1);
      }
      cout << "Case #" << (caso+1) << ": " << funcion(estado,porLiberar) << endl;
   }
   return 0;
}


