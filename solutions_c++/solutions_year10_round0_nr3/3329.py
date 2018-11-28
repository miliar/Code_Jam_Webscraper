#include <iostream>
#include <vector>

void work(void)
{
  int R, k, N;

  std::cin >> R >> k >> N;

  std::vector<int> vec;
  for(int i = 0; i < N; i++)
    {
      int v;
      std::cin >> v;
      vec.push_back(v);
    }

  int money = 0;
  int idx = 0;
  for(int i = 0; i < R; i++)
    {
      int space = k;
      int cnt = N;
      while(vec[idx] <= space && cnt--)
	{
	  money += vec[idx];
	  space -= vec[idx];
	  idx++;
	  idx %= N;
	}
    }
  std::cout << money;
}

int main(void)
{
  int nb;
  std::cin >> nb;

  for(int i = 1; i <= nb; i++)
    {
      std::cout << "Case #" << i << ": ";
      work();
      std::cout <<"\n";
    }
  return 0;
}
