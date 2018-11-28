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

#define CLEAR(x,c) memset(x,c,sizeof(x))
#define FOR(i,a,b) for(int i=(a),_b=(b);i<_b;i++)
#define FORD(i,a,b) for(int i=(b)-1,_b=(a);i>=_b;i--)
#define FORF(i,a,b,c) for(double i=(a),_b=(b);i<_b;i+=c)
#define sz size()
#define mp make_pair
#define X first
#define Y second
#define pb push_back
#define SORT(x) sort(all(x))
#define REVERSE(x) reverse(all(x))
#define CLEAR(x,c) memset(x,c,sizeof(x))
#define all(x) (x).begin(),(x).end()
#define MEM(tipo,tam) (tipo)malloc(sizeof(tipo)*tam)

#define pi acos(-1.)
#define eps 1e-7
#define aprox(a,b) (fabs((a)-(b))<eps)

template<typename T> inline T sqr(T a) { return a*a; }
template<typename T> inline int Size(const T& c) { return (int)c.size(); }
template<typename T> inline void checkMin(T& a, T b) { if (b < a) a = b; }
template<typename T> inline void checkMax(T& a, T b) { if (b > a) a = b; }
template<typename T> inline bool isSet(T number, int bit) { return (number&(T(1)<<bit)) != 0; }
template<class T> T abs(T x){return x>0 ? x:(-x);}

using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef vector<long> VL;

int n,k,b,t;
VI posiciones(100,0);
VI velocidad(100,0);

int mejor(int maximo){
   int respuesta = -1;
   FOR(pollito,0,maximo){
      if (respuesta == -1 || (double)(b-posiciones[pollito])/(double)velocidad[pollito] < (double)(b-posiciones[respuesta])/(double)velocidad[respuesta] ) {
         respuesta = pollito;
      }
   }
   return respuesta;
}

int main(){
   int casos;
   cin >> casos;
   FOR(caso,0,casos){
      cin >> n >> k >> b >> t;
      FOR(i,0,n) cin >> posiciones[i];
      FOR(i,0,n) cin >> velocidad[i];
      int respuesta = 0;
      bool malo = false;
      int cantQueNoLLega = 0;
      FORD(pollito,0,n){
         if (k == 0) break;
         if ((double)(b-posiciones[pollito])/(double)velocidad[pollito] <= (double)t){
            --k;
            respuesta += cantQueNoLLega;
         }else{
            ++cantQueNoLLega;
         }
      }
      if (k!=0)
         cout << "Case #" << (caso+1) << ": IMPOSSIBLE" << endl;
      else{
         cout << "Case #" << (caso+1) << ": " << respuesta << endl;
//         assert(respuesta != n);
      }
   }
   return 0;
}


