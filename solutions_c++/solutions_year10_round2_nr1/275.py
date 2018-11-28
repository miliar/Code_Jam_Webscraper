#include <cstdio>
#include <vector>
#include <set>
#include <algorithm>
#include <iostream>
#include <string>


int n, m;
std::set<std::string> directories;

void add (std::string text)
{
    text += '/';

    for (int i = 1; i < (int)text.length (); ++i)
        if (text[i] == '/') 
            directories.insert (text.substr (0, i));
}

int gogo ()
{
    directories.clear ();
    int ret = 0;

    std::cin >> n >> m;

    for (int i = 0; i < n; ++i)
    {
        std::string text;
        std::cin >> text;
        add (text);
    }
    ret = directories.size ();

    for (int i = 0; i < m; ++i)
    {
        std::string text;
        std::cin >> text;
        add (text);
    }

    return directories.size () - ret;
}

int main ()
{
    int tests;
    std::cin >> tests;

    for (int i = 1; i <= tests; ++i)
        printf ("Case #%d: %d\n", i, gogo ());
    return 0;
}