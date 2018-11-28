#include<iostream>
#include<string>
#include<map>
using namespace std;

int main()
{
    map<char,char> arr;
    arr['a'] = 'y';
    arr['b'] = 'h';
    arr['c'] = 'e';
    arr['d'] = 's';
    arr['e'] = 'o';
    arr['f'] = 'c';
    arr['g'] = 'v';
    arr['h'] = 'x';
    arr['i'] = 'd';
    arr['j'] = 'u';
    arr['k'] = 'i';
    arr['l'] = 'g';
    arr['m'] = 'l';
    arr['n'] = 'b';
    arr['o'] = 'k';
    arr['p'] = 'r';
    arr['q'] = 'z';
    arr['r'] = 't';
    arr['s'] = 'n';
    arr['t'] = 'w';
    arr['u'] = 'j';
    arr['v'] = 'p';
    arr['w'] = 'f';
    arr['x'] = 'm';
    arr['y'] = 'a';
    arr['z'] = 'q';
    arr[' '] = ' ';

    freopen("A-small-attempt3.in", "r", stdin);
    freopen("out.txt", "w", stdout);

    int T;
    cin >> T;

    cin.ignore();

    for(int t=0; t<T; ++t)
    {
        char ss[101];
        cin.getline(ss, 101);

        cout << "Case #" << t+1 << ": ";

        int i=0;

        while(ss[i] != '\0')
        {
            cout << arr[ss[i]];
            ++i;
        }

        cout << endl;
    }

    return 0;
}
