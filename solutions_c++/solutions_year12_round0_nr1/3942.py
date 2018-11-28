#include <iostream>
#include <algorithm>
#include <stdlib.h>
#include <string>

using namespace std;

char letter(char c);
string convert(string s);

int main(int argc, char *argv[])
{
    int T;
    cin >> T;
    string s;
    getline(cin, s);
    for(int count = 1; count <= T; count++)
    {
        getline(cin, s);

        cout << "Case #" << count << ": " << convert(s) << "\n";
    }

    return 0;
}

char letter(char c)
{
    switch(c)
    {
        case 'a':
            return 'y';
            break;
        case 'b':
            return 'h';
            break;
        case 'c':
            return 'e';
            break;
        case 'd':
            return 's';
            break;
        case 'e':
            return 'o';
            break;
        case 'f':
            return 'c';
            break;
        case 'g':
            return 'v';
            break;
        case 'h':
            return 'x';
            break;
        case 'i':
            return 'd';
            break;
        case 'j':
            return 'u';
            break;
        case 'k':
            return 'i';
            break;
        case 'l':
            return 'g';
            break;
        case 'm':
            return 'l';
            break;
        case 'n':
            return 'b';
            break;
        case 'o':
            return 'k';
            break;
        case 'p':
            return 'r';
            break;
        case 'q':
            return 'z';
            break;
        case 'r':
            return 't';
            break;
        case 's':
            return 'n';
            break;
        case 't':
            return 'w';
            break;
        case 'u':
            return 'j';
            break;
        case 'v':
            return 'p';
            break;
        case 'w':
            return 'f';
            break;
        case 'x':
            return 'm';
            break;
        case 'y':
            return 'a';
            break;
        case 'z':
            return 'q';
            break;
        case ' ':
            return ' ';
            break;
    }

    return -1;
}

string convert(string s)
{
    string ans = "";
    for(int c = 0; c < (int)s.length(); c++)
    {
        ans += letter(s[c]);
    }

    return ans;
}

