#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>

long long int
bot_trust(std::vector<std::pair<char, unsigned int> >& sequence)
{
  long long int pO = 1;
  long long int tO = 0;

  long long int pB = 1;
  long long int tB = 0;

  long long int T = 0;

  for (std::vector<std::pair<char, unsigned int> >::iterator i = sequence.begin(); i != sequence.end(); ++i)
  {
    if (i->first == 'O')
    {
      tO += std::abs(pO - i->second) + 1;
      pO = i->second;

      T = std::max(T + 1, tO);
      tO = T;
    }
    else if (i-> first == 'B')
    {
      tB += std::abs(pB - i->second) + 1;
      pB = i->second;

      T = std::max(T + 1, tB);
      tB = T;
    }
  }

  return T;
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

        std::vector<std::pair<char, unsigned int> > sequence;
        for (unsigned int j = 0; j < N; ++j)
        {
          std::pair<char, unsigned int> input;

          ss >> input.first;
          ss >> input.second;

          sequence.push_back(input);
        }

	std::cout << "Case #" << (i + 1)
		  << ": " << bot_trust(sequence) << std::endl;
      }

      ifs.close();
    }
  }

  return 0;
}
