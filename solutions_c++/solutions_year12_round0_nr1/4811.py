#include <iostream>
#include <string>

using namespace std;

int main ()
{
    char line[101];
    char map[] = {
           'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b',
           'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'
           };
    int c = -1;
    int t = 0;
    while (cin.getline(line, 101))
    {
          if (c < 0)
          {
             t = atoi(line);
             ++c;
             continue;
          }
          if ( c >= t )
          {
             break;
          }
          ++c;
          cout << "Case #" << c << ": ";
          for (int i=0; i < 100; ++i)
          {
              if (line[i] == '\0')
              {
                 break;
              }
              if (line[i] == ' ')
              {
                 cout << line[i];
              
              }
              else
              {
                  cout << map[line[i] - 'a'];
              }
          }
          cout << endl;
    }
    return 0;
}
