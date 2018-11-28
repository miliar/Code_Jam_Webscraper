#include <iostream>
#include <string>

#include <cassert>
using namespace std;

int bitpos[]={1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072,262144,524288,1048576,2097152,4194304,8388608,16777216,33554432,67108864,134217728,268435456,536870912,1073741824};
  


int main() {

  int T,N,K;
  cin >> T;
  for (int i=1;i<=T;i++) {
    cin >> N >> K;
    //cout << bitpos[N-1] << endl;
    //cout << (bitpos[N-1] & K) << endl;
    bool onoff = true;
    for (int j= N-1;j>=0;j--) {
      if ((bitpos[j]&K)==0) onoff=false;
    }
    if (onoff) {
      cout << "Case #"<<i<<": ON" <<endl;
    } else {
      cout << "Case #"<<i<<": OFF" << endl;
    }
  }
}
