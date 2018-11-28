#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int get_seconds(vector<char>&, vector<int>&);

int main(void)
{
    int T, N;
    char c;
    int b;
    int i, j;
    vector<char> colour;
    vector<int> button;

    // Get the number of cases
    cin >> T;

    for (i=1; i<=T; i++)
    {
        // Get the number of buttons
        cin >> N;

        // Get each robot colour and button
        for (j=0; j<N; j++)
        {
            cin >> c >> b;            
            colour.push_back(c);
            button.push_back(b);
        }

        cout << "Case #" << i << ": " << get_seconds(colour, button) << endl;

        colour.clear();
        button.clear();
    }

    return 0;
}

int get_seconds(vector<char> &colour, vector<int> &button)
{
    int seconds = 0;
    int i, j;
    int orangepos, bluepos;
    int pushed;

    // Get the first index of Orange
    i = 0;
    while (i<colour.size() && colour[i] != 'O')
        i++;

    // Get the first index of Blue
    j = 0;
    while (j<colour.size() && colour[j] != 'B')
        j++;

    orangepos = bluepos = 1;
    while (i < colour.size() && j < colour.size())
    {
        pushed = 0;
        if (orangepos < button[i])
        {
            orangepos++;
        }
        else if (orangepos > button[i])
        {
            orangepos--;
        }
        else if (i < j)
        {
            pushed = 1;
            i++;
            while (i<colour.size() && colour[i] != 'O')
                i++;
        }
        if (bluepos < button[j])
        {
            bluepos++;
        }
        else if (bluepos > button[j])
        {
            bluepos--;
        }
        // Only if O hasn't push the button already
        else if (j < i && !pushed)
        {
            j++;
            while (j<colour.size() && colour[j] != 'B')
                j++;
        }
        seconds++;
    }
    while (i < colour.size())
    {
        if (orangepos < button[i])
        {
            orangepos++;
        }
        else if (orangepos > button[i])
        {
            orangepos--;
        }
        else
        {
            i++;
        }

        seconds++;
    }
    while (j < colour.size())
    {
        if (bluepos < button[j])
        {
            bluepos++;
        }
        else if (bluepos > button[j])
        {
            bluepos--;
        }
        else
        {
            j++;
        }

        seconds++;
    }

    return seconds;
}
