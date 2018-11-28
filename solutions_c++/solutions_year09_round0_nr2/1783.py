#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

int main(int argc, char* argv[]) {
  ifstream is("data.in");
  
  int N;
  is >> N;
  
  for (int n = 0; n < N; ++n) {
    int H, W;
    is >> H >> W;
    vector<vector<int>> plan(H, vector<int>(W, 0));
    vector<vector<char>> out(H, vector<char>(W, '.'));
    for (int h = 0; h < H; ++h) {
      for (int w = 0; w < W; ++w) {
        is >> plan[h][w];
        out[h][w] = '.';
      }
    }
        
    char next_sink = 'a';
    for (int h = 0; h < H; ++h) {
      for (int w = 0; w < W; ++w) {

        char sink = '?';
        int dx = 0;
        int dy = 0;
        vector<pair<int, int>> route;
        while (out[h + dy][w + dx] == '.') {
          route.push_back(make_pair(h + dy, w + dx));
          int gx = 0, gy = 0;
          int gv = 100000;
          if (h + dy - 1 >= 0 && plan[h + dy - 1][w + dx] < plan[h + dy][w + dx]) {
            if (plan[h + dy - 1][w + dx] < gv) {
              gx = 0; gy = -1;
              gv = plan[h + dy + gy][w + dx + gx];
            }
          } 
          if (w + dx - 1 >= 0 && plan[h + dy][w + dx - 1] < plan[h + dy][w + dx]) {
            if (plan[h + dy][w + dx - 1] < gv) {
              gx = -1; gy = 0;
              gv = plan[h + dy + gy][w + dx + gx];
            }
          } 
          if (w + dx + 1 < W && plan[h + dy][w + dx + 1] < plan[h + dy][w + dx]) {
            if (plan[h + dy][w + dx + 1] < gv) {
              gx = +1; gy = 0;
              gv = plan[h + dy + gy][w + dx + gx];
            }
          } 
          if (h + dy + 1 < H && plan[h + dy + 1][w + dx] < plan[h + dy][w + dx]) {
            if (plan[h + dy + 1][w + dx] < gv) {
              gx = 0; gy = +1;
              gv = plan[h + dy + gy][w + dx + gx];
            }
          }
          if (gx == 0 && gy == 0) { 
            sink = next_sink++;
            break;
          }
          dx += gx;
          dy += gy;
          if (out[h + dy][w + dx] != '.') {
            sink = out[h + dy][w + dx];
            break;
          }
        }
        for (size_t i = 0; i < route.size(); ++i)
          out[ route[i].first ][ route[i].second ] = sink;
        /*
        for (int i = 0; i < H; ++i) {
          for (int j = 0; j < W; ++j)
            cerr << out[i][j] << " ";
          cerr << endl;
        }
        cerr << "-------------------" << endl;
        */
        // sink = '@';
      }
    }
    cout << "Case #" << n + 1 << ":" << endl;
    for (int i = 0; i < H; ++i) {
      for (int j = 0; j < W; ++j)
        cout << out[i][j] << " ";
      cout << endl;
    }
  }
    
	return 0;
}

