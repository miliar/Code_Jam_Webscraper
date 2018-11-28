#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <cstring>

using namespace std;

int main(int argc, char* argv[]) {
  if (argc != 3) {
    std::cout << "Usage: <input_file> <output_file>\n";
    return -1;
  }
  ifstream ifs(argv[1]);
  ofstream ofs(argv[2]);
  string line;
  stringstream ss;
  int C = 0;

  // get inputs
  getline(ifs, line);
  ss << line;
  ss >> C;
  ss.clear();

  // run test cases
  for (int c=1;c<=C;c++) {
    getline(ifs, line);
    ss << line;
    int N = 0;
    ss >> N;
    int S = 0;
    ss >> S;
    int p = 0;
    ss >> p;
    vector<int> G;
    int t = 0;
    for (int n=0;n<N;n++) {
      ss >> t;
      G.push_back(t);
    }
    ss.clear();
    int max_count = 0;
    int smax_count = 0;
    for (int n=0;n<N;n++) {
      t = G[n];
      if ((p + p + p) <= t) {
        max_count++;
        continue;
      } 
      if ((p-1) >= 0) {
        if ((p + p + (p-1)) <= t) {
          max_count++;
          continue;
        } else if ((p + (p-1) + (p-1)) <= t) {
          max_count++;
          continue;
        }
      }
      if ((p-2) >= 0) {
        if ((p + p + (p-2)) <= t) {
          smax_count++;
          continue;
        } else if ((p + (p-1) + (p-2)) <= t) {
          smax_count++;
          continue;
        } else if ((p + (p-2) + (p-2)) <= t) {
          smax_count++;
          continue;
        }
      }
    }
    G.clear();
    int solution = max_count + min(smax_count, S);
    ofs << "Case #" << c << ": ";
    cout << "Case #" << c << ": ";
    ofs << solution;
    cout << solution;
    ofs << std::endl;
    cout << std::endl;
  }

  ifs.close();
  ofs.close();
  return 0;
}
