#include <vector>
#include <iostream>

#include <stdio.h>

using namespace std;

bool solve(long long,long long ,long long);

int main(){
  int num_cases;
  cin >> num_cases;
  for(int i = 0; i < num_cases; i++){
    long long n, pd, pg;
    cin >> n >> pd >> pg;
    bool r = solve(n,pd,pg);
    if(r)
      cout << "Case #" << i+1 << ": Possible" << endl;
    else 
      cout << "Case #" << i+1 << ": Broken" << endl;
  }
}

long long gcd(long long a, long long b){
  if (b > a) swap(a,b);
  long long r = a % b;
  if(r == 0) return b;
  else return gcd(b,r);
}

bool solve(long long n, long long pd, long long pg){
  if(pd != 0){
    int g = gcd(100,pd);
    int min = 100/g;
    if(n < min) return false;
  }
  if(pg == 100) {
    if(pd == 100) return true; else return false;
  } 
  if(pg == 0) {
    if(pd == 0) return true; else return false;
  }
}
