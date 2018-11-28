/*
 ** exo1.cpp for codejam
 **
 ** Made by Guillaume "Vermeille" Sanchez
 ** Login   sanche_g <Guillaume.V.Sanchez@gmail.com>
 **
 ** Started on sam.  14 avril 2012 18:57:12 CEST Guillaume "Vermeille"  Sanchez
 ** Last update sam. 14 avril 2012 19:39:05 CEST Guillaume "Vermeille" Sanchez
 */

#include <iostream>
#include <map>
#include <string>
#include <algorithm>

int main()
{
    char tr[26];
    tr['a'-'a'] = 'y';
    tr['b'-'a'] = 'h';
    tr['c'-'a'] = 'e';
    tr['d'-'a'] = 's';
    tr['e'-'a'] = 'o';
    tr['f'-'a'] = 'c';
    tr['g'-'a'] = 'v';
    tr['h'-'a'] = 'x';
    tr['i'-'a'] = 'd';
    tr['j'-'a'] = 'u';
    tr['k'-'a'] = 'i';
    tr['l'-'a'] = 'g';
    tr['m'-'a'] = 'l';
    tr['n'-'a'] = 'b';
    tr['o'-'a'] = 'k';
    tr['p'-'a'] = 'r';
    tr['q'-'a'] = 'z';
    tr['r'-'a'] = 't';
    tr['s'-'a'] = 'n';
    tr['t'-'a'] = 'w';
    tr['u'-'a'] = 'j';
    tr['v'-'a'] = 'p';
    tr['w'-'a'] = 'f';
    tr['x'-'a'] = 'm';
    tr['y'-'a'] = 'a';
    tr['z'-'a'] = 'q';

    int nbr;
    std::cin >> nbr;

        std::string line;
        std::getline(std::cin, line);
    for (int i = 0 ; i < nbr ; ++i)
    {
        std::cout << "Case #" << (i+1) << ": ";
        std::string line;
        std::getline(std::cin, line);
        for (int j = 0 ; j < line.length() ; ++j)
        {
            if (line[j] != ' ')
                std::cout << tr[line[j]-'a'];
            else
                std::cout << ' ';
        }
        std::cout << std::endl;
    }

    return 0;
}

