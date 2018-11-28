#include <iostream>
#include <fstream>

#define MAX_N (1000)

typedef unsigned int uint;

void
init_mat(uint k, uint N, uint *groups, uint (*costs)[2])
{
   uint money = 0;
   uint count = 0;

   for (uint start_g = 0; start_g < N; ++start_g)
   {
      money = 0;
      count = 0;
      while (count < N
	     && (money + groups[(start_g + count) % N]) <= k)
      {
	 money += groups[(start_g + count) % N];
	 count++;
      }
      costs[start_g][0] = count;
      costs[start_g][1] = money;
   }
}

uint
ride(uint R, uint k, uint N, uint* groups)
{
   uint costs[MAX_N][2];
   uint money = 0;
   uint state = 0;

   init_mat(k, N, groups, costs);

   for (uint r = 0; r < R; ++r)
   {
      money += costs[state][1];
      state = (state + costs[state][0]) % N;
   }

   return money;
}

int
main()
{
  std::ifstream fin;
  std::ofstream fout;
  fin.open("C-small.in", std::fstream::in);
  fout.open("C-small.out", std::fstream::out);
  
  int n_test = 0;
  fin >> n_test;

  uint groups[MAX_N];

  for (int i = 0; i < n_test; ++i)
  {
     uint R, k, N;
     fin >> R >> k >> N;
     for (uint n = 0; n < N; ++n)
	fin >> groups[n];

     uint res = ride(R, k, N, groups);
     fout << "Case #" << i + 1 << ": "
	  << res  << std::endl;
     std::cout << "Case #" << i + 1 << ": "
	       << res  << std::endl;
  }

  fin.close();
  fout.close();

  return 0;
}
