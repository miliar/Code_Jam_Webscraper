#include<iostream>
#include<stdlib.h>
#include<stdio.h>
#include<algorithm>

using namespace std;

int distances[1000];
int stars[1000000];

int main() {
  int T;
  cin >> T;
  for (int test = 0; test < T; test++) {
    int L, N, C;
    long long t;
    long long total_time = 0, prev_time = 0;
    int curr = 0;
    cin >> L >> t >> N >> C;
    //cout << C << endl;
    for (int c = 0; c < C; c++) { 
      cin >> distances[c];
    }
    for (int n = 0; n < N; n++) {
      total_time += distances[n % C] * 2;
      if (t < total_time) {
        if (t > prev_time) 
          stars[curr++] = (total_time - t) / 2;
        else stars[curr++] = distances[n % C];
      }
      prev_time = total_time;
    }
    //for (int i = 0; i < curr; i++)
      //cout << stars[i] << endl;
    sort(stars, stars + curr);  
    //cout << total_time << endl;
    for (int l = 0; l < L; l++) {
      int index = curr - 1 - l;
      if (index >= 0)
        total_time -= stars[curr - 1 - l];
    }
    printf("Case #%d: %lld\n", test + 1, total_time);
  }
  return 0;
}
