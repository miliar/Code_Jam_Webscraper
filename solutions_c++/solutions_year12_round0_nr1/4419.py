#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <cmath>

using namespace std;

int main()
{
    ifstream stream("C:/A-small-attempt2.in");
    ofstream result("C:/result.txt");

if(stream && result)
{
    string line;
    int nb_cases, b=2;
    char a;
    getline(stream, line);
    istringstream ss(line);
    ss >> nb_cases;
    result << "Case #1: ";
        while(stream.get(a) && b<=nb_cases+1)
        {
            switch(a)
            {
                case 'a':
                result << 'y';
                break;
                case 'b':
                result << 'h';
                break;
                case 'c':
                result << 'e';
                break;
                case 'd':
                result << 's';
                break;
                case 'e':
                result << 'o';
                break;
                case 'f':
                result << 'c';
                break;
                case 'g':
                result << 'v';
                break;
                case 'h':
                result << 'x';
                break;
                case 'i':
                result << 'd';
                break;
                case 'j':
                result << 'u';
                break;
                case 'k':
                result << 'i';
                break;
                case 'l':
                result << 'g';
                break;
                case 'm':
                result << 'l';
                break;
                case 'n':
                result << 'b';
                break;
                case 'o':
                result << 'k';
                break;
                case 'p':
                result << 'r';
                break;
                case 'q':
                result << 'z';
                break;
                case 'r':
                result << 't';
                break;
                case 's':
                result << 'n';
                break;
                case 't':
                result << 'w';
                break;
                case 'u':
                result << 'j';
                break;
                case 'v':
                result << 'p';
                break;
                case 'w':
                result << 'f';
                break;
                case 'x':
                result << 'm';
                break;
                case 'y':
                result << 'a';
                break;
                case 'z':
                result << 'q';
                break;
                case ' ':
                result << ' ';
                break;
                case '\n':
                result << endl;
                if(b<=nb_cases)
                {
                    result << "Case #" << b << ": ";
                }
                b++;
                break;
                default:
                result << a;
                break;

            }
        }
}
else
{
    result << "ERREUR: Impossible d'ouvrir le fichier en lecture." << endl;
}
    return 0;
}
