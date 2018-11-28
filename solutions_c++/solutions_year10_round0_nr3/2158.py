#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <string>
#include <map>
using namespace std;
int main()
{
    int T;
    cin >> T;
    for(int t=0;t<T;t++)
    {
        int R,K, N;
        cin >> R >> K >> N;
        int TOT = 0;
        vector<int> groups;
        list<int> grouplist;
        for(int i = 0;i<N;i++)
        {
          int g;
          cin >> g;
          TOT += g;

          grouplist.push_back( g );
          groups.push_back( g );
        }
        long long result = 0;
        if (K>=TOT)
        {
          result = TOT;
          result *= R;
        } 
        else
        {
          int startpos = 0;
          for(int r=0;r<R;r++)
          {
            int k=K;
            int endpos = startpos;
            // Add first group
            result += groups[ startpos ];
            k -= groups[ startpos ];
            startpos++;

            startpos %= N;
            while( (startpos != endpos) 
                && ( k >= groups[ startpos ] )
                )
            {
              result += groups[ startpos ];
              k -= groups[ startpos ];
              ++startpos;
              startpos %= N;
            }


          }
        }

        cout << "Case #" << t+1 << ": " << result << endl;
    }
}
