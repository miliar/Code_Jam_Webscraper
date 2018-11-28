#include <fstream>
#include <map>
#include <iostream>
#include <cstdlib>
using namespace std;
int main()
{
    //cout<<"YO"<<endl
    map<char,char> vals;
    int ka=0;
    vals['a']= 'y';vals['b']= 'h';vals['c']= 'e';vals['d']= 's';vals['e']= 'o';vals['f']= 'c';vals['g']= 'v';vals['h']= 'x';
    vals['i']= 'd';vals['j']= 'u';vals['k']= 'i';vals['l']= 'g';vals['m']= 'l';vals['n']= 'b';vals['o']= 'k';vals['p']= 'r';
    vals['q']= 'z';vals['r']= 't';vals['s']= 'n';vals['t']= 'w';vals['u']= 'j';vals['v']= 'p';vals['w']= 'f';vals['x']= 'm';
    vals['y']= 'a';vals['z']= 'q'; vals[' ']=' ';
    int k=0;
    ofstream out("1.out");
    ifstream in("2.txt");
    string ta;
    getline(in,ta);
    int t=atoi(ta.c_str());
    //cout<<t<<endl;
    while(k!=t)
    {
        k++;
        string m;
        getline(in,m);
        string s="";
        //cout<<m<<endl;
        for(int ia=0;ia<m.length();ia++)
        {
            //cout<<vals[m[ia]];
            s+=vals[m[ia]];
        }
        //cout<<endl;
        out<<"Case #"<<k<<": "<<s<<endl;
    }
}
