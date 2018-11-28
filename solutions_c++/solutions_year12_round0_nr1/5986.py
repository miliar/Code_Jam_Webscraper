#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
using namespace std;

int main()
{
    ifstream in("A-small-attempt0.in");
    ofstream out("output.txt");
    int noc;
    in >> noc;
    string str;
    string arr = "abcdefghijklmnopqrstuvwxyz" ;
    string arr1 = "yhesocvxduiglbkrztnwjpfmaq";
    
    
    in.ignore();
    
    for (int i=0; i<noc; i++)
    {
        out << "Case #" << i+1 << ": ";
        
        //getline(in, str);
        getline(in, str);
        for (int j=0; j<str.length(); j++)
        {
            if (str[j] == ' ')
            {
               out << " ";
               continue;
            }
            int z=0;
            for (; z<26; z++)
            {
                if (str[j] == arr[z])
                   break;
            }
            out << arr1[z];
        }
        out << endl;
    }
    
    return 0;
}
