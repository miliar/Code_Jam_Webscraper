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
      unsigned int nbRow, nbCol;
      cin >> nbRow >> nbCol;
      vector< vector< char > > picture( nbRow );
      for( auto &r: picture )
        {
          r = vector< char >( nbCol );
          for( auto &c: r )
            cin >> c;
        }

      bool impossible = false;
      for( unsigned nr = 0 ; nr < nbRow ; nr++ )
        {
          for( unsigned nc = 0 ; nc < nbCol ; nc++ )
            {
              switch( picture[nr][nc] )
                {
                case '.':
                  break;
                case '\\':
                case '/':
                  break;
                case '#':
                  if( nr + 1 < nbRow && nc + 1 < nbCol &&
                      picture[nr][nc+1] == '#' &&
                      picture[nr+1][nc] == '#' &&
                      picture[nr+1][nc+1] == '#' )
                    {
                      picture[nr][nc] = '/';
                      picture[nr+1][nc] = '\\';
                      picture[nr][nc+1] = '\\';
                      picture[nr+1][nc+1] = '/';
                    }
                  else
                    {
                      impossible = true;
                      break;
                    }
                  break;
                default:
                  abort();
                }
            }
          if( impossible )
            break;
        }

      if( impossible )
        {
          cout << "Case #" << noCase << ": " << endl;
          cout << "Impossible" << endl;
        }
      else
        {
          cout << "Case #" << noCase << ": " << endl;
          for( auto &r: picture )
            {
              for( auto &c: r )
                cout << c;
              cout << endl;
            }
        }
    }
  return EXIT_SUCCESS;
}
