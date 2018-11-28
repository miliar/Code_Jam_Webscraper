#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<queue>
#include<sstream>
#include<set>
#include<map>
#include<cstdio>
#include<cstdlib>
#include<cstring>

using namespace std;


int main(){
  int t;
  cin >> t;
  for(int c = 1; c<=t; c++){
    int n,k;
    cin >> n >> k;
    int ff = 1<<n;
    if(k > ff) k = k % ff;
    cout << "Case #" << c << ": ";
    if(k == (ff-1)){
      cout << "ON" << endl;
    }else {
      cout << "OFF" << endl;
    }
  }
  return 0;
}
