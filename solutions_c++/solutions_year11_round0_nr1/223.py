#include <iostream>
#include <cmath>

using namespace std;

int main()
{   
    int T;
    
    cin >> T;
    
    for(int i = 0; i < T; i ++)
    {
        int N;
        cin >> N;

        int lastO = 1;
        int lastB = 1;
        int accO = 0;
        int accB = 0;
        char lastWho = ' ';

        for(int j = 0; j < N; j ++)
        {
            char robot;
            int button;

            cin >> robot;
            while(robot != 'O' && robot != 'B')
                cin >> robot;

            if(lastWho == ' ')
                lastWho = robot;

            cin >> button;

            if(robot == 'O')
            {
                accO += abs(button - lastO) + 1;
                lastO = button;
            }
            else if(robot == 'B')
            {
                accB += abs(button - lastB) + 1;
                lastB = button;
            }

            if(lastWho == 'O' && robot == 'B'
                    && accB <= accO)
            {
                accB = accO + 1;
            }
            else if(lastWho == 'B' && robot == 'O'
                    && accO <= accB)
            {
                accO = accB + 1;
            }

            lastWho = robot;
        }

        cout << "Case #" << i + 1 << ": ";
        accO > accB ? cout << accO : cout << accB;
        cout << endl;
    }
    return 0;
}

