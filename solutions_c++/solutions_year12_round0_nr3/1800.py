#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
using namespace std;

string itos( int n){
  string ret;
  int t = 0;
  while(n>0){
    ret += (n%10)+'0';
    n/=10;
  }
  reverse(ret.begin(), ret.end());
  return ret;
}

int main(){
  int T;
  cin >> T;
  for (int testCase = 1; testCase<=T; testCase++){
    int A,B;
    cin >> A >> B;
    int ans = 0;
    int d = 0;
    int dd = 1;
    for (;dd<=A;dd*=10,d++); dd/=10;
    for (int n=A; n<B; n++){
      int t = n;
      int ch[d];
      for (int i=0; i<d-1; i++){
	t = t/10 + (t%10)*dd;
	ch[i] = t;
	bool f = true;
	for (int j=0; j<i; j++){
	  if (ch[j] == t) f = false;
	}
	if (f && t <= B &&  n<t){
	  ans++;
	}
      }

    }
    printf ("Case #%d: %d\n",testCase,ans);
  }
}
