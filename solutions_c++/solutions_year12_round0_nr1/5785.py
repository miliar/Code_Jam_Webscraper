#include <iostream>
#include <string>
#include <sstream>

using namespace std;

const string dictionary = 
   "yhesocvxduiglbkrztnwjpfmaq";

string convert(string in)
{
    for(size_t i = 0; i < in.length(); i++)
    {
        char& c = in[i];
        if(c >= 'a' && c <= 'z')
            c = dictionary[c-'a'];
    }
    return in;
}

int main()
{
    int testcases;
    string line;
    getline(cin, line);
    stringstream ss;
    ss << line;
    ss >> testcases;
    
    for(int i = 0; i < testcases; i++)
    {
        getline(cin, line);
        cout << "Case #" << (i+1) << ": " << convert(line) << endl;
    }
}


