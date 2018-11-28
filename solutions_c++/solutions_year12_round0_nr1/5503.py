#include <iostream>
#include <map>

using namespace std;
map<char,char> m;
int main() {
    m['a']= 'y';
    m['b']= 'h';
    m['c']= 'e';
    m['d']= 's';
    m['e']= 'o';
    m['f']= 'c';
    m['g']= 'v';
    m['h']= 'x';
    m['i']= 'd';
    m['j']= 'u';
    m['k']= 'i';
    m['l']= 'g';
    m['m']= 'l';
    m['n']= 'b';
    m['o']= 'k';
    m['p']= 'r';
    m['q']= 'z';
    m['r']= 't';
    m['s']= 'n';
    m['t']= 'w';
    m['u']= 'j';
    m['v']= 'p';
    m['w']= 'f';
    m['x']= 'm';
    m['y']= 'a';
    m['z']= 'q';
    
    char ch;
    int num;cin >> num;
    string in;
    getline(cin,in);
    for(int xi=0;xi<num;xi++) {
        getline(cin,in);
        cout << "Case #" << xi+1 << ": ";
        for(int i=0;i<in.size();i++) {
            if(in[i]>='a'&& in[i]<='z') cout << m[in[i]];
            else cout << in[i];
        }
        cout << '\n';
    }
}