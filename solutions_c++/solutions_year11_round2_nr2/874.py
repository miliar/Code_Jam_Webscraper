#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

bool done( vector< double >& v, int d )
{
   /*
   for(int i = 0; i < v.size(); i++)
   {
      std::cout << v[i] << " ";
   }
   std::cout << std::endl;
   */
   for(int i = 1; i < v.size(); i++)
   {
      if( v[i] - v[i-1] < d )
         return false;
   }
   return true;
}

int main()
{
   int t;
   cin >> t;
   for(int i = 0; i < t; i++)
   {
      int c, d;
      cin >> c >> d;
      std::vector< double > v;
      for(int j = 0; j < c; j++)
      {
         int x, y;
         cin >> x >> y;
         for(int k = 0; k < y; k++)
         {
            v.push_back(x);
         }
      }

      sort(v.begin(), v.end());
      double time = 0;


      /*
      while(!done(v,d) )
      {
          time += .5;
         std::vector< double >::iterator itr = v.begin();
         std::vector< double >::iterator itr2 = v.end();
         --itr2;

         *itr -= .5;
         *itr2 += .5;

         ++itr;
          if(itr == itr2)
               continue;
         --itr2;
         if(itr == itr2)
               continue;

         while( !done(v,d) )
         {
            if( itr == itr2 && v.size() != 1)
            {
               if( (*(itr2+1) - *itr2) == (*itr - *(itr-1)))
                  break;
               if((*(itr2+1) - *itr2) < (*itr - *(itr-1)))
                  *itr -= .5;
               else
                  *itr += .5;
               break;
            }

            if(*itr - *(itr-1) >= d + .5)
               *itr -= .5;
            if(*(itr2+1) - *itr2 >= d + .5)
               *itr2 += .5;
            ++itr;
            if(itr == itr2)
               break;
            --itr2;
           // if(itr == itr2)
             //  break;
         }
      }
      */
      /*
      while(!done(v,d))
      {
         time += .5;
         v[0] -= .5;
         for(int j = 1; j < v.size(); j++)
         {
            if(v[j] - v[j-1] >= d + .5)
               v[j] -= .5;
         }
         std::vector< double >::reverse_iterator itr = v.rbegin();
         *itr += .5;
         itr++;
         for(itr; itr != v.rend(); itr++)
         {
            if( *(itr-1) - *itr >= d + .5)
               d += .5;
         }
      }
      */
      while(!done(v,d))
      {
         time += .5;
         v[0] -= .5;
         v[v.size()-1] += .5;
         for(int j = 1; j < v.size()-1; j++)
         {
            if( v[j+1] - v[j] > v[j] - v[j-1] )
               v[j] += .5;
            else if( v[j+1] - v[j] < v[j] - v[j-1] )
               v[j] -= .5;
         }
      }
      //std::cout << c << " " << d << std::endl;

      //if(v.size() == 1)
        // time = 0;
      std::cout << "Case #" << i+1 << ": " << time << std::endl;
   }

}