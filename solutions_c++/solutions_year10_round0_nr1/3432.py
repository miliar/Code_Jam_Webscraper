#include <iostream>

#define ON	true
#define	OFF	false

bool state(int n, long k)
{
  /* It's a geometric series */
  /* Sum [ Un = 2^n ] = (1-2^n)/(1-2) */
  long int pow = 1;
  pow <<= n;
  int key = pow - 1;

  //Each time you make a key+1 cycle, all
  //snappers comme back to OFF state
  k = k % (key + 1);

  //Is it k == Sum [i = 0-> i = k]( Uk ) ?
  return k == key;
}

void work(int id)
{
      int N;
      int K;
      std::cin >> N >> K;
      std::cout << "Case #" << id << ": ";
      if (state(N, K) == ON)
	std::cout << "ON\n";
      else
	std::cout << "OFF\n";
}

int main(int, char *[])
{
  int nb_in;
  int id;

  std::cin >> nb_in;
  for (id = 1; id <= nb_in; id++)
    work(id);

  return 0;
}
