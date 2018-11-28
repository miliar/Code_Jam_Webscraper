//
// main.cpp for GCJ Qualification Round
// Written by Clement Cousin <140.opera@gmail.com>
// 05/08/2010
//

#include <iostream>
#include <fstream>
#include <deque>

struct  Group
{
  Group(int n) : size(n) {}
  int   size;
};

int run_test(std::deque<Group>& queue, const int rides, const int maxP)
{
  int total = 0;
  for (int i = 0; i < rides; ++i)
  {
    int nbP = 0;
    int queue_size = queue.size();
    while (queue_size > 0 && (nbP <= maxP - queue.front().size))
    {
      nbP += queue.front().size;
      queue.push_back(queue.front());
      queue.pop_front();
      --queue_size;
    }
    total += nbP;
  }
  return total;
}

int main(int ac, char** av)
{
  if (ac > 1)
  {
    std::ifstream ifs;
    for (int i = 1; i < ac; ++i)
    {
      ifs.open(av[i]);
      int nbTests = 0;
      ifs >> nbTests;
      for (int j = 0; j < nbTests; ++j)
      {
        int rides = 0;
        ifs >> rides;
        int maxP = 0;
        ifs >> maxP;
        int nb = 0;
        ifs >> nb;
        std::deque<Group> queue;
        for (int n = 0; n < nb; ++n)
        {
          int s = 0;
          ifs >> s;
          queue.push_back(Group(s));
        }
        int res = run_test(queue, rides, maxP);
        std::cout << "Case #" << j + 1 << ": " << res <<std::endl;
      }
      ifs.close();
      ifs.clear();
    }
  }
  return 0;
}
