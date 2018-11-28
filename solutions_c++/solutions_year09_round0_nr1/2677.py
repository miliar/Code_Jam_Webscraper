// A.cpp : Defines the entry point for the console application.
//

#include <fstream>
#include <string>
#include <vector>

std::ifstream in("A.in");
std::ofstream out("A.out");

int L, N, T;
std::vector< std::string > words;
std::vector< std::vector< int > > pattern;

void parse(std::string str)
{
    pattern.clear();
    pattern.resize(L);
    for (int i = 0; i < L; i++)
    {
        pattern[i].resize(26);
    }
    int ind = 0;
    int l = 0;
    while (l < L)
    {
        if (str[ind] == '(')
        {
            ind++;
            while (str[ind] != ')')
            {
                pattern[l][str[ind] - 'a'] = 1;
                ind++;
            }
        }
        else
        {
            pattern[l][str[ind] - 'a'] = 1;
        }
        ind++;
        l++;
    }
}
bool check(std::string str)
{
    bool res = true;
    for (int i = 0; i < L; i++)
    {
        if (pattern[i][str[i] - 'a'] == 0)
        {
            res = false;
            break;
        }
    }
    return res;
}

int main()
{
    in >> L >> N >> T;
    words.resize(N);
    for (int i = 0; i < N; i++)
    {
        in >> words[i];
    }
    std::string temp;
    for (int i = 0; i < T; i++)
    {
        int res = 0;
        in >> temp;
        parse(temp);
        for (int j = 0; j < (int)words.size(); j++)
        {
            if (check(words[j]))
            {
                res++;
            }
        }
        out << "Case #" << i + 1 << ": " << res << std::endl;
    }
	return 0;
}

