#include <iostream>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main()
{
   int t;
   cin >> t;
   for(int i = 0; i < t; i++)
   {
      std::vector< std::string > m;
      int r, c;
      cin >> r >> c;
      for(int j = 0; j < r; j++)
      {
         string s;
         for(int k = 0; k < c; k++)
         {
            char ch;
            cin >> ch;
            s += ch;
         }
         m.push_back(s);
      }

      ///for(int j = 0; j < m.size(); j++)
        // std::cout << m[j] << std::endl;

      bool impossible = false;
      for(int j = 0; j < m.size(); j++)
      {
         for(int k = 0; k < m[j].size(); k++)
         {
            if( m[j][k] == '#')
            {
               if(j == m.size()-1 || k == m[j].size()-1)
               {
                  impossible = true;
                  break;
               }
               if(m[j+1][k] == '#' && m[j+1][k+1] == '#' && m[j][k+1] == '#')
               {
                  m[j][k] = '/';
                  m[j+1][k] = '\\';
                  m[j+1][k+1] = '/';
                  m[j][k+1] = '\\';
               }
               else
               {
                  impossible = true;
                  break;
               }
            }
         }
         if(impossible)
            break;
      }

      std::cout << "Case #" << i+1 << ": " << std::endl;
      if(impossible)
         std::cout << "Impossible" << std::endl;
      else
      {
         for(int j = 0; j < m.size(); j++)
            std::cout << m[j] << std::endl;
      }
   }
}