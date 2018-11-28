#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string.h>

using namespace std;

int main ()
{
    int T;
    bool A, B, draw;
    string ma [5];

    freopen ("A.in","r",stdin);
    freopen ("A.out","w",stdout);
    cin >> T;

    for (int tc = 0 ; tc < T ; tc ++)
    {
        A = false, B = false, draw = true;

        for (int i = 0; i < 4 ; i ++)
        {
            cin >> ma [i];

            for (int j = 0 ; j < 4 ; j ++)
            {
                if (ma [i][j] == '.')
                    draw = false;
            }
        }

        for (int i = 0 ; i < 4 ; i ++)
        {
            int cont1 = 0;
            int cont2 = 0;
            for (int j = 0 ; j < 4 ; j ++)
            {
                if (ma [i][j] == 'O' || ma [i][j] == 'T')
                {
                    cont1 ++;
                }

                if (ma [i][j] == 'X' || ma [i][j] == 'T')
                {
                    cont2 ++;
                }
            }

            if (cont1 == 4)
            {
                A = true;
                break;
            }

            if (cont2 == 4)
            {
                B = true;
                break;
            }
        }

        if (A)
        {
            cout << "Case #" << tc + 1 << ": O won" << endl;
            continue;
        }

        if (B)
        {
            cout << "Case #" << tc + 1 << ": X won" << endl;
            continue;
        }


        for (int j = 0 ; j < 4 ; j ++)
        {
            int cont1 = 0;
            int cont2 = 0;
            for (int i = 0 ; i < 4 ; i ++)
            {
                if (ma [i][j] == 'O' || ma [i][j] == 'T')
                {
                    cont1 ++;
                }

                if (ma [i][j] == 'X' || ma [i][j] == 'T')
                {
                    cont2 ++;
                }
            }

            if (cont1 == 4)
            {
                A = true;
                break;
            }

            if (cont2 == 4)
            {
                B = true;
                break;
            }
        }

        if (A)
        {
            cout << "Case #" << tc + 1 << ": O won" << endl;
            continue;
        }

        if (B)
        {
            cout << "Case #" << tc + 1 << ": X won" << endl;
            continue;
        }


        if ( (ma [0][0] == 'O' || ma [0][0] == 'T' ) && ( ma [1][1] == 'O' || ma [1][1] == 'T' ) && ( ma [2][2] == 'O'|| ma [2][2] == 'T') && ( ma [3][3] == 'O' || ma [3][3] == 'T'))
        {
            A = true;
        }

        if ( (ma [0][0] == 'X' || ma [0][0] == 'T' ) && ( ma [1][1] == 'X' || ma [1][1] == 'T' ) && ( ma [2][2] == 'X'|| ma [2][2] == 'T') && ( ma [3][3] == 'X' || ma [3][3] == 'T'))
        {
            B = true;
        }

        if ( (ma [0][3] == 'O' || ma [0][3] == 'T' ) && ( ma [1][2] == 'O' || ma [1][2] == 'T' ) && ( ma [2][1] == 'O'|| ma [2][1] == 'T') && ( ma [3][0] == 'O' || ma [3][0] == 'T'))
        {
            A = true;
        }

        if ( (ma [0][3] == 'X' || ma [0][3] == 'T' ) && ( ma [1][2] == 'X' || ma [1][2] == 'T' ) && ( ma [2][1] == 'X'|| ma [2][1] == 'T') && ( ma [3][0] == 'X' || ma [3][0] == 'T'))
        {
            B = true;
        }

        if (A)
        {
            cout << "Case #" << tc + 1 << ": O won" << endl;
            continue;
        }

        if (B)
        {
            cout << "Case #" << tc + 1 << ": X won" << endl;
            continue;
        }

        if(draw)
        {
            cout << "Case #" << tc + 1 << ": Draw" << endl;
            continue;
        }
        else
        {
            cout << "Case #" << tc + 1 << ": Game has not completed" << endl;
            continue;
        }

    }

    return 0;
}








