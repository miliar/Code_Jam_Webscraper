#include <iostream>
#include <vector>
#include <string.h>
#include <functional>
#include <algorithm>
#include <math.h>
#include <cstdio>
#include <queue>
#include <string>
#include <sstream>
#include <cstdlib>
#include <map>
#include <fstream>
using namespace std;
int A, B;

template<class T> string toString(T n){ostringstream ost;ost<<n;ost.flush();return ost.str();}
int toInt(string s){int r=0;istringstream sin(s);sin>>r;return r;}

vector<int> vec;

void recycle(int j, int B){
  string s = toString(j);
  int cnt = 0;
  for(int i = 1; i < s.size();++i){
    string p = s.substr(s.size() - i, s.size());
    string q = s.substr(0,s.size() - i);
    p += q;
    int check = toInt(p);
    if(check <= B && check > j){
      vec.push_back(check);
    }
  }
  vec.erase(unique(vec.begin(),vec.end()), vec.end());
}

int i, j, n, cnt;
string str;

int main(){
  ifstream myFile;
  myFile.open("small.in");
  getline(myFile,str);
  stringstream sin(str);
  sin>>n;
  for(i = 0; i < n; ++i){
    getline(myFile,str);
    stringstream sin(str);
    sin>>A>>B;
    vec.clear();
    for(j = A; j < B; ++j){
      recycle(j, B);
    }
    cout<<"Case #"<<i + 1<<": "<<vec.size()<<endl;
  }
  return 0;
}
