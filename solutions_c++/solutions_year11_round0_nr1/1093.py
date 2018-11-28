#include<iostream>
#include<vector>
#include<stdio.h>
#include<stdlib.h>
#include<map>
#include<algorithm>

using namespace std;

int main() {
  int T; 
  cin >> T;
  for (int t = 0; t < T; t++) {
    int N;
    int total_time = 0;
    vector<char> colors;
    vector<int> positions;
    cin >> N;
    for (int n = 0; n < N; n++) {
      char R;
      int P;
      cin >> R >> P;
      colors.push_back(R);
      positions.push_back(P);
    }
    map<char, int> cur_pos, time_used;
    cur_pos['O'] = 1;
    cur_pos['B'] = 1;
    time_used['O'] = 0;
    time_used['B'] = 0;
    
    char prev_color = 'O';
    if (colors[0] == 'O') 
      prev_color = 'B';

    for (int n = 0; n < N; n++) {
      char current_color = colors[n];
      int move_time = abs(positions[n] - cur_pos[current_color]);
      cur_pos[current_color] = positions[n];
      if (current_color != prev_color) {
        move_time = max(0, move_time - time_used[prev_color]);
        time_used[current_color] = 0;
        prev_color = current_color;
      }  
      time_used[current_color] += move_time + 1; 
      total_time += move_time + 1;         
    }
    cout << "Case #" << t + 1 << ": " << total_time << endl;
  }
  return 0;
}
