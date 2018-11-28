#include<iostream>
#include<algorithm>
#include<map>
using namespace std;

int main()
{
    int t;
    cin>>t;
    string s[t];
    cin.get();
    int i=0;
    map<char,char> m;
    m['e'] = 'o';
    m['j'] = 'u';
    m['p'] = 'r';
    m['m'] = 'l';
    m['y'] = 'a';
    m['s'] = 'n';
    m['l'] = 'g';
    m['c'] = 'e';
    m['k'] = 'i';
    m['d'] = 's';
    m['x'] = 'm';
    m['v'] = 'p';
    m['e'] = 'o';
    m['n'] = 'b';
    m['r'] = 't';
    m['i'] = 'd';
    m['f'] = 'c';
    m['b'] = 'h';
    m['o'] = 'k';
    m['l'] = 'g';
    m['g'] = 'v';
    m['a'] = 'y';
    m['t'] = 'w';
    m['w'] = 'f';
    m['u'] = 'j';
    m['q'] = 'z';
    m['h'] = 'x';
    m['z'] = 'q';
    while(i<t)
    {
        getline(cin,s[i]);
        //cout<<s[i].length();
        cout<<"Case #"<<i+1<<": ";
        
        for(int j=0;j<s[i].length();j++)
        if(s[i][j] == ' ')
        cout<<' ';
        else
        cout<<m[s[i][j]];
        
        cout<<endl;
        i++;
    }
    
    return 0;
}
