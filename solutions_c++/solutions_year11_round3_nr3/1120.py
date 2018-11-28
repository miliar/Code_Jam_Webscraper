#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>

//std::cout << << std::endl;
//std::vector<string>::iterator it, ite;
//it = v.begin();
//ite = v.end();
//for (; it != ite)
//{
//
//}


std::string process_line(std::ifstream &ifs)
{
    int nb_player;
    int min;
    int max;
    std::vector<int> notes;
    int tmp;
    std::vector<int>::iterator it, ite;
    int okay;

    ifs >> nb_player;
    ifs >> min;
    ifs >> max;
    for (int i = 0; i < nb_player; ++i)
    {
        ifs >> tmp;
        notes.push_back(tmp);
    }

    for (int i = min; i <= max; ++i)
    {
        it = notes.begin();
        ite = notes.end();
        okay = 0;
        for (; it != ite; ++it)
        {
            if (i > (*it))
            {
                if (i % (*it) == 0)
                    okay++;
            }
            else if (i < (*it))
            {
                if ((*it) % i == 0)
                    okay++;
            }
            else // i == it
                okay++;
        }
        if (okay == notes.size())
        {
            std::stringstream ss;

            ss << i;
            return ss.str();
        }
    }
    return "NO";
}

int main()
{
    std::ifstream ifs("../C-small-attempt1.in");
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
