#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <cassert>

using namespace std;
#define CHECK(x) assert(x)

struct TTTT {
  static void init_cnt(int cnt[]) { memset(cnt, 0, sizeof(int)*256); }
  static int check_winner(int cnt[], int status) {
    if (cnt[any] + cnt[p2] == 0) return p1;
    if (cnt[any] + cnt[p1] == 0) return p2;
    return cnt[any] != 0 ? status|256 : status;
  }
  static string winner(const vector<string> &grid) {
    int n = grid.size();
    int cnt[256], winner = 0;
    for (int j = 0; j < n; j++) {
      init_cnt(cnt);
      for (int i = 0; i < n; i++) cnt[(int)grid[j][i]]++;
      if ((winner = check_winner(cnt, winner))%256 > 0) goto out;
    }
    for (int i = 0; i < n; i++) {
      init_cnt(cnt);
      for (int j = 0; j < n; j++) cnt[(int)grid[j][i]]++;
      if ((winner = check_winner(cnt, winner))%256 > 0) goto out;
    }
    init_cnt(cnt);
    for (int k = 0; k < n; k++) cnt[(int)grid[k][k]]++;
    if ((winner = check_winner(cnt, winner))%256 > 0) goto out;
    init_cnt(cnt);
    for (int k = 0; k < n; k++) cnt[(int)grid[k][n-1-k]]++;
    if ((winner = check_winner(cnt, winner))%256 > 0) goto out;
  out:
    if (winner == p1) return string("X won");
    if (winner == p2) return string("O won");
    if (winner == 0) return string("Draw");
    return string("Game has not completed");
  }
  static const int p1 = 'X', p2 = 'O', any = '.', sp = 'T';
};

int main(int argc, char *argv[]) {
  if (argc < 2) return -1;
  ofstream ofs;
  if (argc >= 3) ofs.open(argv[2]);
  ostream &os = (argc >= 3) ? ofs : cout;

  ifstream ifs;
  ifs.open(argv[1]);
  string s;
  
  getline(ifs, s);
  int T = atoi(s.c_str());
  for (int t = 1; t <= T; t++) {
    vector<string> grid(4);
    for (int k = 0; k < 4; k++) getline(ifs, grid[k]);
    os << "Case #" << t << ": " << TTTT::winner(grid) << endl;;
    getline(ifs, s);
  }
  
  getline(ifs, s);
  getline(ifs, s);
  CHECK(ifs.eof());
  
  ifs.close();
  ofs.close();
  return 0;
}