#include <iostream>
#include <fstream>
#include <array>
#include <string>

int main()
{
    std::ifstream in("A-large.in");
    std::ofstream out("test.out");
    int t;
    in >> t;
    std::array<std::array<char, 4>, 4> arr;
    std::string s;
    for (int q = 1; q <= t; ++q)
    {
        out << "Case #" << q;
        int point_count = 0;
        bool t_symbol = false;
        int x_symbol = 0;
        int o_symbol = 0;
        bool f = false;
        bool f_x = false;
        bool f_o = false;
        for (int i = 0; i < 4; ++i)
        {
            in >> s;
            t_symbol = false;
            x_symbol = 0;
            o_symbol = 0;
            for (int j = 0; j < 4; ++j)
            {
                arr[i][j] = s[j];
                if (s[j] == 'X')
                {
                    ++x_symbol;
                }
                else
                {
                    if (s[j] == 'T')
                    {
                        t_symbol = true;
                    }
                    else
                    {
                        if (s[j] == 'O')
                        {
                            ++o_symbol;
                        }
                        else
                        {
                            ++point_count;
                        }
                    }
                }
            }
            if (o_symbol == 4 || (t_symbol && o_symbol == 3))
            {
                f_o = true;
            }
            if (x_symbol == 4 || (t_symbol && x_symbol == 3))
            {
                f_x = true;
            }
        }
        if (f_o)
        {
            out << ": O won" << std::endl;
            continue;
        }
        if (f_x)
        {
            out << ": X won" << std::endl;
            continue;
        }
        //columns
        for (int j = 0; j < 4; ++j)
        {
            t_symbol = false;
            x_symbol = 0;
            o_symbol = 0;
            for (int i = 0; i < 4; ++i)
            {
                if (arr[i][j] == 'X')
                {
                    ++x_symbol;
                }
                else
                {
                    if (arr[i][j] == 'T')
                    {
                        t_symbol = true;
                    }
                    else
                    {
                        if (arr[i][j] == 'O')
                        {
                            ++o_symbol;
                        }
                    }
                }
            }
            if (o_symbol == 4 || (t_symbol && o_symbol == 3))
            {
                out << ": O won" << std::endl;
                f = true;
                break;
            }
            if (x_symbol == 4 || (t_symbol && x_symbol == 3))
            {
                out << ": X won" << std::endl;
                f = true;
                break;
            }
        }
        if (f)
        {
            continue;
        }
        //diag1
        t_symbol = false;
        x_symbol = 0;
        o_symbol = 0;
        for (int i = 0; i < 4; ++i)
        {
            if (arr[i][i] == 'X')
            {
                ++x_symbol;
            }
            else
            {
                if (arr[i][i] == 'T')
                {
                    t_symbol = true;
                }
                else
                {
                    if (arr[i][i] == 'O')
                    {
                        ++o_symbol;
                    }
                }
            }
        }
        if (o_symbol == 4 || (t_symbol && o_symbol == 3))
        {
            out << ": O won" << std::endl;
            continue;
        }
        if (x_symbol == 4 || (t_symbol && x_symbol == 3))
        {
            out << ": X won" << std::endl;
            continue;
        }
        //diag2
        t_symbol = false;
        x_symbol = 0;
        o_symbol = 0;
        for (int i = 0; i < 4; ++i)
        {
            if (arr[i][3 - i] == 'X')
            {
                ++x_symbol;
            }
            else
            {
                if (arr[i][3 - i] == 'T')
                {
                    t_symbol = true;
                }
                else
                {
                    if (arr[i][3 - i] == 'O')
                    {
                        ++o_symbol;
                    }
                }
            }
        }
        if (o_symbol == 4 || (t_symbol && o_symbol == 3))
        {
            out << ": O won" << std::endl;
            continue;
        }
        if (x_symbol == 4 || (t_symbol && x_symbol == 3))
        {
            out << ": X won" << std::endl;
            continue;
        }
        //end
        if (point_count == 0)
        {
            out << ": Draw" << std::endl;
        }
        else
        {
            out << ": Game has not completed" << std::endl;
        }
    }
    return 0;
}

