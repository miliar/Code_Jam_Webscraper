#include <stdio.h>
#include <iostream>
#include <string.h>
#include <string>
using namespace std;

const int MAXN = 128;

char letters[MAXN];
char text[MAXN];

int t;

int main()
{
    letters['a' - 'a'] = 'y';
    letters['b' - 'a'] = 'h';
    letters['c' - 'a'] = 'e';
    letters['d' - 'a'] = 's';
    letters['e' - 'a'] = 'o';
    letters['f' - 'a'] = 'c';
    letters['g' - 'a'] = 'v';
    letters['h' - 'a'] = 'x';
    letters['i' - 'a'] = 'd';
    letters['j' - 'a'] = 'u';
    letters['k' - 'a'] = 'i';
    letters['l' - 'a'] = 'g';
    letters['m' - 'a'] = 'l';
    letters['n' - 'a'] = 'b';
    letters['o' - 'a'] = 'k';
    letters['p' - 'a'] = 'r';
    letters['q' - 'a'] = 'z';
    letters['r' - 'a'] = 't';
    letters['s' - 'a'] = 'n';
    letters['t' - 'a'] = 'w';
    letters['u' - 'a'] = 'j';
    letters['v' - 'a'] = 'p';
    letters['w' - 'a'] = 'f';
    letters['x' - 'a'] = 'm';
    letters['y' - 'a'] = 'a';
    letters['z' - 'a'] = 'q';

    cin >> t;

    cin.getline(text, MAXN);
    for (int i = 1; i <= t; i++)
    {
        cin.getline(text, MAXN);

        cout << "Case #" << i << ": ";

        for (int i = 0; i < strlen(text); i++)
        {
            if (text[i] >= 'a' && text[i] <= 'z')
            {
                cout << letters[text[i] - 'a'];
            }
            else
            {
                cout << text[i];
            }
        }

        cout << endl;
    }

    return 0;
}
