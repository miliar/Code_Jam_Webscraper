#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <cstdlib>

using namespace std;

int decode (const int A, const int B)
{
    int recycledPairs = 0;
    for ( int i = A; i < B ; i++)
        for ( int j = i + 1; j <= B; j++)
        {
            char bufferI[8] = "";
            char bufferJ[8] = "";
            itoa (i, bufferI, 10);            
            itoa (j, bufferJ, 10);            
            if (string(bufferI).length() == string(bufferJ).length())
            {
                string temp = string (bufferI) + string (bufferI);
                if (temp.find(string(bufferJ)) != string::npos)
                    ++recycledPairs;
            }
        }

    return recycledPairs;
}

int main(void)
{
    ifstream input ("C-small-attempt0.in");

    if (input.is_open())
    {
        int tests = 0;
        string line;
        if (input.good())
        {
            getline(input,line);
            tests = atoi ( line.c_str());
            if ( tests != 0 )
            {
                int i = 0;
                ofstream output;
                output.open("output1.txt");
                while (input.good() && i++ < tests)
                {
                    getline(input,line);
                    istringstream in(line, std::istringstream::in);
                    int A = 0, B = 0;
                    in >> A;
                    in >> B;
                    int recycledPairs = decode (A, B);
                    output << "Case #" << i << ": " << recycledPairs << endl;
                }
                output.close();
            }
        }

        input.close();
    }
    else
        cout <<"Couldn't open file!" << endl;

    return 0;

}

