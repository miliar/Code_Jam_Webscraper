#include <iostream>
#include <string>
#include <sstream>


const char* table = "yhesocvxduiglbkrztnwjpfmaq";


int main(int argc, char** argv)
{
  std::string s;

  std::getline(std::cin, s);

  std::istringstream ss(s);

  int T;

  ss >> T;

  for (int i = 0; i < T; i ++) {
    std::getline(std::cin, s);

    for (std::string::iterator it = s.begin(); it != s.end(); ++ it)
      if (*it != ' ')
	*it = table[*it - 'a'];

    std::cout << "Case #" << i + 1 << ": " << s << std::endl;
  }
}
