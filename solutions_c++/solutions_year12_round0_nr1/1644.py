#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
using namespace std;

int main()
{
    ifstream myfile ("A-small-attempt1.in");
    ofstream out;
    out.open ("att.txt");

    string line;
    int no;
    getline (myfile,line);
    istringstream as(line);
    as >> no;
    for (int i=0 ; i<no ;i++)
    {
        getline (myfile,line);
        for(unsigned int j=0; j<line.length();j++)
        {

            switch(line.at(j))
            {
                case 97://a->y
                    line = line.substr(0,j) + 'y' + line.substr(j+1);
                    break;
                case 98:
                    line = line.substr(0,j) + 'h' + line.substr(j+1);
                    break;
                case 99:
                    line = line.substr(0,j) + 'e' + line.substr(j+1);
                    break;
                case 100:
                    line = line.substr(0,j) + 's' + line.substr(j+1);
                    break;
                case 101:
                    line = line.substr(0,j) + 'o' + line.substr(j+1);
                    break;
                case 102://f
                    line = line.substr(0,j) + 'c' + line.substr(j+1);
                    break;
                case 103:
                    line = line.substr(0,j) + 'v' + line.substr(j+1);
                    break;
                case 104:
                    line = line.substr(0,j) + 'x' + line.substr(j+1);
                    break;
                case 105:
                    line = line.substr(0,j) + 'd' + line.substr(j+1);
                    break;
                case 106:
                    line = line.substr(0,j) + 'u' + line.substr(j+1);
                    break;
                case 107:
                    line = line.substr(0,j) + 'i' + line.substr(j+1);
                    break;
                case 108:
                    line = line.substr(0,j) + 'g' + line.substr(j+1);
                    break;
                case 109:
                    line = line.substr(0,j) + 'l' + line.substr(j+1);
                    break;
                case 110:
                    line = line.substr(0,j) + 'b' + line.substr(j+1);
                    break;
                case 111:
                    line = line.substr(0,j) + 'k' + line.substr(j+1);
                    break;
                case 112:
                    line = line.substr(0,j) + 'r' + line.substr(j+1);
                    break;
                case 113://q
                    line = line.substr(0,j) + 'z' + line.substr(j+1);
                    break;
                case 114:
                    line = line.substr(0,j) + 't' + line.substr(j+1);
                    break;
                case 115:
                    line = line.substr(0,j) + 'n' + line.substr(j+1);
                    break;
                case 116:
                    line = line.substr(0,j) + 'w' + line.substr(j+1);
                    break;
                case 117:
                    line = line.substr(0,j) + 'j' + line.substr(j+1);
                    break;
                case 118:
                    line = line.substr(0,j) + 'p' + line.substr(j+1);
                    break;
                case 119:
                    line = line.substr(0,j) + 'f' + line.substr(j+1);
                    break;
                case 120://x
                    line = line.substr(0,j) + 'm' + line.substr(j+1);
                    break;
                case 121:
                    line = line.substr(0,j) + 'a' + line.substr(j+1);
                    break;
                case 122:
                    line = line.substr(0,j) + 'q' + line.substr(j+1);
                    break;
            }
        }
        out << "Case #" << i+1 << ": " << line << endl;

    }
    myfile.close();
    out.close();
    return 0;
}
