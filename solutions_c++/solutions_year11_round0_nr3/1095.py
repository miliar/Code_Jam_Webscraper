#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <queue>

unsigned long long int
candy_splitting(std::vector<unsigned long int>& candies)
{
  unsigned long long int real_sum = 0;
  unsigned long long int xor_sum = 0;

  for (std::vector<unsigned long int>::iterator it = candies.begin(); it != candies.end(); ++it)
  {
    real_sum += *it;
    xor_sum ^= *it;
  }

  if ((xor_sum % 2) != 0)
    return -1;

  std::sort(candies.begin(), candies.end());

  for (size_t i = 1; i < candies.size(); ++i)
  {
    unsigned long long int sumA = 0;
    unsigned long long int sumB = 0;

    for (size_t j = 0; j < i; ++j)
      sumA ^= candies[j];

    for (size_t j = i; j < candies.size(); ++j)
      sumB ^= candies[j];

    if (sumA == sumB)
    {
      unsigned long long int sum = 0;

      for (size_t j = i; j < candies.size(); ++j)
        sum += candies[j];

      return sum;
    }
  }

  return -1;
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

        std::vector<unsigned long int> candies;
        for (unsigned int j = 0; j < N; ++j)
        {
          long int candy;

          ss >> candy;
          candies.push_back(candy);
        }

        long long int sum = candy_splitting(candies);

        if (sum >= 0)
          std::cout << "Case #" << (i + 1) << ": " << sum << std::endl;
        else
          std::cout << "Case #" << (i + 1) << ": " << "NO" << std::endl;
      }

      ifs.close();
    }
  }

  return 0;
}
