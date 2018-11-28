// CodeJam 2011 Candy Splitting

#include <iostream>
#include <list>

int main ()
{
  int cases;
  int n;

  static unsigned int c_s [ 1000 ];

  static unsigned int accum;
  static unsigned int real_accum;

  // Read Cases
  std::cin >> cases;

  for ( int i = 1; i <= cases; i++ )
    {
      std::cin >> n;
      // Read C's
      for ( int j = 0; j < n; j++ )
	{
	  std::cin >> c_s [ j ];
	}

      // Check if possible
      accum = c_s [ 0 ];
      for ( int j = 1; j < n; j++ )
	{
	  accum ^= c_s [ j ];
	}

      if ( accum == 0 )
	{
	  std::list<unsigned int> sorted_c_s;;
	  // Insert elements into list
	  for ( int j = 0; j < n; j++ )
	    {
	      sorted_c_s.push_back ( c_s [ j ] );
	    }

	  sorted_c_s.sort ( std::greater<unsigned int>() );

	  real_accum = accum = sorted_c_s.front();
	  std::list<unsigned int>::iterator it = sorted_c_s.begin();

	  while  ( *(++it) != sorted_c_s.back() )
	    {
	      accum ^= *it;
	      real_accum += *it;
	    }
	  std::cout << "Case #" << i << ": " << real_accum << std::endl;
	}
      else
	{
	  std::cout << "Case #" << i << ": NO\n";
	}
    }
  return 0;
}
