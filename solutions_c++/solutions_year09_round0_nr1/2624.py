#include <string>
#include <vector>
#include <set>
#include <iostream>

int main(int argc, char **argv)
{
   (void)argc;
   (void)argv;
   int L, D, N;
   std::cin >> L >> D >> N;
   std::vector<std::string> vocab;
   for(int i = 0;i != D;++i)
   {
      std::string word;
      std::cin >> word;
      vocab.push_back(word);
   }
   for(int i = 0;i != N;++i)
   {
      std::string pattern;
      std::cin >> pattern;
      std::vector<std::string> matches(vocab);
      int j = 0;
      for(std::string::iterator iter = pattern.begin();iter != pattern.end();++iter, ++j)
      {
         if(j == L)
         {
            matches.clear();
            break;
         }
         std::set<char> elem;
         if(*iter != '(')
         {
            elem.insert(*iter);
         }
         else
         {
            ++iter;
            while(*iter != ')')
            {
               elem.insert(*iter);
               ++iter;
            }
         }
         std::vector<std::string>::iterator matches_iter = matches.begin();
         while(matches_iter != matches.end())
         {
            if(elem.find(matches_iter->at(j)) == elem.end())
            {
               matches_iter = matches.erase(matches_iter);
            }
            else
            {
               ++matches_iter;
            }
         }
      }
      if(j != L)
      {
         matches.clear();
      }
      std::cout << "Case #" << (i + 1) << ": " << matches.size() << std::endl;
   }
   return 0;
}
