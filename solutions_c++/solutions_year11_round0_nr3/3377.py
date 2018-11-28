#include <iostream>
#include <vector>

using namespace std;

unsigned int f( vector< unsigned int > *candies2distribute,
                vector< unsigned int > *candies1,
                vector< unsigned int > *candies2 )
{
  if( candies2distribute->empty() )
    {
      if( candies1->empty() || candies2->empty() )
        return 0;
      unsigned int sumPatrick1 = 0;
      unsigned int sumPatrick2 = 0;
      unsigned int sumSean1 = 0;
      unsigned int sumSean2 = 0;
      for( auto &c1: *candies1 )
        {
          sumPatrick1 ^= c1;
          sumSean1 += c1;
        }
      for( auto &c2: *candies2 )
        {
          sumPatrick2 ^= c2;
          sumSean2 += c2;
        }
      if( sumPatrick1 != sumPatrick2 )
        return 0;
      else
        return max( sumSean1, sumSean2 );
    }
  else
    {
      unsigned int candy = candies2distribute->back();
      candies2distribute->pop_back();
      unsigned int r1, r2;
      candies1->push_back( candy );
      r1 = f( candies2distribute, candies1, candies2 );
      candies1->pop_back();
      candies2->push_back( candy );
      r2 = f( candies2distribute, candies1, candies2 );
      candies2->pop_back();
      candies2distribute->push_back( candy );
      return max( r1, r2 );
    }
}

int main()
{
  unsigned int nbCase;
  cin >> nbCase;
  for( unsigned int noCase = 1 ; noCase <= nbCase ; noCase++ )
    {
      unsigned int nbCandy;
      cin >> nbCandy;
      vector< unsigned int > candies;
      for( unsigned int i = 0 ; i < nbCandy ; i++ )
        {
          unsigned int c;
          cin >> c;
          candies.push_back( c );
        }

      vector< unsigned int > c1, c2;
      unsigned int r = f( &candies, &c1, &c2 );
      cout << "Case #" << noCase << ": ";
      if( r == 0 )
        cout << "NO" << endl;
      else
        cout << r << endl;
    }
  return 0;
}
