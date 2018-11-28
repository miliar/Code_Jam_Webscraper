#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <algorithm>

struct combine
{
    char b1;
    char b2;
    char nbe;
};

struct opposed
{
    char b1;
    char b2;
};

std::string make_str(std::vector<char> &invokes)
{
    std::string res_str;

    res_str = "[";
    for (unsigned int i = 0; i < invokes.size(); ++i)
    {
        res_str += invokes[i];
        if (i+1 < invokes.size())
            res_str += ", ";
    }
    res_str += "]";
    return res_str;
}

void process_vectors(const std::vector<combine> &combs, const std::vector<opposed> &ops, std::vector<char> &invokes)
{
    std::vector<combine>::const_iterator cit, cite;
    std::vector<opposed>::const_iterator oit, oite;
    std::vector<char>::iterator iit, iite;
    std::vector<char> res;

    iit = invokes.begin();
    iite = invokes.end();
    for (int i = 0; iit != iite; ++iit, ++i)
    {
        cit = combs.begin();
        cite = combs.end();
        for (; cit != cite; ++cit)
        {
            if (iit != invokes.begin())
            {
                if (((*cit).b1 == (*iit) && (*cit).b2 == *(iit - 1))
                    || ((*cit).b2 == (*iit) && (*cit).b1 == *(iit - 1)))
                {
                    iit = invokes.erase(iit -1, iit + 1);
                    iit = invokes.insert(iit, (*cit).nbe);
                    iite = invokes.end();
                }
            }

        }
        if (invokes.size() == 0)
            break;
        oit = ops.begin();
        oite = ops.end();
        for (; oit != oite; ++oit)
        {
            if ((*oit).b1 == *iit)
            {
                if (std::find(invokes.begin(), iit, (*oit).b2) != iit)
                {
                    iit = invokes.erase(invokes.begin(), iit + 1);
                    iite = invokes.end();
                    if (invokes.size() == 0)
                        break;
                }
            }
            else if ((*oit).b2 == *iit)
            {
                if (std::find(invokes.begin(), iit, (*oit).b1) != iit)
                {
                    iit = invokes.erase(invokes.begin(), iit + 1);
                    iite = invokes.end();
                    if (invokes.size() == 0)
                        break;
                }
            }
        }
        if (invokes.size() == 0)
            break;
    }

}

std::string process_line(std::ifstream &ifs)
{
    std::string tmp;
    // combined
    int nb_combine;
    combine c;
    std::vector<combine> combs;
    // opposed
    int nb_opposed;
    opposed o;
    std::vector<opposed> ops;
    // invoke list
    int nb_invoke;
    std::vector<char> invokes;
    // results
    std::string res_str;

    ifs >> nb_combine;
    for (int i = 0; i < nb_combine; ++i)
    {
        ifs >> tmp;
        c.b1 = tmp[0];
        c.b2 = tmp[1];
        c.nbe = tmp[2];
        combs.push_back(c);
        tmp.clear();
    }
    ifs >> nb_opposed;
    for (int i = 0; i < nb_opposed; ++i)
    {
        ifs >> tmp;
        o.b1 = tmp[0];
        o.b2 = tmp[1];
        ops.push_back(o);
        tmp.clear();
    }
    ifs >> nb_invoke;
    ifs >> tmp;
    for (int i = 0; i < nb_invoke; ++i)
    {
        invokes.push_back(tmp[i]);    
    }
    tmp.clear();
    process_vectors(combs, ops, invokes);
    return make_str(invokes);
}

int main()
{
    std::ifstream ifs("B-large.in");
    std::ofstream ofs("A-large.out");
    std::string res;

    if (ifs.is_open() && ofs.is_open())
    {
        int nb_lines;

        ifs >> nb_lines;
        for (int i = 0; i < nb_lines; ++i)
        {
            res = process_line(ifs);
            ofs << "Case #" << i+1 << ": " << res << std::endl;
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
