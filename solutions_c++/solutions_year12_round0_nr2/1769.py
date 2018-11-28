#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <vector>
using namespace std;

int main(){
  int T;
  cin >> T;
  for (int c = 1; c<=T; c++){
    int N,P,T;
    cin >> N >> P >> T;
    int v[N];
    for (int i=0; i<N; i++){
      cin >> v[i]; 
    }
    int a=0,b=0;
    int p = T + max((T-1)*2, 0);
    int q = T + max((T-2)*2, 0);
    for (int i=0; i<N; i++){
      if (v[i] >= p) a++;
      else if (v[i] >= q) b++;
    }
    printf ("Case #%d: %d\n",c, a+(min(b,P)));
  }
}
