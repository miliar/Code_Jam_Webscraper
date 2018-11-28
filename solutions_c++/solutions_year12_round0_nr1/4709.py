#include <iostream>
#include <list>
#include <fstream>
#include <map>

using namespace std;

int main()
{
    int max = 0;
    char m[27] = "ynficwlbkuomxsevzpdrjgthaq";
    
    map<char,char> fn;
    
    for(int i=0; i<26; i++)
    {
        fn.insert(pair<char, char>(m[i], (char)(i+97)));
    }
    
    fn.insert(pair<char, char>(' ', ' '));
    
    char str[101] = "";
    
    ifstream fin("A-small-attempt2.in");
    ofstream fout("A-small-attempt2.out");
    
    if(!fin) cerr <<"Error";
    
    fin >> max;
    fin.getline(str, 100); //adjusting
    
    for(int i=0; i<max; i++){
        fin.getline(str, 101);
        
        fout << "Case #" << i+1 << ": ";
        
        for(int j=0; str[j]; j++)
            fout << fn[str[j]];
        
        fout << endl;
    }
    
    fout.close();
    fin.close();
    return 0;
}
