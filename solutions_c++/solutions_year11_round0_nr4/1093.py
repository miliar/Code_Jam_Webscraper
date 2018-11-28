#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <queue>

long long int
goro(std::vector<unsigned long int>& values)
{
  long long int diff = 0;

  for (size_t i = 0; i < values.size(); ++i)
    if (values[i] != i + 1)
      ++diff;

  return diff;
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
	unsigned int	N;

	getline(ifs, line);
	ss.clear();
	ss << line;

        ss >> N;

	getline(ifs, line);
	ss.clear();
	ss << line;

        std::vector<unsigned long int> values;
        for (unsigned int j = 0; j < N; ++j)
        {
          long int value;

          ss >> value;
          values.push_back(value);
        }

        std::cout << "Case #" << (i + 1) << ": " << goro(values) << ".000000" << std::endl;
      }

      ifs.close();
    }
  }

  return 0;
}
