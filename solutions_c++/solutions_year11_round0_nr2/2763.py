// Magicka
#include <iostream>
#include <list>
#include <vector>
#include <map>
#include <assert.h>
#include <stdio.h>
#include <memory.h>
using namespace std;

int readint() {
    int x;
    cin >> x;
    return x;
}

int abs(int x) {
    return (x > 0) ? x : -x;
}
int max(int x, int y) {
    return (x > y) ? x : y;
}

#define ZEROMEM(X) memset(X, 0, sizeof(X));

char cdata[0x10000];
char ddata[0x10000];

int makekey(int a, int b) {
    return a * 0x100 + b;
}

char setcombine(int a,int b, int c) {
    cdata[ makekey(a,b)] = c;
    cdata[ makekey(b,a)] = c;
}

void setdelete(int a,int b) {
    ddata[ makekey(a,b)] = 1;
    ddata[ makekey(b,a)] = 1;
}

int dodelete(char a,char b) {
    return ddata[ makekey(a,b) ];
}

char combine(char a,char b) {
    return cdata[ makekey(a,b) ];
}

string addletter( const string & str, char ch )
{
    size_t l = str.length();
    if (l==0) {
        string result = "A";
        result[0]=ch;
        return result;
    }else {
        char prevChar = str[ l - 1 ];

        char x= combine(prevChar, ch );
        if (x!=0) {
            return addletter( str.substr(0, l -1 ), x );
        }

        for(int i = 0;i<l;i++) {
            if (dodelete(ch, str[i]))
                return "";
        }

        string temp = "A";
        temp[0]= ch;
        return str + temp;
    }
}
int main() {
    int T = readint();
    for(int t=0;t<T; t++) {
        ZEROMEM(cdata);
        ZEROMEM(ddata);
        int C = readint();
        for(int i = 0; i<C; i++) {
            string S;
            cin >> S;
            // cout << "Comb: "<< S << endl;
            setcombine( S[0], S[1], S[2] );
        }

        int D = readint();
        for(int i = 0; i<D; i++) {
            string S;
            cin >> S;
            // cout << "D: "<< S << endl;
            setdelete( S[0], S[1] );
        }
        int N = readint();

        string S;
        cin >> S;
        // cout << "N: "<< S << endl;

        string result;

        if (N>0) {
            result = "";

            for(int i =0; i< N; i++) {
                result = addletter( result, S[i] );
            }
        }

        cout << "Case #" << t+1 << ": [" ;
        for(int i = 0; i<result.length(); i++) {
            if (i)
                cout << ", ";
            cout << result[i];
        }
        cout << "]" << endl;
    }
    return 0;
}
