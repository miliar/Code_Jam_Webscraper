#include <iostream>
#include <cstdio>
#include <vector>
#include <list>
#include <string>
#include <numeric>
#include <map>
#include <cstring>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
using namespace std;

int T;
char S[101];
map<char, char> m;

void init(){
    m['a'] =  'y';
    m['b'] = 'h';
    m['c'] = 'e';
    m['d'] = 's';
    m['e'] = 'o';
    m['f'] = 'c';
    m['g'] = 'v';
    m['h'] = 'x';
    m['i'] = 'd';
    m['j'] = 'u';
    m['k'] = 'i';
    m['l'] = 'g';
    m['m'] = 'l';
    m['n'] = 'b';
    m['o'] = 'k';
    m['p'] = 'r';
    m['q'] = 'z';
    m['r'] = 't';
    m['s'] ='n';
    m['t'] = 'w';
    m['u'] = 'j';
    m['v'] = 'p';
    m['w'] = 'f';
    m['x'] = 'm';
    m['y'] = 'a';
    m['z'] = 'q';
}

void getResult(){
    for(int i=0;i<strlen(S);i++){
        if(S[i] == ' '){
            cout<<" ";
        }
        else{
            cout<<m[S[i]];
        }
    }
    cout<<endl;

}


int main(){
    freopen("A.in","r",stdin);
    //freopen("test.out","w",stdout);

    init();
    cin>>T;
    char tmp[10];
    gets(tmp);
    for(int Case=1;Case<T+1;Case++){
        cout<<"Case #"<<Case<<": ";
        gets(S);
        getResult();
    }
    return 0;
}
