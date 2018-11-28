#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <iomanip>

char sub[256];

void map(const char* code, const char* key)
{
    for (int n = 0; code[n] != '\0'; n++)
    {
        sub[code[n]] = key[n];
    }
}

int main()
{
    memset(sub, '?', 256); 

    map("yeq ", "aoz ");
    map("ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand");
    map("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities");
    map("de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up");

    map("z", "q");

    char line[256];
    std::cin.getline(line, 255);

    int numCases = atoi(line);

    for (int i = 0; i < numCases; i++)
    {
        std::cout << "Case #" << (i + 1) << ": ";

        std::cin.getline(line, 255);

        for (int n = 0; line[n] != '\0'; n++)
        {
            std::cout << sub[line[n]];
        }

        std::cout << std::endl;
    }
}
