#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <limits>
#include <fstream>

using namespace std;

const double EPS = 1e-9;

struct DDMY{ ostringstream o; template<class T>DDMY& operator,(const T &t){o<<t<<",";return *this;} string operator*(){ return o.str().substr(0,o.str().size()-1); } };
#define debug(args...) cout<<"("#args")=("<< *(DDMY(),args)<<") (L"<<__LINE__<<")"<<endl

template<class T> std::ostream &operator<<(std::ostream &o,const std::vector<T> &v)
{ o << "["; for(std::size_t i=0;i<v.size();i++) o << v[i] << (i < v.size()-1 ? ",":""); return o << "]"; }
template<class T,class U> std::ostream &operator<<(std::ostream &o,const std::pair<T,U> &v)
{ return o << v.first << ":" << v.second; }
template<class T,class U> std::ostream &operator<<(std::ostream &o,const std::map<T,U> &v)
{ o << "{"; typename std::map<T,U>::const_iterator i=v.begin(),j=i;++j;for(;i!=v.end();++i,++j) o << *i << (j!=v.end()? ",":""); return o << "}"; }
template<class T> std::ostream &operator<<(std::ostream &o,const std::set<T> &v)
{ o << "{"; typename std::set<T>::const_iterator i=v.begin(),j=i;++j;for(;i!=v.end();++i,++j) o << *i << (j!=v.end()? ",":""); return o << "}"; }

int solve(int N, int S, int p, vector<int> v){
  sort(v.rbegin(),v.rend());
  int res = 0;
  if(p == 0) return v.size();
  //debug(N,S,p,v);
  for(int i = 0; i < v.size(); i++){
    //debug(v[i],v[i]/3,v[i]%3,S,res);
    if(v[i] / 3 >= p){
      res++;
      continue;
    }
    if(v[i] % 3 == 0){
      if(p != 1 && v[i] / 3 == p - 1 && S > 0){
        res++;
        S--;
      }
    }else if(v[i] % 3 == 1){
      if(v[i] / 3 == p - 1){
        res++;
        continue;
      }
    }else if(v[i] % 3 == 2){
      if(v[i] / 3 == p - 1){
        res++;
        continue;
      }
      if(v[i] / 3 == p - 2 && S > 0){
        res++;
        S--;
        continue;
      }

    }
  }
  return res;
}



int main(int argc, char *argv[]){
  ios::sync_with_stdio(false);

  int T;
  cin >> T;
  for(int i = 0; i < T; i++){
    int N,S,p;
    vector<int> v;
    cin >> N >> S >> p;
    for(int j = 0; j < N; j++){
      int k;
      cin >> k;
      v.push_back(k);
    }
    cout << "Case #" << (i+1) << ": " << solve(N,S,p,v) << endl;
  }

  return 0;
}
