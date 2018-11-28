#include<iostream>
#include<vector>
#include<fstream>
#include<map>
#include<sstream>
#include<string>
#include<algorithm>
using namespace std;
#define REP(i,n) for(int i =0;i<n;i++)
#define FOR(i,a,b) for(int i =a;i<=b;i++)
int main(){
    int kase, T;
    string s, temp;
    map<char, char > mp;
    mp['a'] = 'y', mp['b'] = 'h', mp['c']='e', mp['d'] = 's', mp['e'] ='o', mp['f'] = 'c', mp['g'] = 'v', mp['h'] = 'x',mp['i'] = 'd',mp['j'] = 'u',mp['k'] = 'i',mp['l'] = 'g',mp['m'] = 'l',mp['n'] = 'b',mp['o'] = 'k',mp['p'] = 'r',mp['q'] = 'z',mp['r'] = 't',mp['s'] = 'n',mp['t'] = 'w',mp['u'] = 'j',mp['v'] = 'p',mp['w'] = 'f',mp['x'] = 'm',mp['y'] = 'a',mp['z'] = 'q';
    cin>>T;
    stringstream ss;
    getline(cin,temp);
    ss<<temp;
    ss>>T;
    for(int kase = 1;kase <= T;kase++){
        getline(cin,s);
        string ans;
        for(int i =0;i<s.size();i++){
            if(s[i] == ' ')
                ans += ' ';
            else
                ans += mp[s[i]];
        }
        cout<< "Case #"<<kase<<": " <<ans<<endl;
    }
    return 0;
}
