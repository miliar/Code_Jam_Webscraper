#include <iostream>
#include <cstdio>
#include <map>
#include <set>
#include <string>
#include <cstring>
#include <sstream>
#include <vector>
#include <queue>
#include <bitset>
#include <cmath>
#include <stack>
#include <algorithm>
#include <cctype>
#include <fstream>
#include <cassert>
#include <iomanip>
using namespace std;
#define pb push_back
#define f first
#define s second
#define mp make_pair
#define E 1e-9
#define FOR(i,ini,fin) for(int i=ini;i<fin;i++)

#define M 1000000000
#define P 100.0000000

typedef long long L;
typedef double D;
typedef pair<int,int>par;

map<char,char>mapa;
map<char,char>::iterator iter;

string f(string s){
    string r="";
    for(int i=0;i<(int)s.size();i++)
        if(s[i]>='a' && s[i]<='z')r+=s[i];
    return r;
}
void hash(string s, string t){
    cout<<s<<" "<<t<<endl;
    int l=(int)s.size();
    FOR(i,0,l)mapa[s[i]]=t[i];
}
int main(){
    mapa['a'] = 'y';mapa['b'] = 'h';
    mapa['c'] = 'e';mapa['d'] = 's';mapa['e'] = 'o';mapa['f'] = 'c';
    mapa['g'] = 'v';mapa['h'] = 'x';mapa['i'] = 'd';mapa['j'] = 'u';
    mapa['k'] = 'i';mapa['l'] = 'g';mapa['m'] = 'l';mapa['n'] = 'b';
    mapa['o'] = 'k';mapa['p'] = 'r';mapa['r'] = 't';mapa['s'] = 'n';
    mapa['t'] = 'w';mapa['u'] = 'j';mapa['v'] = 'p';mapa['w'] = 'f';
    mapa['x'] = 'm';mapa['y'] = 'a';mapa['z'] = 'q';mapa['q'] = 'z';

    int n;
    string s;
    scanf("%d\n",&n);
    FOR(j,0,n){
        getline(cin,s);
        cout<<"Case #"<<j+1<<": ";
        for(int i=0;i<(int)s.size();i++){
            if(s[i]>='a' && s[i]<='z')cout<<mapa[s[i]];
            else cout<<s[i];
        }
        cout<<endl;
    }
    return 0;
}


