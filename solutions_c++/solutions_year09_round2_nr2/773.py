#include <iostream>
#include <algorithm>



int main()
{
  int T;
  std::cin >>T;

  for (int i = 1; i <=T; ++i)
  {
    std::string s;
    std::cin >> s;
    s = "0" +s;
    std::next_permutation(s.begin(), s.end());
    if (s[0]=='0')
      s = s.substr(1);
    std::cout << "Case #" << i << ": " << s << std::endl;
  }  
}
