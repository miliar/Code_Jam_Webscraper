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


int M[2000];
int P;
int precios[2000];
VS losPrecios(11);

bool todoBien(int inicio , int fin){
   for ( int i = inicio ; i <= fin ; ++i ){
      if (M[i]>0) return false;
   }
   return true;
}

int gastado = 0;

void resolver(int inicio, int fin){
   //cout << "Resolver " << inicio << " " << fin << endl;
   if (todoBien(inicio,fin)) return;
   for ( int i = inicio ; i <= fin ; ++i ) --M[i];
   gastado += precios[0];
   resolver(inicio,(fin+inicio)/2);
   resolver((fin+inicio)/2+1,fin);
}

int main(){
   int casos;
   cin >> casos;
   FOR(caso,0,casos){
      cin >> P;
      FOR(i,0,(1<<P)){
         cin >> M[i];
         M[i] = P-M[i];
      }
      
      losPrecios.clear();
      string tmp;
      getline(cin,tmp);
      FOR(i,0,P) getline(cin,losPrecios[i]);
      //FOR(i,0,P) cout << " a " << losPrecios[i] << endl;
      REVERSE(losPrecios);
      int posicion = 0;
      gastado = 0;
      FOR(i,0,P){
         stringstream ss;
         ss << losPrecios[i];
         int price;
         while(ss >> price){
            precios[posicion] = price;
            ++posicion;
         }
      }
      int cantidad = 0;
      resolver(0,(1<<P)-1);
      cout << "Case #" << (caso+1) << ": " << gastado << endl; 
      cerr << "Procesado caso " << (caso+1) << endl;
   }
   return 0;
}


