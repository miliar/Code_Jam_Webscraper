#include <iostream>
#include <fstream>
#include <vector>

struct action
{
    int pos;
    int order;
};

int process_vectors(const std::vector<action> &orange, const std::vector<action> &blue, int first)
{
    std::vector<action>::const_iterator fit, fite;
    std::vector<action>::const_iterator sit, site;
    int time = 0;
    int fpos = 1;
    int spos = 1;
    bool finished = false;
    bool action = false;

    if (first == 1)
    {
        fit = orange.begin();
        fite = orange.end();
        sit = blue.begin();
        site = blue.end();
    }
    else
    {
        sit = orange.begin();
        site = orange.end();
        fit = blue.begin();
        fite = blue.end();
    }
    while (!finished)
    {
        action = false;
        if (fit != fite)
        {
            if ((*fit).pos != fpos)
            {
                // move 1 meter
                if ((*fit).pos > fpos)
                    fpos++;
                else
                    fpos--;
                //std::cout << "First robot move to " << fpos << "\t";
            }
            else
            {
                // push button
                if ((sit == site) || (*fit).order < (*sit).order)
                {
                    if (!action)
                    {
                        // push button
                        //std::cout << "First robot pushes button " << (*fit).pos << "\t";
                        ++fit;
                        action = true;
                    }
                }
                else
                {
                    // wait
                    //std::cout << "First robot waits at " << fpos << "\t";
                }
            }
        }
        else
        {
            //std::cout << "First robot is done\t";
        }

        if (sit != site)
        {
            if ((*sit).pos != spos)
            {
                // move 1 meter
                if ((*sit).pos > spos)
                    spos++;
                else
                    spos--;
                //std::cout << "Second robot move to " << spos << std::endl;
            }
            else
            {
                // push button
                if ((fit == fite) || (*sit).order < (*fit).order)
                {
                    if (!action)
                    {
                        // push button
                        //std::cout << "Second robot pushes button " << (*sit).pos << std::endl;
                        ++sit;
                        action = true;
                    }
                }
                else
                {
                    // wait
                    //std::cout << "Second robot waits at " << spos << std::endl;
                }
            }
        }
        else
        {
            //    std::cout << "Second robot is done" << std::endl;
        }
        time++;
        if (fit == fite && sit == site)
            finished = true;
    }
    return time;
}

int process_line(std::ifstream &ifs)
{
    int nb_actions;
    char robot;
    int button;
    std::vector<action> orange;
    std::vector<action> blue;
    bool first = false;
    int first_robot = 0;
    action a;

    ifs >> nb_actions;
    for (int i = 0; i < nb_actions; ++i)
    {
        ifs >> robot;
        ifs >> a.pos;
        a.order = i;
        if (robot == 'O')
        {
            if (!first)
            {
                first_robot = 1;
                first = true;
            }
            orange.push_back(a);
        }
        else
        {
            if (!first)
            {
                first_robot = 2;
                first = true;
            }
            blue.push_back(a);
        }
    }
    return process_vectors(orange, blue, first);
}

int main()
{
    std::ifstream ifs("../A-large.in");
    std::ofstream ofs("A-large.out");
    int res;

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
