#include <iostream>
#include<fstream>
#include<string>
#include<map>
#include<stdlib.h>
using namespace std;
map<char,char> alpha;

int main()
{
    int i,j,t;
    size_t len;
    //string s;
    char temp[100],str[500];
    alpha['a']='y';
    alpha['b']='h';
    alpha['c']='e';
    alpha['d']='s';
    alpha['e']='o';
    alpha['f']='c';
    alpha['g']='v';
    alpha['h']='x';
    alpha['i']='d';
    alpha['j']='u';
    alpha['k']='i';
    alpha['l']='g';
    alpha['m']='l';
    alpha['n']='b';
    alpha['o']='k';
    alpha['p']='r';
    alpha['q']='z';
    alpha['r']='t';
    alpha['s']='n';
    alpha['t']='w';
    alpha['u']='j';
    alpha['v']='p';
    alpha['w']='f';
    alpha['x']='m';
    alpha['y']='a';
    alpha['z']='q';
    alpha[' ']=' ';
    ifstream inp_file("input",ios::in);
    inp_file.getline(temp,500);
    t=atoi(temp);
    for(i=0;i<t;i++)
    {
        inp_file.getline(str,500);
        len=0;
        j=0;
        while(str[j++]!='\0')
        len++;
        for(j=0;j<len;j++)
        {
            str[j]=alpha[str[j]];
        }
        cout<<"Case #"<<i+1<<": "<<str<<"\n";
    }
    return 0;
}
