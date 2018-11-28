#include <cstdlib>
#include <iostream>
#include <vector>

using namespace std;

int main()
{
  unsigned int nbCase;
  cin >> nbCase;
  for( unsigned int noCase = 1 ; noCase <= nbCase ; noCase++ )
    {
      unsigned int n, l, h;
      cin >> n >> l >> h;
      vector< unsigned int > notes(n);
      for( auto &note: notes )
        cin >> note;

      bool found = false;
      for( unsigned int t = l ; t <= h ; t++ )
        {
          bool possible = true;
          for( auto &note: notes )
            {
              if( note < t )
                if( t % note != 0 )
                  {
                    possible = false;
                    break;
                  }
              if( note > t )
                if( note % t != 0 )
                  {
                    possible = false;
                    break;
                  }
            }

          if( possible )
            {
              cout << "Case #" << noCase << ": " << t << endl;
              found = true;
              break;
            }
        }

      if( !found )
      cout << "Case #" << noCase << ": NO" << endl;
    }
  return EXIT_SUCCESS;
}
