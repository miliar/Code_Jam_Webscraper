#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>

bool
snap(int n, int k)
{
  std::vector<bool>	state(n);
  std::vector<bool>	power(n);

  for (int i = 0; i < n; ++i)
  {
    power[i] = false;
    state[i] = false;
  }
  power[0] = true;

  for (int i = 0; i < k; ++i)
  {
    for (int j = n - 1; j >= 0; --j)
      if (power[j])
	state[j] = !state[j];

    for (int j = 1; j < n; ++j)
      power[j] = power[j - 1] && state[j - 1];
  }

  return power[n - 1] && state[n - 1];
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

      for (int i = 0; i < ninputs; ++i)
      {
	unsigned int	n;
	unsigned int	k;

	getline(ifs, line);
	ss.clear();
	ss << line;
	ss >> n;
	ss >> k;

	std::cout << "Case #" << (i + 1)
		  << ": " << (snap(n, k) ? "ON" : "OFF") << std::endl;
      }

      ifs.close();
    }
  }

  return 0;
}
