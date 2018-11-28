#include <iostream>

using namespace std;

typedef struct
{
    char color;
    int button;
} term;

int findNextRobot(const term [], int, int, char);

int main()
{
    int t, n;
    string color;
    term *sequence;
    int position;
    int orange, blue;
    int nextOrange, nextBlue;
    int counter;

    cin >> t;

    for (int i = 0; i < t; i++)
    {
        cin >> n;
        sequence = new term[n + 1];

        for (int j = 1; j <= n; j++)
        {
            cin >> color >> sequence[j].button;
            sequence[j].color = color[0];
        }

        position = orange = blue = 1;
        counter = 0;

        while (position <= n)
        {
            counter++;

            if (sequence[position].color == 'O')
            {
                if (orange < sequence[position].button)
                    orange++;
                else if (orange > sequence[position].button)
                    orange--;
                else
                    position++;

                nextBlue = findNextRobot(sequence, n, position, 'B');
                if (blue != -1)
                {
                    if (blue < nextBlue)
                        blue++;
                    else if (blue > nextBlue)
                        blue--;
                }
            }
            else
            {
                if (blue < sequence[position].button)
                    blue++;
                else if (blue > sequence[position].button)
                    blue--;
                else
                    position++;

                nextOrange = findNextRobot(sequence, n, position, 'O');
                if (orange != -1)
                {
                    if (orange < nextOrange)
                        orange++;
                    else if (orange > nextOrange)
                        orange--;
                }
            }
        }

        cout << "Case #" << i + 1 << ": " << counter << endl;

        delete [] sequence;
    }

    return 0;
}

int findNextRobot(const term sequence[], int size, int position, char color)
{
    for (int i = position; i <= size; i++)
    {
        if (sequence[i].color == color)
            return sequence[i].button;
    }

    return -1;
}
