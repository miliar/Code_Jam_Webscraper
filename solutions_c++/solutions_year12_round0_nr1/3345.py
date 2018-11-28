#include <cstdlib>
#include <iostream>
#include <map>

using namespace std;

int main(int argc, char *argv[])
{
    map<char,char> horadriccube;
    horadriccube[' ']=' ';
    horadriccube['a']='y';
    horadriccube['b']='h';
    horadriccube['c']='e';
    horadriccube['d']='s';
    horadriccube['e']='o';
    horadriccube['f']='c';
    horadriccube['g']='v';
    horadriccube['h']='x';
    horadriccube['i']='d';
    horadriccube['j']='u';
    horadriccube['k']='i';
    horadriccube['l']='g';
    horadriccube['m']='l';
    horadriccube['n']='b';
    horadriccube['o']='k';
    horadriccube['p']='r';
    horadriccube['q']='z';
    horadriccube['r']='t';
    horadriccube['s']='n';
    horadriccube['t']='w';
    horadriccube['u']='j';
    horadriccube['v']='p';
    horadriccube['w']='f';
    horadriccube['x']='m';
    horadriccube['y']='a';
    horadriccube['z']='q';
    int T;
    int t;
    int i;
    cin>>T;
    cin.ignore(256, '\n');
    string translation;
   
    for(t=0;t<T;t++)
    {
        char lineinput[101];
        cin.getline(lineinput,101);
        string stringinput = lineinput;
        translation = stringinput;
        int size=stringinput.size();
        
        for(int i=0;i<size;i++)
        {
                translation[i]=horadriccube[stringinput[i]];
        }
        cout<<"Case #"<<t+1<<": "<<translation<<"\n";
    }        
    
    

    
    
    //system("PAUSE");
    return EXIT_SUCCESS;
}
