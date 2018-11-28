#include <iostream>
#include <string>
#include <vector>

using namespace std;


int main()
{
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++)
  {
    vector< vector<char> > pic;
    int x,y;
    cin >> x >> y;
    pic.resize(x);
    
    for (int i =0 ; i < x; i++)
    {
      pic[i].resize(y);
      for (int j = 0; j < y; j++)
      {
         char c;
         cin >> ws >> c;
         pic[i][j]=(c);
      }
    }
      int z = 0;
      bool ex = true;
      for (int i = 0; i < x; i++)
      for (int j = 0; j < y; j++)
      {
        if ((i == x-1 || j == y-1) && pic[i][j] == '#')
        {
           ex = false;
           z = 1;
           i = x+1;
           j = x+1;
           break;
        }
        else
        if (ex && pic[i][j] == '#')
        {
          if (pic[i+1][j] == '#' and pic[i][j+1] == '#'  and pic[i+1][j+1] == '#')
          {
            pic[i][j] = '/';
            pic [i+1][j] = '\\';
            pic[i+1][j+1] = '/';
            pic[i][j+1] = '\\';
          }
          else {z = 2; ex = false; i = x; j = y; break;}
         
        }

      }
      if (ex)
      {
         cout << "Case #" << t << ":" << endl;
         for (int i =0 ; i < x; i++)
         {
           for (int j = 0; j < y; j++)
            cout << pic[i][j];
           cout << endl;  
         }
       
      }
      else cout << "Case #" << t << ':' << endl << "Impossible" << endl;
  }
}
