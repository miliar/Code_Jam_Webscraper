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

  int n,t,nb,na,hp,mp,hl,ml,ra,rb;

  vector<int> ta,tb;

  vector<pair<int,char> > tall;

  pair<int,int> pt;
  pair<int, char> pa;

  scanf("%d",&n);

  FORN(i,n){
    
    ta.clear();
    tb.clear();
    tall.clear();

    ra=0;
    rb=0;

    scanf("%d",&t);
    
    scanf("%d %d",&na,&nb);
    
    FORN(j,na){
      scanf("%d:%d %d:%d",&hp,&mp,&hl,&ml);
//       pt = make_pair(hp*60+mp, hl*60+ml);
      ta.push_back(hl*60+ml+t);

      pa = make_pair(hp*60+mp, 'a');
      tall.push_back(pa);
    }

    FORN(j,nb){
      scanf("%d:%d %d:%d",&hp,&mp,&hl,&ml);
      //      pt = make_pair(hp*60+mp, hl*60+ml);
      tb.push_back(hl*60+ml+t);

      pa = make_pair(hp*60+mp, 'b');
      tall.push_back(pa);
    }

    sort(all(ta));
    sort(all(tb));
    sort(all(tall));

    FORV(j,tall){

      //     cout<<tall[j].first<<" "<<tall[j].second<<endl;

      if(tall[j].second == 'a'){
	if(tb.size() > 0 && tb[0] <= tall[j].first){
	  tb.erase(tb.begin());
	}else{
	  ra++;
	}
      } else{
	if(ta.size() > 0 && ta[0] <= tall[j].first){
	  ta.erase(ta.begin());
	}else{
	  rb++;
	}
      }
    }

    cout<<"Case #"<<i+1<<": "<<ra<<" "<<rb<<endl;
  }
	
  return 0;
}
 
