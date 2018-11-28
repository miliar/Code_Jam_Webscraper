#include <string>
#include <iostream>
#include <iomanip>

int count_subseq(const std::string &str, std::string::iterator first, std::string::iterator last)
{
   if(str.size() == 1)
   {
      return std::count(first, last, str[0]);
   }
   std::string new_str(str);
   new_str.erase(new_str.begin());
   int c = 0;
   std::string::iterator pos = std::find(first, last, str[0]);
   while(pos != last)
   {
      ++pos;
      c += count_subseq(new_str, pos, last);
      c %= 10000;
      pos = std::find(pos, last, str[0]);
   }
   return c;
}

int main(int argc, char **argv)
{
   int N;
   std::cin >> N;
   std::string line;
   std::getline(std::cin, line);
   for(int i = 0;i < N;++i)
   {
      std::getline(std::cin, line);
      std::cout << "Case #" << (i + 1) << ": " << std::setfill('0') << std::setw(4) << (count_subseq("welcome to code jam", line.begin(), line.end()) % 10000) << std::endl;
   }
}
