#include <fstream>
#include <string>
#include <sstream>
#include <iostream>

using namespace std;

// not sure whats the trick in this problem.
// just deduced the mappings from the examples and hardcoded!
char a[26] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

int main(int argc, char* argv[]) {
  if (argc != 3) {
    std::cout << "Usage: <input_file> <output_file>\n";
    return -1;
  }
  ifstream ifs(argv[1]);
  ofstream ofs(argv[2]);
  string line;
  stringstream ss;
  int T = 0;

  // get inputs
  getline(ifs, line);
  ss << line;
  ss >> T;

  // run test cases
  for (int t=1;t<=T;t++) {
    getline(ifs, line);
    ofs << "Case #" << t << ": ";
    cout << "Case #" << t << ": ";
    for (int i=0;i<line.length();i++) {
      int ch = line[i] - 'a';
      if (ch >= 0 && ch < 26) {
        ofs << a[line[i] - 'a'];
        cout << a[line[i] - 'a'];
      } else {
        ofs << line[i];
        cout << line[i];
      }
    }
    ofs << std::endl;
    cout << std::endl;
  }

  ifs.close();
  ofs.close();
  return 0;
}
