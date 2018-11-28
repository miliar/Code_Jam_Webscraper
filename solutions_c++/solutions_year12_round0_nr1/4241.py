#include <iostream>
#include <map>

using namespace std;

int main()
{
    int cases;
    cin >> cases;

    map<char, char> cipher;
    cipher.insert(pair<char, char>('a', 'y'));
    cipher.insert(pair<char, char>('b', 'h'));
    cipher.insert(pair<char, char>('c', 'e'));
    cipher.insert(pair<char, char>('d', 's'));
    cipher.insert(pair<char, char>('e', 'o'));
    cipher.insert(pair<char, char>('f', 'c'));
    cipher.insert(pair<char, char>('g', 'v'));
    cipher.insert(pair<char, char>('h', 'x'));
    cipher.insert(pair<char, char>('i', 'd'));
    cipher.insert(pair<char, char>('j', 'u'));
    cipher.insert(pair<char, char>('k', 'i'));
    cipher.insert(pair<char, char>('l', 'g'));
    cipher.insert(pair<char, char>('m', 'l'));
    cipher.insert(pair<char, char>('n', 'b'));
    cipher.insert(pair<char, char>('o', 'k'));
    cipher.insert(pair<char, char>('p', 'r'));
    cipher.insert(pair<char, char>('q', 'z'));
    cipher.insert(pair<char, char>('r', 't'));
    cipher.insert(pair<char, char>('s', 'n'));
    cipher.insert(pair<char, char>('t', 'w'));
    cipher.insert(pair<char, char>('u', 'j'));
    cipher.insert(pair<char, char>('v', 'p'));
    cipher.insert(pair<char, char>('w', 'f'));
    cipher.insert(pair<char, char>('x', 'm'));
    cipher.insert(pair<char, char>('y', 'a'));
    cipher.insert(pair<char, char>('z', 'q'));

    for (int i = 0; i < cases + 1; i++)
    {
        char line[120];
        cin.getline(line, 105);

        if (i == 0) continue; //flushing stream

        for (int j = 0; j < strlen(line); j++)
        {
            if (line[j] >= 'a' && line[j] <= 'z')
            {
                line[j] = cipher.find(line[j])->second;
            }
        }

        cout << "Case #" << i << ": " << line << endl;
    }

    return 0;
}
