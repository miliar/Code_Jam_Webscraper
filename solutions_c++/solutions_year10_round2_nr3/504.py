#include <string.h>
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

int n;

int memoria[30];

bool valido(int conjunto, int bit){
   //cout <<" Conjutno " << conjunto << "Bit " << bit << endl;
   if (bit < 0) return true;
   if (!(1<<(bit) & conjunto)) return false;
   int pos = -1;
   FOR(i,0,bit){
      if (1<<i & conjunto){
         ++pos;
      }
   }
   //cout << "Nume " << (bit+2) << "Esta en pos " << pos << endl;
   return valido(conjunto,pos);
}

int main(){
   int casos;
   cin >> casos;
   memset(memoria,-1,sizeof(memoria));
   FOR(caso,0,casos){
      cin >> n;
      int respuesta = 0;
      if (memoria[n]!=-1) respuesta = memoria[n];
      else{
         int conjunto = 1<<(n-2);
         int tope = 1<<(n-1);
         FOR(it,conjunto,tope){
            if (valido(it,n-2)){
               ++respuesta;
            }
            respuesta %= 100003;
         }
      }
      memoria[n]=respuesta;
      cout << "Case #" << (caso+1) << ": " << respuesta << endl;
   }
   return 0;
}


