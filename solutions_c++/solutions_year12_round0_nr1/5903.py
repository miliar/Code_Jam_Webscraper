#include <iostream>

#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;


const char gbc[] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
const char ggbc[] = {'Y','H','E','S','O','C','V','X','D','U','I','G','L','B','K','R','Z','T','N','W','J','P','F','M','A','Q'};

char toGoogle(char c)
{
    if(c >= 'a' && c <= 'z') {
        return gbc[c - 'a'];
    }
    else if(c >= 'A' && c <= 'Z') {
        return ggbc[c - 'A'];
    }

    return c;
}

int main()
{
    ifstream in("input.txt");
    ofstream out("output.txt");

    int numCases = 0;
    in >> numCases;

    string fakeline;
    getline(in, fakeline);

    for(int c = 0; c < numCases; c++) {
        out << "Case #" << c + 1 << ": ";
        string line;
        getline(in, line);
        for(size_t i = 0; i < line.length(); i++) {
            out << toGoogle(line.at(i));
        }
        out << endl;
    }

    in.close();
    out.close();
    return 0;
}
