#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

struct team
{
   team()
   {
      wp = 0;
      owp = 0;
      oowp = 0;
   }
   team( double wp, double owp, double oowp )
   {
      this->wp = wp;
      this->owp = owp;
      this->oowp = oowp;
   }
   double wp;
   double owp;
   double oowp;
};

int main()
{
   int t;
   cin >> t;
   for(int i = 0; i < t; i++)
   {
      int n;
      cin >> n;
      std::vector< std::string > m;
      for(int j = 0; j < n; j++)
      {
         std::string s;
         cin >> s;
         m.push_back(s);
      }

      std::vector< team > teams;
      teams.resize( n );

      for(int j = 0; j < n; j++)
      {
         double w = 0;
         double a = 0;
         for(int k = 0; k < m[j].size(); k++)
         {
            if( m[j][k] != '.' )
               a++;
            if( m[j][k] == '1' )
               w++;
         }
         teams[j].wp = w / a;
      }

      for(int j = 0; j < n; j++)//for each team
      {
         double w = 0;
         double a = 0;
         for(int k = 0; k < m[j].size(); k++)
         {
            if( m[j][k] != '.' )//found opponent
            {
               a++;
               double a2 = 0;
               double w2 = 0;
               for(int l = 0; l < m[k].size(); l++)
               {
                  if( l == j )
                     continue;
                  if( m[k][l] != '.' )
                     a2++;
                  if( m[k][l] == '1' )
                     w2++;
               }
               w += w2 / a2;
            }
         }
         teams[j].owp = w / a;
      }

      for(int j = 0; j < n; j++)//for each team
      {
         double w = 0;
         double a = 0;
         for(int k = 0; k < m[j].size(); k++)
         {
            if( m[j][k] != '.' )//found opponent
            {
               a++;
               w += teams[k].owp;
            }
         }
         teams[j].oowp = w / a;
      }  

      std::cout << "Case #" << i+1 << ": " << std::endl;
      for(int j = 0; j < teams.size(); j++)
      {
        // std::cout << teams[j].wp << " " << teams[j].owp << " " << teams[j].oowp << std::endl;
         double x = .25 * teams[j].wp + .5 * teams[j].owp + .25 * teams[j].oowp;
         std::cout << x << std::endl;
      }
   }

}