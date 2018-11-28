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

char str[] = {
  'y', // a
  'n', // b
  'f', // c
  'i', // d
  'c', // e
  'w', // f
  'l', // g
  'b', // h
  'k', // i
  'u', // j
  'o', // k
  'm', // l
  'x', // m
  's', // n
  'e', // o
  'v', // p
  'z', // q
  'p', // r
  'd', // s
  'r', // t
  'j', // u
  'g', // v
  't', // w
  'h', // x
  'a', // y
  'q', // z
};



int main(int argc, char *argv[]){
  ios::sync_with_stdio(false);

  int T;
  cin >> T;
  string line;
  getline(cin, line);
  for(int i = 0; i < T; i++){
    string line2;
    getline(cin, line);
    for(int j = 0; j < line.size(); j++){
      if(line[j] == ' '){
        line2 += ' ';
        continue;
      }
      for(int k = 0; k < 27; k++){
        if(line[j] == str[k]){
          line2 += k + 'a';
          goto success;
        }
      }
    success:;
    }
    cout << "Case #" << (i+1) << ": " << line2 << endl;
  }

  return 0;
}
