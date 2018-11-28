#include <fstream>
#include <string>

using namespace std;

int main (void)
{
    string translate = "yhesocvxduiglbkrztnwjpfmaq";
    string str;
    int T, i, j;
    fstream fin, fout;
    
    fin.open ("A-small-attempt3.in", ios::in);
    fout.open ("output.txt", ios::out);
    
    fin >> T;
    
    fin.ignore ();
    for (j = 1; j <= T; j++)
    {
        getline (fin, str);
        
        fout << "Case #" << j << ": ";
        for (i = 0; i < str.length (); i++)
        {
            if (str[i] == ' ')
                fout << " ";
            else
                fout << translate[unsigned (str[i] - 'a')];
        }
        fout << "\n";
    }
    
    return 0;
}    
