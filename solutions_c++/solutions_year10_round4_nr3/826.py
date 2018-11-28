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
#include <string.h>

#define DEBUG(x) cerr << '>' << #x << ": " << x << endl;
#define CLEAR(x,c) memset(x,c,sizeof(x))
#define FOR(i,a,b) for(int i=(a),_b=(b);i<_b;i++)
#define FORM(it,v) for( typeof((v).begin()) it = (v).begin(); it != (v).end(); ++it )
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

#define pi acos(-1.)
#define eps 1e-7
#define aprox(a,b) (fabs((a)-(b))<eps)
#define FIND_MAX(type) (type)(~(1 << ((sizeof(type) * 8) - 1)))

template<typename T> inline T sqr(T a) { return a*a; }
template<typename T> inline int Size(const T& c) { return (int)c.size(); }
template<typename T> inline void checkMin(T& a, T b) { if (b < a) a = b; }
template<typename T> inline void checkMax(T& a, T b) { if (b > a) a = b; }
template<typename T> inline bool isSet(T number, int bit) { return (number&(T(1)<<bit)) != 0; }
template<class T> T abs(T x){return x>0 ? x:(-x);}

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

bool tablero[105][105];
bool tablero2[105][105];

void imprimir(){
   FOR(i,0,10){
      FOR(j,0,10) cout << tablero[i][j];
      cout << endl;
   }
   cout << endl;
}

bool todoMuerto(){
   FOR(i,0,101){
      FOR(j,0,101)
         if (tablero[i][j])
            return false;
   }
   return true;
}

void llenar(int x1, int y1, int x2, int y2){
   for ( int i = x1 ; i <= x2 ; ++i ){
      for ( int j = y1 ; j <= y2 ; ++j ){
         tablero[i][j]=1;
      }
   }
}

bool tieneBacteria(int x, int y){
   return x>=0 && y>=0 && tablero[x][y];
}

void iteracion(){
   memset(tablero2,0,sizeof(tablero2));
   FOR(i,0,105){
      FOR(j,0,105){
         if (!tablero[i][j]){
            if (tieneBacteria(i-1,j) && tieneBacteria(i,j-1)){
               tablero2[i][j]=1;
            }
         }
         else if (tieneBacteria(i-1,j) || tieneBacteria(i,j-1)){
            tablero2[i][j]=1;
         }
      }
   }
   FOR(i,0,105) FOR(j,0,105) tablero[i][j]=tablero2[i][j];
}

int main(){
   int casos;
   cin >> casos;
   FOR(caso,0,casos){
      int celdas;
      cin >> celdas;
      memset(tablero,0,sizeof(tablero));
      
      int a,b,c,d;
      FOR(i,0,celdas){
         cin >> a >> b >> c >> d;
         llenar(a,b,c,d);
         //imprimir();
      }
      int respuesta = 0;
      while(!todoMuerto()){
         //imprimir();
         iteracion();
         ++respuesta;
      }
      
      cout << "Case #" << (caso+1) << ": " << respuesta << endl;
      cerr << "Procesado caso " << (caso+1) << endl;
   }
   return 0;
}


