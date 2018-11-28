#include<iostream>
#include <vector>

struct pair
{
  int x;
  int y;
};

bool intersect(int a, int b, int x, int y)
{
  //case x < a
  if(x < a)
    {
      if(y > b)
	return true;
      return false;
    }
  //case x > b
  if (x > b)
    {
      if(y < b)
	return true;
      return false;
    }
  //else : x < b
  //case x in [a, b]
  if(y < b)
    return true;
  return false;
}

bool intersect(pair a, pair b)
{
  return intersect(a.x, a.y, b.x, b.y);
}

void work(int id)
{
  std::vector<pair> vec;
  int nb;
  std::cin >> nb;
  for(int i = 0; i < nb; i++)
    {
      pair p;
      std::cin >> p.x >> p.y;
      vec.push_back(p);
    }
  //I know it's O(N^2) sry
  int nit = 0;
  for(int i = 0; i < nb; i++)
    {
      for(int j = i + 1; j < nb; j++)
	nit += (int)(intersect(vec[i], vec[j]));
    }

  std::cout << "Case #" << id << ": " << nit << std::endl;
}

int main(void)
{
  int n;

  std::cin >> n;
  for(int i = 0; i < n; i++)
    work(i + 1);
  return 0;
}
