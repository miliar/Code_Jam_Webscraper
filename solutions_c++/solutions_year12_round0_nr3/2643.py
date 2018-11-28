#include <iostream>

using namespace std;

const int MAX = 2000000;

bool vis[MAX];

int a, b;

int cycle(int v, int mul){
  int cnt = 0;
  while(!vis[v-1]){
    vis[v-1] = true;
    if(a <= v && v <= b) ++cnt;
    v = v % 10 * mul + v / 10;
    while(v >= MAX) v = v % 10 * mul + v / 10;
  }
  return (cnt-1)*cnt/2;
}

int main(void){
  int t;
  cin >> t;
  for(int k = 0; k < t; ++k){
    cin >> a >> b;
    fill_n(vis, MAX, false);

    int mul = 1; int tmp = a;
    while(tmp >= 10) tmp /= 10, mul *= 10;

    int cnt = 0;
    for(int i = a; i <= b; ++i){
      if(!vis[i-1])
        cnt += cycle(i, mul);
    }
    cout << "Case #" << k+1 << ": " << cnt << endl;
  }
  return 0;
}
