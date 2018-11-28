#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <vector>
using namespace std;

void go(int Q) {
  int n;
  cin>>n;
  vector<string> bot(n);
  vector<int> pos(n);
  for (int i=0;i<n;i++) {
    cin>>bot[i]>>pos[i];
  }
  int bPos = 1, bTime=0;
  int oPos = 1, oTime=0;
  for (int i=0;i<n;i++) {
    if (bot[i] == "O") {
      oTime = max(oTime+abs(pos[i]-oPos),bTime)+1;
      oPos = pos[i];
    }
    else if (bot[i] == "B") {
      bTime = max(bTime+abs(pos[i]-bPos),oTime)+1;
      bPos = pos[i];
    } else {
      throw 2;
    }
  }
  cout << "Case #"<<Q<<": " << max(bTime,oTime)<<endl;
}
int main() {
  int tc;
  cin>>tc;
  for (int i=1;i<=tc;i++) go(i);
  
}
