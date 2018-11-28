#include<iostream>
#include<algorithm>
#include<stdio.h>
#include<stdlib.h>

using namespace std;

struct Walkway {
  int length, w;
};

bool compare(const Walkway& w1, const Walkway& w2) {
  return w1.w < w2.w;
}

int main(void) {
  int T;
  Walkway walkway[1001];
  
  cin >> T;
  for (int i = 0; i < T; i++) {
    int S, R, N;
    double t, total_time = 0;
    long long X;
    cin >> X >> S >> R >> t >> N;
    long long total_walkway = 0;
    for (int n = 0; n < N; n++) {
      int B, E;
      cin >> B >> E >> walkway[n].w;
      walkway[n].length = E - B;
      total_walkway += E - B;
    }
    walkway[N].length = X - total_walkway;
    walkway[N].w = 0;
    sort(walkway, walkway + N + 1, compare);
    for (int n = 0; n < N + 1; n++) {
      //cout << walkway[n].length << " " << walkway[n].w << " " << t << endl;
      if (t > 0) {
        double time = walkway[n].length * 1.0 / (walkway[n].w + R);
        if (time < t) {
          t -= time;
          total_time += time;
        } else {
          total_time += t + (walkway[n].length - (walkway[n].w + R) * t) * 1.0 / (walkway[n].w + S);
          t = 0;
        }
      } else {
        total_time += walkway[n].length * 1.0 / (walkway[n].w + S); 
      }
      //cout << total_time << endl;
    }
    printf("Case #%d: %.9f\n", i + 1, total_time); 
  }
    
  return 0;
}
