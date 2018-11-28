#include<iostream>
#include<fstream>
#include<string>
#include<map>
using namespace std;
int main()
{
    int t, i, j, len;

    ifstream in ("A-small-attempt0.in");
    fflush(stdin);
    in>>t;
    ofstream of;
    
    of.open("b.txt");
    
    map<char, char>m;
    m['a']='y';
    m['b']='h';
    m['c']='e';
    m['d']='s';
    m['e']='o';
    m['f']='c';
    m['g']='v';
    m['h']='x';
    m['i']='d';
    m['j']='u';
    m['k']='i';
    m['l']='g';
    m['m']='l';
    m['n']='b';
    m['o']='k';
    m['p']='r';
    m['q']='z';
    m['r']='t';
    m['s']='n';
    m['t']='w';
    m['u']='j';
    m['v']='p';
    m['w']='f';
    m['x']='m';
    m['y']='a';
    m['z']='q';
    m[' ']=' ';
    string s;
    getline(in,s);
    for(j=1;j<=t;j++){

        getline(in,s);
        len=s.length();
        for(i=0;i<len;i++){
              s[i]=m[s[i]];
        }
        //cout<<len;
        of<<"Case #"<<j<<": ";
        for(i=0;i<len;i++)
                          of<<s[i];
        if(j!=t)
        of<<endl;
    }
    of.close();
//    system("pause");
    return 0;
}             
        
