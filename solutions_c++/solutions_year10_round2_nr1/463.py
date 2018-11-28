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

int n,m;
set<string> existen;

void leer(){
   FOR(i,0,n){
      string temp;
      cin >> temp;
      FOR(j,0,temp.size()){
         if (temp[j]=='/') temp[j]=' ';
      }
      stringstream ss;
      ss << temp;
      string temp2;
      string buff;
      while(ss >> temp2){
         buff += "/" + temp2 ;
         //cout << "Insertando " << buff << endl;
         existen.insert(buff);
      }
   }
}

int main(){
   int casos;
   cin >> casos;
   FOR(caso,0,casos){
      cin >> n >> m;
      existen.clear();
      leer();
      int respuesta = 0;
      FOR(i,0,m){
         string temp,temp2;
         cin >> temp;
         //cout << "Temp " << temp << endl;
         string buff ;
         stringstream ss;
         FOR(j,0,temp.size()){
            if (temp[j]=='/') temp[j]=' ';
         }
         //cout << "Temp2 " << temp << endl;
         ss << temp;
         
         while(ss>>temp2){
            //cout << "Leyo " << temp2 << endl;
            //cout << (buff + temp2) << endl;
            buff += "/" + temp2;
            if (existen.find(buff) == existen.end()){
               //cout << "No existia " << endl;
               existen.insert(buff);
               ++respuesta;
               break;
            }else{
               ;//cout << "Ya existia" << endl;
            }
         }
         while(ss>>temp2){
            ++respuesta;
            buff += "/" + temp2;
            //cout << "Creo " << (buff) << endl;
            existen.insert(buff);
         }
         //cout << respuesta << endl;
      }
      cout << "Case #" << (caso+1) << ": " << respuesta << endl;
   }
    return 0;
}


