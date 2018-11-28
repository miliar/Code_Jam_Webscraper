#include <iostream>
#include <string>
#include <fstream>
#include <cstdlib>

using namespace std;

void decode (const string line, const string decoder, string& decoded_string)
{
    int len = line.length();
    for (int i = 0; i < len; i++)
        if (line[i] == ' ')
            decoded_string.append(1,' ');
        else
            decoded_string.append(1,decoder[line[i] - 'a']);
}

int main(void)
{

    ifstream input ("A-small-attempt2.in");

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
                //cout << "[" << tests << "]" << endl;
                int i = 0;
                string decoder = "yhesocvxduiglbkrztnwjpfmaq";
                ofstream output;
                output.open("output.txt");
                //cout << "decoder length = [" << decoder.length() << "]" << endl;
                while (input.good() && i++ < tests)
                {
                    getline(input,line);
                    string decoded_string;
                    decode (line, decoder, decoded_string);
                    //cout << "[" << line << "]" << endl;
                    output << "Case #" << i << ": " << decoded_string << endl;
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

