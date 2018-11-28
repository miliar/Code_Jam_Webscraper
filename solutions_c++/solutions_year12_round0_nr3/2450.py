#include<iostream>
#include<string>
#include<cstring>
#include<algorithm>
#include<vector>
using namespace std;

bool rec(int a,int b) {
  int sa = 1;
  for(; sa<a; sa*=10);
  int a2=a;
  while(a) {
    if(a2 == b) return true;
    a2 += sa*(a%10);
    a2/=10;        
    a/=10;
  }
  return false;
}

int A[100];

int rec2(int a,int b) {
  int sa = 1;
  for(; sa<a; sa*=10);
  int a2 = a;
  int a3 = a;
  int ss = 0;
  while(a) {
    if(a2 > a3 && a2<=b) { 
      A[ss++] = (a2);
    }
    a2 += sa*(a%10);
    a2/=10;        
    a/=10;
  }
  sort(A, A+ss);
  return (unique(A, A+ss) - A);
}

int main() {
  ios_base::sync_with_stdio(false);
  int k;
  cin >> k;
  for(int t=1; t<=k; t++) {
    int a,b;
    cin >> a>>b;
    int r=0;
    for(int i=a; i<=b; i++) {
        //if(rec(i,j)) { 
        //  r++; 
          //cerr << i << " : " << j << endl; 
        //}
        r += rec2(i,b);
    }
    
    cout << "Case #" << t << ": " << r << endl;
  }
  return 0;
}
