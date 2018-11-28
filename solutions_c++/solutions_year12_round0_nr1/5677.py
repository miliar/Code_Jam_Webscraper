#include <algorithm>
#include <iostream>
#include <string>

using namespace std;

const char map[26] = {
'y',
'h',
'e',
's',
'o',
'c',
'v',
'x',
'd',
'u',
'i',
'g',
'l',
'b',
'k',
'r',
'z',
't',
'n',
'w',
'j',
'p',
'f',
'm',
'a',
'q'
};

char convert(const char input)
{
    if (isalpha(input))
    {
        if (islower(input))
        {
            return map[input - 'a'];
        }
        else
        {
            return toupper(map[tolower(input) - 'a']);
        }
    }
    return input;
}

int main()
{
    string s;
    int numCase = 1;

    // Ignore the number of cases
    cin.ignore(100, '\n');

    while (getline(cin, s))
    {
        transform(s.begin(), s.end(), s.begin(), convert);
        cout << "Case #" << numCase << ": " << s << '\n';
        ++numCase;
    }
}
