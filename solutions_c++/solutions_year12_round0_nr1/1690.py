#include <string>
#include <vector>
#include <iostream>
using namespace std;

/*
ejp mysljylc kd kxveddknmc re jsicpdrysi
our language is impossible to understand

rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
there are twenty six factorial possibilities

de kr kd eoya kw aej tysr re ujdr lkgc jv
so it is okay if you want to just give up
*/

int main()
{
    string line;
    getline(cin, line);

    const size_t T = atoi(line.c_str());

    char table[256] = {0};
    table['y'] = 'a';
    table['n'] = 'b';
    table['f'] = 'c';
    table['i'] = 'd';
    table['c'] = 'e';
    table['w'] = 'f';
    table['l'] = 'g';
    table['b'] = 'h';
    table['k'] = 'i';
    table['u'] = 'j';
    table['o'] = 'k';
    table['m'] = 'l';
    table['x'] = 'm';
    table['s'] = 'n';
    table['e'] = 'o';
    table['v'] = 'p';
    table['z'] = 'q';
    table['p'] = 'r';
    table['d'] = 's';
    table['r'] = 't';
    table['j'] = 'u';
    table['g'] = 'v';
    table['t'] = 'w';
    table['h'] = 'x';
    table['a'] = 'y';
    table['q'] = 'z';
    table[' '] = ' ';

    vector<string> result;
    result.reserve(T);
    for (size_t t = 0; t < T; ++t)
    {
        string G;
        getline(cin, G);

        for (size_t i = 0; i < G.length(); ++i)
            G[i] = table[G[i]];
        result.push_back(G);
    }

    for (size_t j = 0; j < result.size(); ++j)
        cout << "Case #" << j + 1 << ": " << result[j] << endl;

    return 0;
}