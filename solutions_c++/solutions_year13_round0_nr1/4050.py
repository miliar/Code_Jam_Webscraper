#include <algorithm>
#include <bitset>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>
#include <sstream>

using namespace std;

#define pb push_back
int x,y;

int main()
{
    freopen("/Users/anujkumar/Desktop/cdcdc/test/test/ip.in","r",stdin);
    freopen("/Users/anujkumar/Desktop/cdcdc/test/test/anuj.out","w",stdout);
    int t;
    cin>>t;
    int cseno = 0;
    string s[4];
    while(t--){
        cseno++;
        for(x=0;x<4;x++)
            cin>>s[x];
        int X =1;
        int Y = 1;
        for(x =0 ; x< 4;x++) {
            X=1;
            Y=1;
            for(y=0;y<4;y++){
                if(s[x][y]=='O'||s[x][y]=='.')
                    X=0;
                if(s[x][y]=='X'||s[x][y]=='.')
                    Y=0;
            }
            if(X==1) {
                cout<<"Case #"<<cseno<<": X won\n";
                x = 4;
            }
            if(Y==1) {
                cout<<"Case #"<<cseno<<": O won\n";
                x = 4;
            }
        }
        if(x==5)
            continue;
        X=1;
        Y=1;
        for(x =0 ; x< 4;x++) {
            X=1;
            Y=1;
            for(y=0;y<4;y++){
                if(s[y][x]=='O'||s[y][x]=='.')
                    X=0;
                if(s[y][x]=='X'||s[y][x]=='.')
                    Y=0;
            }
            if(X==1) {
                cout<<"Case #"<<cseno<<": X won\n";
                x = 4;
            }
            if(Y==1) {
                cout<<"Case #"<<cseno<<": O won\n";
                x = 4;
            }
        }
        if(x==5)
            continue;
        X=1;
        Y=1;
        for(x=0;x<4;x++){
            if(s[x][x]=='O'||s[x][x]=='.')
            {X=0;}
            if(s[x][x]=='X'||s[x][x]=='.')
            {Y=0;}
        }
        if(X==1) {
            cout<<"Case #"<<cseno<<": X won\n";
            x = 5;
        }
        if(Y==1) {
            cout<<"Case #"<<cseno<<": O won\n";
            x = 5;
        }
        if(x==5)
            continue;
        X=1;
        Y=1;
        for(x=0;x<4;x++){
            if(s[3-x][x]=='O'||s[3-x][x]=='.')
            {
                X=0;
            }
            if(s[3-x][x]=='X'||s[3-x][x]=='.')
            {
                Y=0;
            }
        }
        if(X==1) {
            cout<<"Case #"<<cseno<<": X won\n";
            x = 5;
        }
        if(Y==1) {
            cout<<"Case #"<<cseno<<": O won\n";
            x = 5;
        }
        if(x==5)
            continue;
        for(x=0;x<4;x++)
            for(y=0;y<4;y++)
            {
                if(s[x][y]=='.')
                {
                    cout<<"Case #"<<cseno<<": Game has not completed\n";
                    x=4,y=4;
                }
            }
        if(x==5)continue;
        cout<<"Case #"<<cseno<<": Draw\n";
    }
    return 0;
}