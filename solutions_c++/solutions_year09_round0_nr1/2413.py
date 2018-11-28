#include <sstream>
#include <iostream>
#include <fstream>
#include <list>

using namespace std;

ifstream in("A-large.in");
ofstream out("A.out");

list<string> word;
list<string> pattern;
list<string>::iterator it;
list<char> character;
int L, D, N, X;

void comparar(int position)
{
    list<char>::iterator it2;

    
    it = pattern.begin();
    while (it != pattern.end())
    {
        for (it2 = character.begin(); it2 != character.end(); it2++)
        {
            if ( (*it)[position] == *it2 )
            {
                break;
            }
        }
        if (it2 == character.end())
        {
            it = pattern.erase(it);
        }
        else
        {
            it++;
        }
    }
}
 
int main()
{
    string str;
    int d, n, i, position;

    //input
    getline(in,str);
    istringstream iss(str);
    
    iss>>L>>D>>N;
    for (d=0; d<D; d++)
    {
        getline(in,str);
        word.push_back(str);
    }

    for (X=1; X<=N; X++)
    {
        //init
        pattern.clear();
        for (it = word.begin(); it != word.end(); it++)
        {
            pattern.push_back(*it);
        }
        //algorithm
        position = 0;
        getline(in,str);
        for (i=0; i<str.length(); i++)
        {
            character.clear();
            if (str[i] != '(')
            {
                character.push_back(str[i]);
            }
            else
            {
                i++;
                while (str[i] != ')')
                {
                    character.push_back(str[i]);
                    i++;
                }
            }
            comparar(position);
            position++;
        }
        //output
        out<<"Case #"<<X<<": "<<pattern.size()<<endl;
    }

    return EXIT_SUCCESS;
}
