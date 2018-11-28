#include<iostream>
#include <vector>

int how(int a, int b, int f)
{
  int cnt = 0;
  while(a < b)
    {
      a *= f;
      cnt++;
    }
  return cnt - 1;
}

int choice(int cnt)
{
  if (cnt < 1)
    return 0;
  int nb = 0;
  while(cnt > 0)
    {
      nb++;
      cnt /= 2;
    }
  return nb;
}

void work(int id)
{
  int l, p, c;
  std::cin >> l >> p >> c;
  std::cout << "Case #" << id << ": " << choice(how(l, p, c)) << std::endl;
}

int main(void)
{
  int n;

  std::cin >> n;
  for(int i = 0; i < n; i++)
    work(i + 1);
  return 0;
}
