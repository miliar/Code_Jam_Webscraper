#include <iostream>
#include "stdio.h"
#include "math.h"
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

void func(void) {
    return ;
}

int main(void) {
    
    //1. define all the virables first
    int T;
    char map[26];
    string s;
  
map['y'-'a'] = 'a';
map['e'-'a'] = 'o';
map['q'-'a'] = 'z';
map['j'-'a'] = 'u';
map['p'-'a'] = 'r';
map['m'-'a'] = 'l';
map['s'-'a'] = 'n';
map['l'-'a'] = 'g';
map['c'-'a'] = 'e';
map['k'-'a'] = 'i';
map['d'-'a'] = 's';
map['x'-'a'] = 'm';
map['v'-'a'] = 'p';
map['n'-'a'] = 'b';
map['r'-'a'] = 't';
map['i'-'a'] = 'd';
map['b'-'a'] = 'h';
map['t'-'a'] = 'w';
map['h'-'a'] = 'x';
map['w'-'a'] = 'f';
map['o'-'a'] = 'k';
map['a'-'a'] = 'y';
map['f'-'a'] = 'c';
map['g'-'a'] = 'v';
map['u'-'a'] = 'j';
map['z'-'a'] = 'q';
    cin>>T;
    getchar();
    int c=1;
    while(T--) {
        getline(cin, s); 
        for(int i=0; i<s.length(); i++) {
            if(' ' == s[i] || '\n' == s[i])
                continue;
            s[i] = map[s[i]-'a'];
        } 
        cout<<"Case #"<<c++<<": "<<s<<endl;
    } 
    return 0;

}
