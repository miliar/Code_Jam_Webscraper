#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <string>
#include <utility>
#include <vector>
using namespace std;

#define f(i,n) for(int i = 0; i < (n); ++i)
#define size(v) ((int)v.size())

typedef vector<int> vi;
typedef vector<vi> vvi;

int main(){
  int T;
  cin >> T;
  f(i,T){
    long long a, b, c;
    cin >> a >> b >> c;
    string ret = "Possible";
    bool d = true;
    if(a < 100){
      f(j,a){
        if((((1 + j) * b) % 100) == 0){
          d = false;
          break;
        }
      }
      if(d) ret = "Broken";
    }
    if(b < 100 and c == 100) ret = "Broken";
    if(b > 0 and c == 0) ret = "Broken";
    cout<<"Case #"<<1+i<<": "<<ret<<endl;
  }
}
