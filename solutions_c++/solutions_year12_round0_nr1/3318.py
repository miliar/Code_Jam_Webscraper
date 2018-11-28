#include<iostream>
#include<map>
using namespace std;
int main()
{
    map<char ,char > language;
    int i,j,k,l;
    string input,temp;
    language['a']='y';
    language['b']='h';
    language['c']='e';
    language['d']='s';
    language['e']='o';
    language['f']='c';
    language['g']='v';
    language['h']='x';
    language['i']='d';
    language['j']='u';
    language['k']='i';
    language['l']='g';
    language['m']='l';
    language['n']='b';
    language['o']='k';
    language['p']='r';
    language['q']='z';
    language['r']='t';
    language['s']='n';
    language['t']='w';
    language['u']='j';
    language['v']='p';
    language['w']='f';
    language['x']='m';
    language['y']='a';
    language['z']='q';
    language[' ']=' ';
    int testCase;
    cin>>testCase;
    getline(cin,temp);
    for(int t=0;t<testCase;t++)
    {


        getline(cin,input);
        cout<<"Case #"<<t+1<<": ";
        for(i=0;i<input.length();i++)
        {
            cout<<language[input[i]];
        }
        cout<<endl;
    }
}
