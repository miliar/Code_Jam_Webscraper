#include <iostream>
#include <string>
#include <fstream>
#include <stdlib.h>

using namespace std;

int main()
{
    ifstream inputFile("A-small-attempt0.in");
    ofstream outputFile("A-small-attempt0.out");

    if (inputFile.is_open() && inputFile.good() && outputFile.is_open() && outputFile.good())
    {
        string line;
        int numOfCases;

        getline(inputFile, line);
        numOfCases = atoi(line.c_str());

        for (int i=0; i<numOfCases; ++i)
        {
            string googlereseAl = "ynficwlbkuomxsevzpdrjgthaq";
            string out = "";

            getline(inputFile, line);

            for (int ii=0; ii<line.length(); ++ii)
            {
                if (line.at(ii) >= 'a' && line.at(ii) <= 'z')
                {
                    for (int iii=0; iii<26; ++iii)
                    {
                        if (googlereseAl.at(iii) == line.at(ii))
                        {
                            out += iii + 'a';
                        }
                    }
                }
                else
                    out += ' ';
            }

            outputFile << "Case #" << i+1 << ": " << out << "\n";
        }
    }

    inputFile.close();
    outputFile.close();

    return 0;
}
