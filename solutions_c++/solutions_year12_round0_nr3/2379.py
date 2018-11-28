#include<iostream>
using namespace std;

int dep(int a){
  int ret = 1;
  while(a /= 10) ++ret;
  return ret;
}

int doit(int a, int d){
  int ret = a / 10;
  int f = a % 10;
  while(--d) f *= 10;
  ret += f;
  return ret;
}

int fes(int a, int b){
  int c = a, ret = 0;
  int d = dep(a);
  do {
    c = doit(c, d);
    if(c > a and c <= b) ++ret;
  } while(c != a);
  return ret;
}

int main(){
  int n;
  int i = 0;
  cin >> n;
  while(n--){
    int a, b;
    cin >> a >> b;
    int ret = 0;
    for(int r = a; r <= b; ++r){
      ret += fes(r, b);
    }
    cout << "Case #" << ++i << ": " << ret << endl;
  }
}
