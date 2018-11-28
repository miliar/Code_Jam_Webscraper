#include <iostream>
#include <fstream>
#include <string>
#include <map>
using namespace std;

map<char,char> dictionary;
map<char,char>::iterator it;
void init()
{
     dictionary['y'] = 'a';
     dictionary['n'] = 'b';
     dictionary['f'] = 'c';
     dictionary['i'] = 'd';
     dictionary['c'] = 'e';
     dictionary['w'] = 'f';
     dictionary['l'] = 'g';
     dictionary['b'] = 'h';
     dictionary['k'] = 'i';
     dictionary['u'] = 'j';
     dictionary['o'] = 'k';
     dictionary['m'] = 'l';
     dictionary['x'] = 'm';
     dictionary['s'] = 'n';
     dictionary['e'] = 'o';
     dictionary['v'] = 'p';
     dictionary['z'] = 'q';
     dictionary['p'] = 'r';
     dictionary['d'] = 's';
     dictionary['r'] = 't';
     dictionary['j'] = 'u';
     dictionary['g'] = 'v';
     dictionary['t'] = 'w';
     dictionary['h'] = 'x';
     dictionary['a'] = 'y';
     dictionary['q'] = 'z';
}


int main()
{
    init();
    ifstream fin("a.txt");
    ofstream fout("result.txt");
    
    int n;
    string b;
    char a;
    fin >> n;
//    fin >> a;
//    cout<<a;
getline(fin,b);
    for (int i=0; i<n; i++)
    {
        getline(fin,b);
        fout<<"Case #"<<(i+1)<<": ";
        for (int j=0; j<b.size(); j++)
        {
            if (b[j]!=' ')
            {
               it = dictionary.find(b[j]);
               fout<<(*it).second;
            }
            else
            {
                fout<<" ";
            }
        }
        fout<<endl;
    }
    fin.close();
    fout.close();
    system("pause");
    
    return 0;
}
    
