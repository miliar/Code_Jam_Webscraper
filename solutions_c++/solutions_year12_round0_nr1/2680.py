#include<iostream>
#include<cstring>
#include<algorithm>
using namespace std;

char tab[125];
char word[101];

int main()
{
    ios_base::sync_with_stdio(0);

    tab['a']='y';
    tab['b']='h';
    tab['c']='e';
    tab['d']='s';
    tab['e']='o';
    tab['f']='c';
    tab['g']='v';
    tab['h']='x';
    tab['i']='d';
    tab['j']='u';
    tab['k']='i';
    tab['l']='g';
    tab['m']='l';
    tab['n']='b';
    tab['o']='k';
    tab['p']='r';
    tab['q']='z';
    tab['r']='t';
    tab['s']='n';
    tab['t']='w';
    tab['u']='j';
    tab['v']='p';
    tab['w']='f';
    tab['x']='m';
    tab['y']='a';
    tab['z']='q';
    tab[' ']=' ';
    
    
    int Z;
    cin >> Z;
    cin.getline(word,101);
        
    for(int z=1; z<=Z; z++)
    {
        cin.getline(word,101);
        
        cout << "Case #" << z << ": ";
        
        for(int i=0; word[i]; i++)
            cout << tab[word[i]];
        
        cout << endl;    
    }
    
return 0;
}

