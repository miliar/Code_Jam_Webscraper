#include <iostream>
#include <cstring>
#include <cstdlib>
using namespace std;

int main()
{
    char Letters[256], Line[1000000];
    int N;
    
    Letters[(int)'a'] = 'y';
    Letters[(int)'b'] = 'h';
    Letters[(int)'c'] = 'e';
    Letters[(int)'d'] = 's';
    Letters[(int)'e'] = 'o';
    Letters[(int)'f'] = 'c';
    Letters[(int)'g'] = 'v';
    Letters[(int)'h'] = 'x';
    Letters[(int)'i'] = 'd';
    Letters[(int)'j'] = 'u';
    Letters[(int)'k'] = 'i';
    Letters[(int)'l'] = 'g';
    Letters[(int)'m'] = 'l';
    Letters[(int)'n'] = 'b';
    Letters[(int)'o'] = 'k';
    Letters[(int)'p'] = 'r';
    Letters[(int)'q'] = 'z';
    Letters[(int)'r'] = 't';
    Letters[(int)'s'] = 'n';
    Letters[(int)'t'] = 'w';
    Letters[(int)'u'] = 'j';
    Letters[(int)'v'] = 'p';
    Letters[(int)'w'] = 'f';
    Letters[(int)'x'] = 'm';
    Letters[(int)'y'] = 'a';
    Letters[(int)'z'] = 'q';

    cin >> N;
    cin.getline(Line, 1000000);
    for (int j = 1; j <= N; j++)
    {
        cin.getline(Line, 1000000);
        cout << "Case #" << j << ": ";
        
        for (int i = 0; i < strlen(Line); i++)
        {
            if (Line[i] != ' ')
                cout << Letters[(int)Line[i]];
            else
                cout << " ";
        }
        cout << endl;
    }
    
    return EXIT_SUCCESS;
}
