#include <list>
#include <vector>
#include <iostream>
#include <set>
#include <map>
#include <string>
#include <math.h>

int main()
{
   size_t T = 0;
   std::cin >> T;

   for (size_t tc = 1; tc != T + 1; ++tc)
   {
      size_t C = 0;
      std::cin >> C;

      std::map<std::pair<char, char>, char> combiners;
      for (size_t l = 0; l != C; ++l)
      {
         std::string s;
         std::cin >> s;

         combiners[std::make_pair(s[0], s[1])] = s[2];
         combiners[std::make_pair(s[1], s[0])] = s[2];
      }

      size_t D = 0;
      std::cin >> D;

      std::map<char, std::set<char>> opposite;
      for (size_t l = 0; l != D; ++l)
      {
         std::string s;
         std::cin >> s;

         opposite[s[0]].insert(s[1]);
         opposite[s[1]].insert(s[0]);
      }

      size_t N = 0;
      std::cin >> N;

      std::string s;
      std::cin >> s;

      std::vector<char> elements_list;
      for (size_t l = 0; l != N; ++l)
      {
         char e = s[l];

         if (elements_list.empty())
            elements_list.push_back(e);
         else
         {
            while (!elements_list.empty() && combiners.find(std::make_pair(e, elements_list.back())) != combiners.end())
            {
               char n = combiners[std::make_pair(e, elements_list.back())];
               elements_list.pop_back();
               e = n;
            }

            bool need_to_clear = false;
            if (!opposite[e].empty())
            {
               std::set<char> const & st = opposite[e];
               for (size_t l = 0; l != elements_list.size(); ++l)
               {
                  if (st.find(elements_list[l]) != st.end())
                  {
                     need_to_clear = true;
                     break;
                  }
               }
            }

            elements_list.push_back(e);
            if (need_to_clear)
               elements_list.clear();
         }
      }

      std::cout << "Case #" << tc << ": [";
      for (size_t l = 0; l + 1 < elements_list.size(); ++l)
         std::cout << elements_list[l] << ", ";
      if (!elements_list.empty())
         std::cout << elements_list.back();
      std::cout << "]" << std::endl;
   }

   return 0;
}

