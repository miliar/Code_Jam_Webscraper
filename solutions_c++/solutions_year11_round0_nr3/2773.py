#include <iostream>
#include <stdio.h>
#include <string.h>
#include <string>

#include <vector>
#include <map>
#include <algorithm>

#define INF 1<<25

using namespace std;

int nMax;
vector<int> values;
long long sum;
map< pair<int,long long> ,long long> mem;

long long f(int index, long long have){
  if ( index >= nMax ){
    if (have == 0LL) {
      return 0;
    }else {
      return -1*INF;
    }
  }

  if ( mem.find( make_pair( index, have ) ) != mem.end() ){
    return mem[make_pair( index, have )];
  }

  long long ans = values[index] + f(index+1 , have^((long long)values[index]));
  if ( ans == sum ) {
    ans = f(index+1, have^(long long)(values[index]));
  }else{
    ans = max(ans , f(index+1, have^(long long)(values[index])));
  }
  return mem[make_pair( index, have )] = ans;
}

int main(){
  int casos;
  cin >> casos;
  for (int caso = 1; caso <= casos; caso++) {
    cin >> nMax;
    values.clear();
    sum=0LL;

    for (int i = 0; i < nMax; i++) {
      int tmp; cin >> tmp;
      values.push_back(tmp);
      sum += tmp;
    }
    std::sort(values.begin(),values.end());
    
    

    mem.clear();
    cout << "Case #" << (caso) << ": ";
    long long ans = f(0,0);
    if ( ans <= 0 ) {
      cout << "NO" << endl;
    }else {
      cout << ans << endl;
    }
  }
  return 0;
}


