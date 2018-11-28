#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
    int cases = 0;
    cin >> cases;
    vector <string> text(cases);

    cin.ignore();
    int i = 0;
    while(i < text.size())
        getline(cin, text[i++]);

    vector <string> resultant(cases);

    for(int j = 0; j < text.size(); j++)
    {
        for(register int i = 0; i < text[j].length(); i++)
        {
            switch(toupper(text[j][i]))
            {
                case 'Y':
                    resultant[j].push_back(tolower('A'));
                break;
                case 'N':
                    resultant[j].push_back(tolower('B'));
                break;
                case 'F':
                    resultant[j].push_back(tolower('C'));
                break;
                case 'I':
                    resultant[j].push_back(tolower('D'));
                break;
                case 'C':
                    resultant[j].push_back(tolower('E'));
                break;
                case 'W':
                    resultant[j].push_back(tolower('F'));
                break;
                case 'L':
                    resultant[j].push_back(tolower('G'));
                break;
                case 'B':
                    resultant[j].push_back(tolower('H'));
                break;
                case 'K':
                    resultant[j].push_back(tolower('I'));
                break;
                case 'U':
                    resultant[j].push_back(tolower('J'));
                break;
                case 'O':
                    resultant[j].push_back(tolower('K'));
                break;
                case 'M':
                    resultant[j].push_back(tolower('L'));
                break;
                case 'X':
                    resultant[j].push_back(tolower('M'));
                break;
                case 'S':
                    resultant[j].push_back(tolower('N'));
                break;
                case 'E':
                    resultant[j].push_back(tolower('O'));
                break;
                case 'V':
                    resultant[j].push_back(tolower('P'));
                break;
                case 'Z':
                    resultant[j].push_back(tolower('Q'));
                break;
                case 'P':
                    resultant[j].push_back(tolower('R'));
                break;
                case 'D':
                    resultant[j].push_back(tolower('S'));
                break;
                case 'R':
                    resultant[j].push_back(tolower('T'));
                break;
                case 'J':
                    resultant[j].push_back(tolower('U'));
                break;
                case 'G':
                    resultant[j].push_back(tolower('V'));
                break;
                case 'T':
                    resultant[j].push_back(tolower('W'));
                break;
                case 'H':
                    resultant[j].push_back(tolower('X'));
                break;
                case 'A':
                    resultant[j].push_back(tolower('Y'));
                break;
                case 'Q':
                    resultant[j].push_back(tolower('Z'));
                break;
                default:
                    resultant[j].push_back(' ');
                break;
            }
        }
    }

    for( int i = 0; i < text.size(); i++)
        cout << "Case #" << i+1 << ": " << resultant[i] << endl;
}
