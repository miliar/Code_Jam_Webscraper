// codejam.cpp : Defines the entry point for the console application.
//
#include <cstdio>
#include <iostream>

using namespace std;

int
main(int argc, char *argv[])
{
    unsigned T;

    std::cin >> T;

    char cipher[] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

    for (unsigned iCase = 1; iCase <= T; ++iCase)
    {
        char line[500];

        std::cin.getline(line, 499, '\n');

        if (strlen(line) == 0)
        {
            --iCase;
            continue;
        }

        std::cout << "Case #" << iCase << ": ";

        for (char *ptr = line; *ptr != '\0' && *ptr != '\n'; ++ptr)
        {
            if (*ptr == ' ')
            {
                std::cout << ' ';
            }
            else
            {
                std::cout << cipher[*ptr - 'a'];
            }
        }
        std::cout << std::endl;
    }

    return 0;
}

