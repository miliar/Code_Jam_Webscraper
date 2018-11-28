#include <iostream>
#include <string>
#include <algorithm>

namespace sample
{
    const char *in[] =
    {
        "yeq",
        "ejp mysljylc kd kxveddknmc re jsicpdrysi",
        "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
        "de kr kd eoya kw aej tysr re ujdr lkgc jv"
    };

    const char *out[] =
    {
        "aoz",
        "our language is impossible to understand",
        "there are twenty six factorial possibilities",
        "so it is okay if you want to just give up"
    };
}

char table[sizeof(char)];

void make_table()
{
    using sample::in;
    using sample::out;
    std::fill_n(table, sizeof(char), 0);
    for (int i = 0; i != 4; ++i)
    {
        for (int j = 0; in[i][j]; ++j)
        {
            table[in[i][j]] = out[i][j];
        }
    }
    int sum = 0;
    for (int i = 'a'; i <= 'z'; ++i)
    {
        sum += table[i];
    }
    for (int i = 'a'; i <= 'z'; ++i)
    {
        if (!table[i])
        {
            table[i] = (int('a') + 'z') * 26 / 2 - sum;
        }
    }
}

void translate(std::string &s)
{
    for (int i = 0; i != s.size(); ++i)
    {
        s[i] = table[s[i]];
    }
}

int main()
{
    make_table();
    int test_count;
    std::cin >> test_count;
    std::string line;
    getline(std::cin, line);
    for (int test_case = 0; test_case != test_count; ++test_case)
    {
        getline(std::cin, line);
        translate(line);
        std::cout << "Case #" << test_case + 1 << ": " << line << std::endl;
    }
    return 0;
}
