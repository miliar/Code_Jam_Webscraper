// SAI [ 9 Aug 2009 ]
#include <stdint.h>
#include <iostream>
#include <vector>
#include <boost/regex.hpp>

#include <InputReader.h>

int main(int argc, char * argv[])
{
  if (argc < 2) return 1;

  InputReader input(argv[1]);

  for (uint32_t i = 0; i < input.patternList.size(); i += 1)
  {
    std::string * pattern = input.patternList.at(i);

    int cnt = 0;
    boost::regex ptn(pattern->c_str());
    for (uint32_t j = 0; j < input.inputList.size(); j += 1)
    {
      std::string * inp = input.inputList.at(j);
      if (boost::regex_match(inp->c_str(), ptn))
      {
        cnt += 1;
      }
    }
    std::cout << "Case #" << (i + 1) << ": " << cnt << std::endl;
  }

  return 0;
}

