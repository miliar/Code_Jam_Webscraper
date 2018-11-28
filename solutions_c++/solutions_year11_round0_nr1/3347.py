#include <iostream>
#include <list>

const int INVALID_POS = -1;

std::list<std::pair<char,int>> g_sequence;

int nextPos(char color);

int main()
{
    int T;
    std::cin >> T;

    for(int t = 1; t <= T; t++)
    {
        g_sequence.clear();

        int N;
        std::cin >> N;

        for(int n = 0; n < N; n++)
        {
            char botColor;
            int buttonPos;

            std::cin >> botColor;
            std::cin >> buttonPos;

            g_sequence.push_back(std::pair<char,int>(botColor, buttonPos));
        }

        int seconds = 0;
        int bluePos = 1, orangePos = 1;

        while(g_sequence.size())
        {
            bool bPush = false;

            int blueDest = nextPos('B');
            int orangeDest = nextPos('O');

            if(bluePos < blueDest)
            {
                bluePos++;
            }
            else if(bluePos > blueDest)
            {
                bluePos--;
            }
            else
            {
                if(g_sequence.front().first == 'B')
                    bPush = true;
            }

            if(orangePos < orangeDest)
            {
                orangePos++;
            }
            else if(orangePos > orangeDest)
            {
                orangePos--;
            }
            else
            {
                if(g_sequence.front().first == 'O')
                    bPush = true;
            }

            if(bPush)
                g_sequence.pop_front();

            seconds++;
        }

        std::cout << "Case #" << t << ": " << seconds << std::endl;
    }

    return 0;
}

int nextPos(char color)
{
    for(std::list<std::pair<char,int>>::const_iterator i = g_sequence.begin(); i != g_sequence.end(); i++)
    {
        if(i->first == color)
            return i->second;
    }

    return INVALID_POS;
}