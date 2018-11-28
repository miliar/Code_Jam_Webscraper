#include <iostream>
#include <conio.h>
#include <stdio.h>
#include <string>
#include <sstream>


using namespace std;

#define REP(i,n) for(int i=0, _n = n; i < _n; i++) 

//abcdefghijklmnopqrstuvwxyz
char _decode['z' - 'a' + 1] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 
                          'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w',
                          'j', 'p', 'f', 'm', 'a', 'q'};

char decode(char x) {
     if (x == ' ') return x;
     return _decode[x-'a'];
}

int main() {
    string s;
    int count = 0;
    getline(cin,s);    
    istringstream sin(s);
    int n;
    sin >> n;
    while(count < n) {
        getline(cin,s);
        REP(i,s.size()) {
            s[i] = decode(s[i]);
        }
        count++;
        printf("Case #%d: %s\n",count,s.c_str());
    }
    //system("pause");
    return 0;
}
