#include<iostream>
#include<string>
#include<cstring>
#include<algorithm>
using namespace std;

int D[105*105];

int main() {
  ios_base::sync_with_stdio(false);
  int k;
  cin >> k;
  for(int t=1; t<=k; t++) {
    memset(D, 0, sizeof(int)*105*105);
    int n,s,p;
    cin >> n >> s >> p;
    //cout << s << endl;
    s++;
    for(int i=0; i<n;i++) {
      int akt;
      cin >> akt;
      int ns = (akt+2)/3;
      int ns2 = (akt<3) ? akt : (akt+4)/3;
      //cout << "p=" << p<< " akt="<<akt<< " " << ns << endl;
      for(int j=0; j<s; j++) {
        int prev = i ? D[s*(i-1) + j] : 0;
        D[s*i+j] = max( ( ns>=p ) ? prev+1 : prev, D[s*i+j] );
        if(ns<29 && j+1<s ) D[s*i+j+1] = (ns2>=p) ? (prev+1) : prev;
        // cerr << i << " " << j << " = " << D[s*i+j] << endl;
      }
    }
    cout << "Case #" << t << ": " << D[s*n-1] << endl; 
  }
  return 0;
}
