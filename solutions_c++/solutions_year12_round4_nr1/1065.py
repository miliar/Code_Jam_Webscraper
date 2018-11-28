#include <cstdio>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;
typedef long long i64;

#define FOREACH(type, collection, arg) for(vector<type>::iterator arg = collection.begin(); arg != collection.end(); arg++)
#define FOREACH_R(type, collection, arg) for(vector<type>::iterator arg = collection.rbegin(); arg != collection.rend(); arg++)

int main(int argc, char *argv[]){
  int T;
  cin >> T;

  for(int t=1;t<=T;t++) {
    printf("Case #%d: ", t);
    i64 N;
    cin >> N;
    vector<i64> d(N), l(N), h(N, -1);
    for(i64 n=0;n<N;n++)
      cin >> d[n] >> l[n];
    i64 D;
    cin >> D;

    h[0] = d[0];
    for(i64 n=0;n<N;n++) {
      for(i64 m=n+1;m<N;m++) {
	if(d[n] + h[n] >= d[m]) {
	  h[m] = max(h[m], min(d[m] - d[n], l[m]));
	}
      }
    }

    bool f = false;
    for(i64 n=0;n<N;n++) {
      if(h[n] >= 0 && d[n] + h[n] >= D) {
	f = true;
	break;
      }
    }
    cout << (f ? "YES" : "NO") << endl;
  }

  return 0;
}
