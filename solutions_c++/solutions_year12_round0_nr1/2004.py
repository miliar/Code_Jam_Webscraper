#include<iostream>
#include<fstream>
#include<map>

using namespace std;

map<char, char> charmap;

int main()
{
    charmap['y'] = 'a';
    charmap['n'] = 'b';
    charmap['f'] = 'c';
    charmap['i'] = 'd';
    charmap['c'] = 'e';
    charmap['w'] = 'f';
    charmap['l'] = 'g';
    charmap['b'] = 'h';
    charmap['k'] = 'i';
    charmap['u'] = 'j';
    charmap['o'] = 'k';
    charmap['m'] = 'l';
    charmap['x'] = 'm';
    charmap['s'] = 'n';
    charmap['e'] = 'o';
    charmap['v'] = 'p';
    charmap['z'] = 'q';
    charmap['p'] = 'r';
    charmap['d'] = 's';
    charmap['r'] = 't';
    charmap['j'] = 'u';
    charmap['g'] = 'v';
    charmap['t'] = 'w';
    charmap['h'] = 'x';
    charmap['a'] = 'y';
    charmap['q'] = 'z';

    char getch;
    ifstream infile ("A-small-attempt0.in");
    ofstream outfile;
    outfile.open("output.txt");
    int numlines = 0;
    int index = 0;

    if (infile.is_open())
    {
        while (!infile.eof())
        {
            //infile.get(getch);
            getch = infile.get();
            //if ()
            if (getch >= '0' && getch <= '9')
            {
                numlines = numlines * 10 + getch - '0';
                continue;
            }
            if (getch == '\n')
            {
                if (index > 0)
                {
                    outfile << "\n";
                }
                index++;
                if (index <= numlines)
                {
                    outfile << "Case #" << index << ": ";
                }
                continue;
            }
            if (getch == ' ')
            {
                outfile << " ";
                continue;
            }
            if (getch >= 'a' && getch <= 'z')
            {
                outfile << charmap[getch];
            }
        }

    }
    else
    {
        cout << "unable to open file\n";
    }

    return 0;
}
