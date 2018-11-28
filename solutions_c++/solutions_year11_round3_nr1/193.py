#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int T;
    
    cin >> T;
    for(int caseIndex = 0; caseIndex < T; caseIndex ++)
    {
        int R, C;
        int blueCount = 0;
        bool found = false;
        bool stop = false;

        cin >> R >> C;

        char layout[60][60];

        for(int i = 0; i < R; i ++)
            for(int j = 0; j < C; j ++)
            {
                cin >> layout[i][j];

                if(layout[i][j] == '#')
                    blueCount ++;
            }

        cout << "Case #" << caseIndex + 1 << ": " << endl; 
        if(blueCount % 4 != 0)
        {
            cout << "Impossible" << endl;
        }
        else
        {
            for(int i = 0; i < R && !stop; i ++)
                for(int j = 0; j < C && !stop; j ++)
                {
                    if(layout[i][j] == '#')
                    {
                        if(j == (C - 1))
                        {
                            stop = true;
                            break;
                        }

                        if(i == (R - 1))
                        {
                            stop = true;
                            break;
                        }

                        if(layout[i][j + 1] != '#' ||
                                layout[i + 1][j] != '#' ||
                                layout[i + 1][j + 1] != '#')
                        {
                            stop = true;
                            break;
                        }

                        layout[i][j] = '/';
                        layout[i][j + 1] = '\\';
                        layout[i + 1][j] = '\\';
                        layout[i + 1][j + 1] ='/';

                        blueCount -= 4;
                    }
                }

            if(blueCount == 0)
            {
                for(int i = 0; i < R; i ++)
                {
                    for(int j = 0; j < C; j ++)
                        cout << layout[i][j];
                    cout << endl;
                }
            }
            else
                cout << "Impossible" << endl;
                
        }

    }
}
