#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    const int nAlphabet = 26;
    char mapping[nAlphabet] = {'q', 'a', 'm', 'f', 'p', 'j', 'w', 'n', 't', 'z', 'r', 'k', 'b', 'l', 'g', 'i', 'u', 'd', 'x', 'v', 'c', 'o', 's', 'e', 'h', 'y'};

    ifstream input("1a.input");
    ofstream output("1a.output");
    if(!input.is_open() || !output.is_open())
        return -1;

    int nTests;
    string inputLine;
    input >> nTests;
    getline(input, inputLine);
    for(int iTest = 1; iTest <= nTests; ++iTest)
    {
        getline(input, inputLine);
        output << "Case #" << iTest << ": ";
        for(int iChar = 0; iChar < inputLine.size(); ++iChar)
            output << (inputLine[iChar] != ' ' ? mapping['z' - (int) inputLine[iChar]] : ' ');
        output << endl;
    }

    input.close();
    output.close();
}
