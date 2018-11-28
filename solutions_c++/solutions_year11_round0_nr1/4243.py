#include <iostream>

using namespace std;

int getNextBlue(int* buttons, char* robots, int pos, int length)
{
    for (int i = pos; i < length; ++i)
    {
        if (robots[i] == 'B')
            return buttons[i];
    }
    return pos;
}

int getNextOrange(int* buttons, char* robots, int pos, int length)
{
    for (int i = pos; i < length; ++i)
    {
        if (robots[i] == 'O')
            return buttons[i];
    }
    return pos;
}

int main(int argc, char* argv[])
{
    int t;
    cin >> t;
    
    
    for (int i = 0; i < t; ++i)
    {
        int robot0pos = 1;
        int robot1pos = 1;        
        int seconds = 0;

        int n;
        cin >> n;
        int buttons[n];
        char robots[n];
        for (int j = 0; j < n; ++j)
        {
            cin >> robots[j];
            cin >> buttons[j];
        }
        
        cout << "Case #" << i + 1 << ": ";
        
        int j = 0;
        while (j < n)
        {
            bool orange = robots[j] == 'O';
            if (orange)
            {
                if (getNextBlue(buttons, robots, j, n) > robot1pos)
                    ++robot1pos;
                else if (getNextBlue(buttons, robots, j, n) < robot1pos)
                    --robot1pos;
                if (buttons[j] == robot0pos)
                    ++j;
                else if (buttons[j] > robot0pos)
                    ++robot0pos;
                else
                    --robot0pos;
            }
            else
            {
                if (getNextOrange(buttons, robots, j, n) > robot0pos)
                    ++robot0pos;
                else if (getNextOrange(buttons, robots, j, n) < robot0pos)
                    --robot0pos;
                if (buttons[j] == robot1pos)
                    ++j;
                else if (buttons[j] > robot1pos)
                    ++robot1pos;
                else
                    --robot1pos;
            }
            ++seconds;
        }
        
        cout << seconds << endl;
    }
    return EXIT_SUCCESS;
}
