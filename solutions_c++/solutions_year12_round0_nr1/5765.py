#include <iostream>
#include <string>

using namespace std;

char replaceSymbol(char &c)
{
    switch(c)
    {
        case 'a': return 'y';
        case 'b': return 'h';
        case 'c': return 'e';
        case 'd': return 's';
        case 'e': return 'o';
        case 'f': return 'c';
        case 'g': return 'v';
        case 'h': return 'x';
        case 'i': return 'd';
        case 'j': return 'u';
        case 'k': return 'i';
        case 'l': return 'g';
        case 'm': return 'l';
        case 'n': return 'b';
        case 'o': return 'k';
        case 'p': return 'r';
        case 'q': return 'z';
        case 'r': return 't';
        case 's': return 'n';
        case 't': return 'w';
        case 'u': return 'j';
        case 'v': return 'p';
        case 'w': return 'f';
        case 'x': return 'm';
        case 'y': return 'a';
        case 'z': return 'q';
        case ' ': return ' ';
    }
}

int main (int argc, char *argv[])
{
    int n;
    cin >> n;
    
    int k = 0;
    string s[30];
    getline(cin, s[0]);
    k=0;
    while(k < 30)
    {
        getline(cin, s[k]);
        k++;
    }

    for(k = 0; k < n; k++)
    {
        for(int j = 0; j < s[k].length(); j++)
        {
            s[k][j] = replaceSymbol(s[k][j]);
        }
    }
    
    for(k = 0; k < n; k++)
    {
        cout << "Case #" << k+1 << ": " << s[k] << endl;
    }
    return 0;
}
