#include <iostream>
#include <fstream>
#include <string>

char translate(char c)
{
    if(c == 'y')
        return 'a';
    if(c == 'n')
        return 'b';
    if(c == 'f')
        return 'c';
    if(c == 'i')
        return 'd';
    if(c == 'c')
        return 'e';
    if(c == 'w')
        return 'f';
    if(c == 'l')
        return 'g';
    if(c == 'b')
        return 'h';
    if(c == 'k')
        return 'i';
    if(c == 'u')
        return 'j';
    if(c == 'o')
        return 'k';
    if(c == 'm')
        return 'l';
    if(c == 'x')
        return 'm';
    if(c == 's')
        return 'n';
    if(c == 'e')
        return 'o';
    if(c == 'v')
        return 'p';
    if(c == 'z')
        return 'q';
    if(c == 'p')
        return 'r';
    if(c == 'd')
        return 's';
    if(c == 'r')
        return 't';
    if(c == 'j')
        return 'u';
    if(c == 'g')
        return 'v';
    if(c == 't')
        return 'w';
    if(c == 'h')
        return 'x';
    if(c == 'a')
        return 'y';
    if(c == 'q')
        return 'z';

    return '1';
}

int main()
{
    std::ifstream fin("in.txt");
    std::ofstream fout("out.txt");
    std::string s;
    int n;

    fin >> n;
    getline(fin,s);

    for(int i = 1; i <= n; ++i)
    {
        getline(fin,s);
        fout << "Case #"<< i << ": ";
        for(auto it = s.begin(); it < s.end(); ++it)
        {
            if(*it != ' ')
                fout << translate(*it);
            else
                fout << ' ';
        }
        fout << '\n';
    }


    fout.close();
    fin.close();
    return 0;
}
