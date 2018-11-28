#include <iostream>
#include <vector>
#include <string>

using namespace std;

void print_ret(int i, int ret) {
  cout << "Case #" << i << ": " << ret << endl;
}

int abs(int i) {
  if (i < 0) return -i;
  else return i;
}

int main(void) { 
  int t, n;
  cin >> t;

  for (int i=0; i<t; i++) {
    cin >> n;
    vector<int> pos;
    vector<int> ch;
    for (int j=0; j<n; j++) {
       int k;
       char c;
       cin >> c >> k;
       pos.push_back(k);
       if (c == 'O') {
	       ch.push_back(0);
       } else {
	       ch.push_back(1);
       }
    }

    // o = 0, b = 1
    int cur_pos[2] = {1, 1};
    int ret = 0;
    int cur_buf[2] = {0, 0};

    for (int j=0; j<n; j++) {
      int cur_ch = ch[j];

      int strand_rel = cur_pos[cur_ch] - pos[j];
      int strand = abs(strand_rel) - cur_buf[cur_ch];

      if (strand < 0) strand = 0;
      ret += strand+1;
      cur_buf[(cur_ch+1)%2] += strand+1;

      cur_pos[cur_ch] = pos[j];
      cur_buf[cur_ch] = 0;

//      cout << "ret: " << ret << ", " << cur_buf[0] << ", " << cur_buf[1] << endl;
    }

    print_ret(i+1, ret);
  }
}


