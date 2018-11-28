#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
//           a    b    c    d    e    f    g    h     i   j  k    l    m    n    o    p    q    r    s    t    u    v  w    x    y    z
char t[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

char T(char a) {
  if (a < 'a' || 'z' < a)
    return ' ';
  return t[a - 'a'];
}

int main (int argc, const char **argv) {
  unsigned int lineCount;

  if (argc != 2) {
    std::cout << "syntax: googlerese file" << std::endl;
    return 1;
  }

  std::ifstream file;
  file.open(argv[1]);
  if (!file.is_open()) {
    std::cout << "file not found" << std::endl;
    return 1;
  }

  std::string line;
  getline(file, line);
  std::stringstream ss(line);

  ss >> lineCount;

  if (lineCount > 100) {
    std::cout << "lineCount exceeds 100" << std::endl;
  }

  for (unsigned int i = 0;i<lineCount;i++) {
    getline(file, line);
    std::cout << "Case #" << i+1 << ": ";
    for (unsigned int j = 0;j<line.length();j++) {
      std::cout << T(line[j]);
    }
    std::cout << std::endl;
  }
  file.close();

  return 0;
}