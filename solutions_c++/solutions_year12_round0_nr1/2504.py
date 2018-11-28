#include <iostream>
#include <fstream>

using namespace std;

string translate(string to_translate)
{
    char to[] =   "abcdefghijklmnopqrstuvwxyz";
    char from[] = "ynficwlbkuomxsevzpdrjgthaq";
    char ttable[26];

    for(int i = 0; i<26; ++i)
    {
        ttable[i] = '?';
    }
    for(int i = 0; i<26; ++i)
    {
        if(from[i] != ' ')
        {
            ttable[from[i]-'a'] = to[i];
        }
    }

    for(int i=0; i<to_translate.size(); ++i)
    {
        if(to_translate[i] >= 'a' && to_translate[i] <= 'z')
        {
            int l = to_translate[i] - 'a';
            to_translate[i] = ttable[l];
        }
    }
    return to_translate;
}

int main(int argc, char* argv[])
{
    ifstream infile;
    ofstream outfile;
    infile.open( "/gcjam/A-small-attempt0.in");
    outfile.open( "/gcjam/output.txt");

    int ntestcases;
    infile >> ntestcases;
    infile.ignore(1, '\n');
    for(int i=0; i<ntestcases; ++i)
    {
        char line[256];
        infile.getline(line, 256);
        outfile << "Case #" << i << ": " << translate(line).c_str() << endl;
        cout << "Case #" << i << ": " << translate(line).c_str() << endl;
    }
	return 0;
}

