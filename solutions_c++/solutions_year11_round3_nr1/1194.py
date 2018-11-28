#include <iostream>
#include <fstream>
#include <vector>

//std::cout << << std::endl;
//std::vector<string>::iterator it, ite;
//it = v.begin();
//ite = v.end();
//for (; it != ite)
//{
//
//}

bool has_sharp(char **tab)
{
    for (int i = 0; i < 51; ++i)
    {
        for (int j = 0; j < 51; ++j)
        {
            if (tab[i][j] == '#')
                return true;
        }
    }
    return false;
}

std::string make_res(char **tab)
{
    std::string res;

    res = "";
    for (int i = 0; i < 51; ++i)
    {
        if (!tab[i][0])
            break;
        res += tab[i];

    }
    return res;
}

std::string process_line(std::ifstream &ifs)
{
    int r;
    int c;
    char tab[51][51];
    int offset;
    char *ptr;

    ifs >> r;
    std::cout << r << std::endl;
    ifs >> c;
    std::cout << c << std::endl;
    memset(tab, 0, 51);
    ifs.getline(tab[0], 51);
    for (int i = 0; i < r; ++i)
    {
        memset(tab[i], 0, 51);
        ifs.getline(tab[i], 51);
        //std::cout << "line:" << tab[i] << std::endl;
    }
    for (int i = 0; i < r; ++i)
    {
       offset = 0;
       ptr = tab[i];
       while ((ptr = ::strstr(ptr, "##")))
       {
           //std::cout << "found ## in " << ptr << std::endl;
           offset = ptr - tab[i];
           if (tab[i + 1])
           {
               if (tab[i + 1][offset] == '#' && tab[i + 1][offset + 1] == '#')
               {
                ptr[0] = '/';
                ptr[1] = '\\';
                tab[i + 1][offset] = '\\';
                tab[i + 1][offset + 1] = '/';
               }
           }
           ptr += 2;
       }
    }
    for (int i = 0; i < r; ++i)
    {
        for (int j = 0; j < c; ++j)
        {
            if (tab[i][j] == '#')
                return "\nImpossible";
        }
    }
    std::string res;

    res = "\n";
    for (int i = 0; i < r; ++i)
    {
        res += tab[i];
        if (i != (r - 1))
            res += "\n";
    }
    return res;
}

int main()
{
    std::ifstream ifs("../A-large.in");
    std::ofstream ofs("output.txt");
    std::string res;

    if (ifs.is_open() && ofs.is_open())
    {
        int nb_lines;

        ifs >> nb_lines;
        for (int i = 0; i < nb_lines; ++i)
        {
            res = process_line(ifs);
            ofs << "Case #" << i+1 << ": " << res.c_str() << std::endl;
            std::cout << "Case #" << i+1 << ": " << res.c_str() << std::endl;
        }
    }
    else
    {
        std::cerr << "Couldn't open input.txt file" << std::endl;
    }
    ifs.close();
    ofs.close();
    return 0;
}
