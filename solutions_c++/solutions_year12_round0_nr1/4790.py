#include <iostream>
#include <fstream>
#include <string>

//            abcdefghijklmnopqrstuvwxyz
char map[] = "yhesocvxduiglbkrztnwjpfmaq";

using namespace std;

int main()
{
    int N;
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    fin >> N;
    string line;
    getline(fin, line);
    for(int i=0; i<N; ++i)
    {
        fout << "Case #" << (i+1) << ": ";
        getline(fin, line);
        for(int j=0; j<line.size(); ++j)
        {
            char c = line[j];
            char co;
            if(c >= 'a' && c <= 'z')
                co = map[c - 'a'];
            else if(c == ' ')
                co = c;
            else
                break;
            fout << co;
        }
        fout << endl;
    }
    return 0;
}
