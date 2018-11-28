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

  int n,s,q, resp;
  string ts;
  char line[256];
  cin >> n;

  vector<string> ss;
  vector<string> qs;
  
  vector<string>::iterator it1, it2;

  FORN(i,n){
    cin >> s;
    resp = -1;

    qs.clear();
    ss.clear();

    cin.getline(line,256);
    FORN(j,s){
      cin.getline(line,256);
      ts = line;
      ss.push_back(ts);
    }

    cin >> q;

    if(q  == 0){
      resp = 0;
    }

    cin.getline(line,256);
    FORN(j,q){
      cin.getline(line,256);
      ts = line;
      qs.push_back(ts);

    }

    it1 = qs.begin();
    it2 = qs.begin();

    while(it1 != qs.end()){
      
      FORV(j,ss){
	if(it1 < find(it2,qs.end(),ss[j])){
	  it1 = find(it2,qs.end(),ss[j]);
	}
      }

      it2 = it1;

      resp++;
    }
    
    cout << "Case #" << i + 1 << ": " << resp <<endl;
  }
	
  return 0;
}
