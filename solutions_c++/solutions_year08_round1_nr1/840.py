#include <iostream>
#include <limits>
#include <vector>
#include <iterator>
#include <cstdio>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <utility>
#include <cstring>
#include <cmath>
#include <sstream>
#include <functional>

//Plantilla conjuntos
#define unionc(a,b,c) set_union(a.begin(),a.end(),b.begin(),b.end(),inserter(c,c.begin()))
#define interc(a,b,c) set_intersection(a.begin(),a.end(),b.begin(),b.end(),inserter(c,c.begin()))
#define diferc(a,b,c) set_diference(a.begin(),a.end(),b.begin(),b.end(),inserter(c,c.begin()))
#define subcnj(a,b,c) includes(a.begin(),a.end(),b.begin(),b.end())

//Plantilla contenedores
#define esta(v,n) find(v.begin(),v.end(),n)!=v.end()
#define all(v) v.begin(),v.end()

//Plantilla para for
#define FORV(I,V) for(int I=0;I<V.size();I++)
#define FORN(I,N) for(int I=0;I<N;I++)
#define FORAB(I,A,B) for(int I=A;I<B;I++)

//Plantilla para INF y -INF
#define INF(T) numeric_limits<T>::has_infinity?numeric_limits<T>::infinity():numeric_limits<T>::max()
#define MINF(T) numeric_limits<T>::has_infinity?(-1*(numeric_limits<T>::infinity())):numeric_limits<T>::min()

using namespace std;


int main(){

  int c,n,val;
  int resp = INF(int),p;
  vector<int> a,b;
  cin >> c;

  FORN(i,c){
    cin >> n;
    a.clear();
    b.clear();
    FORN(j,n){
      cin>>val;
      a.push_back(val);
    }

    FORN(j,n){
      cin>>val;
      b.push_back(val);
    }

    sort(all(a));
    sort(all(b));

    p = 0;
    resp =  INF(int);
    FORV(j,a){
      p += a[j] * b[b.size() - 1 - j];
    }

    resp = p;



    cout<<"Case #"<<i+1<<": "<<resp<<endl;
  }
  
  
  return 0;
}
