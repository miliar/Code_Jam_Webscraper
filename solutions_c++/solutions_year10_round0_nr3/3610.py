#include <iostream>
#include <fstream>
#include <sstream>
#include <queue>

unsigned int
coaster(unsigned int R, unsigned int k, unsigned int N, unsigned int* groups)
{
  unsigned int	index = 0;
  unsigned int	sum = 0;
  unsigned int*	nb_groups = new unsigned int[N];
  unsigned int* nb_people = new unsigned int[N];

  for (unsigned int i = 0; i < N; ++i)
  {
      unsigned int count = 0;

      nb_groups[i] = nb_people[i] = 0;
      while (count + groups[(i + nb_groups[i]) % N] <= k && nb_groups[i] < N)
      {
	count += groups[(i + nb_groups[i]) % N];
	++nb_groups[i];
      }
      nb_people[i] = count;
  }

  for (unsigned int i = 0; i < R; ++i)
  {
    unsigned int count = 0;

    sum += nb_people[index];
    index = (index + nb_groups[index]) % N;
  }

  return sum;
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
	unsigned int	R;
	unsigned int	k;
	unsigned int	N;
	unsigned int*	groups;
	unsigned int	j = 0;

	getline(ifs, line);
	ss.clear();
	ss << line;
	ss >> R;
	ss >> k;
	ss >> N;

	groups = new unsigned int[N];

	getline(ifs, line);
	ss.clear();
	ss << line;

	while (ss >> groups[j++])
	  ;

	std::cout << "Case #" << (i + 1) << ": " << coaster(R, k, N, groups) << std::endl;
      }

      ifs.close();
    }
  }
  return 0;
}
