#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
int main (int argc, const char **argv) {
  unsigned int lineCount;

  if (argc != 2) {
    std::cout << "syntax: googlerese file" << std::endl;
    return 1;
  }

  std::ifstream input;
  input.open(argv[1]);
  if (!input.is_open()) {
    std::cout << "file not found" << std::endl;
    return 1;
  }

  std::string line;
  getline(input, line);
  std::stringstream ss(line);

  ss >> lineCount;

  if (lineCount > 100) {
    std::cout << "lineCount exceeds 100" << std::endl;
  }

  std::ofstream output;
  output.open("result.txt");

  for (unsigned int i = 0;i<lineCount;i++) {
    int n, s, p;
    int fitting = 0;
    getline(input, line);
    ss = std::stringstream(line);
    output << "Case #" << i+1 << ": ";

    ss >> n >> s >> p;
    if (p == 0) {
      output << n << std::endl;
      continue;
    }
    else if (p == 1)
      s = 0;

    for (int j = 0;j<n;j++) {
      int t;
      ss >> t;

      if (t >= (3*p - 2))
        fitting++;
      else if (t >= (3*p - 4) && s) {
        fitting++;
        s--;
      }
    }
    output << fitting << std::endl;
  }

  input.close();
  output.close();

  return 0;
}