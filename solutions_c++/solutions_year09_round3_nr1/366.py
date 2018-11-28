#include <iostream>
#include <map>

std::map<char, int> map;
std::map<char, int>::iterator it;
std::string s;

void Solve()
{
  int cur_dig=2;
  bool one_taken = false;
  map.clear();
  for (int i = 0; i < s.length(); ++i)
  {
    char ch = s[i];
    it = map.find(ch);
    if (it ==map.end())
    {
      int digit = cur_dig;
      if (i ==0)
      {
	digit = 1;
	one_taken = true;
      }else
      if (one_taken)
      {
	digit = 0;
	one_taken = false;
      }
      else
	digit = cur_dig++;
      map[ch] = digit;
    }
  }
  long base = cur_dig;
  long int res = 0; 
  for (int i = 0; i < s.length(); i++)
  {
    //    std::cout << map[s[i]] << std::endl;
    res = res*base + map[s[i]];
  }
  std::cout << res << std::endl;
}

      

int main()
{
  int N;
  std::cin >>N;
  for (int i = 1; i <=N; ++i)
  {
    std::cin >>s;
    std::cout << "Case #" << i << ": ";
    Solve();
  }
}
