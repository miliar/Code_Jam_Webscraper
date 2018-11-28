#include <iostream>
#include <cmath>
#include <sstream>
#include <string>

using namespace std;
int main ()

{
    int num_games, game_num, n, pd, pg, d, g;
    string result;

    cin >> num_games;

    for (game_num = 1; game_num <= num_games; game_num++ )
    {
        cin >> n >> pd >> pg;

        bool d_works, g_works;
        d_works = false;
        g_works = false;

        for (d = 1; d <= n; ++d)
        {
            if ( ( d*pd ) % 100 == 0 )
            {   
                d_works = true;
                break;
            }
        }

        if (d_works) {

            // Hell, G is unbounded, so it's only an issue if pg is 0 or 100.
            if (pg == 0) {
                if (pd == 0) {
                    g_works = true;
                }
            } else if (pg == 100) {
                if (pd == 100) {
                    g_works = true;
                }
            } else {
                g_works = true;
            }
        }
            
        result += "Case #";
        stringstream cvert;
        cvert.flush();
        cvert << game_num;
        result += cvert.str();
        if (g_works) {
            result += ": Possible\n";
        } else {
            result += ": Broken\n";
        }
    }


    cout << result;
    return 0;
}


