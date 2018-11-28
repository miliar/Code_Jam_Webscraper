#include <iostream>
#include <fstream>
#include <map>
#include <sstream>
#include <vector>

void
magicka(std::string& result,
        const std::vector<char>& input,
        std::map<std::string, char>& combined,
        std::map<std::string, char>& opposed)
{
  std::vector<char>     sequence;

  sequence.push_back(input[0]);
  for (std::vector<char>::const_iterator it = input.begin() + 1; it != input.end(); ++it)
  {
    bool        add = true;
    char        current_char = *it;
    std::string match = std::string(1, current_char);

    if (!sequence.empty())
      match = sequence.back() + match;

    if (combined.find(match) != combined.end())
    {
      sequence[sequence.size() - 1] = combined[match];
      current_char = sequence.back();
      add = false;
    }

    for (std::vector<char>::reverse_iterator jt = sequence.rbegin(); jt != sequence.rend(); ++jt)
    {
      std::string str = std::string(1, current_char) + std::string(1, *jt);

      if (opposed.find(str) != opposed.end())
      {
        sequence.clear();
        add = false;
        break;
      }
    }

    if (add)
      sequence.push_back(*it);
  }

  bool first = true;
  for (std::vector<char>::iterator it = sequence.begin(); it != sequence.end(); ++it)
  {
    if (!first)
      result += ", ";

    result += *it;
    first = false;
  }

  result = "[" + result + "]";
}

int
main(int argc, char* argv[])
{
  if (argc > 1)
  {
    std::ifstream	ifs(argv[1]);

    if (ifs.is_open())
    {
      std::string	line;
      std::stringstream	ss;
      unsigned int	ninputs = 0;

      getline(ifs, line);
      ss << line;
      ss >> ninputs;

      for (unsigned int i = 0; i < ninputs; ++i)
      {
	unsigned int C;
        unsigned int D;
        unsigned int N;

	getline(ifs, line);
	ss.clear();
	ss << line;

        std::map<std::string, char> opposed;
        std::map<std::string, char> combined;
        std::vector<char>           input;

        ss >> C;
        for (unsigned int j = 0; j < C; ++j)
        {
          std::string   cb;

          ss >> cb;
          combined[std::string(1, cb[0]) + std::string(1, cb[1])] = cb[2];
          combined[std::string(1, cb[1]) + std::string(1, cb[0])] = cb[2];
        }

        ss >> D;
        for (unsigned int j = 0; j < D; ++j)
        {
          std::string   op;

          ss >> op;
          opposed[std::string(1, op[0]) + std::string(1, op[1])] = 'X';
          opposed[std::string(1, op[1]) + std::string(1, op[0])] = 'X';
        }

        ss >> N;
        for (unsigned int j = 0; j < N; ++j)
        {
          char i;

          ss >> i;
          input.push_back(i);
        }

        std::string  result;
        magicka(result, input, combined, opposed);

	std::cout << "Case #" << (i + 1) << ": " << result << std::endl;
      }

      ifs.close();
    }
  }

  return 0;
}
