#include <fstream>
#include <string>

using namespace std;

int main()
{
    ofstream output;
    ifstream input ("A-small-attempt0.in");
    output.open("A-small-attempt0.out");
    string table("yhesocvxduiglbkrztnwjpfmaq");
    string dummy;

    int t;

    
    input >> t;
    getline(input, dummy);

    for (int i=0; i<t; i++)
    {
        output << "Case #"<<i+1<<": ";
        string str;
        getline (input, str);
        for(int j=0; j<str.length(); j++)
        {
            if (str[j] == ' ')
                output << " ";
            else if (str[j] >= 'a' && str[j] <='z')
                output<<table[str[j]-'a'];
        }
        output << endl;
    }

}

