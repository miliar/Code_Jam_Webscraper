#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
    int T;
    cin>>T;
    for(int t=1; t<=T; t++) {
        vector< std::string > v(4);
        for(int i=0; i<4; i++) {
            cin>>v[i];
        }
        int res = 0;
        for(int i=0; i<4; i++) {
            int o=1, x=1;
            for(int j=0; j<4; j++) {
                if(v[i][j] != 'O' && v[i][j] != 'T') o=0;
                if(v[i][j] != 'X' && v[i][j] != 'T') x=0;
            }
            if(o) res = 1;
            if(x) res = 2;
        }
        for(int i=0; i<4; i++) {
            int o=1, x=1;
            for(int j=0; j<4; j++) {
                if(v[j][i] != 'O' && v[j][i] != 'T') o=0;
                if(v[j][i] != 'X' && v[j][i] != 'T') x=0;
            }
            if(o) res = 1;
            if(x) res = 2;
        }
        {
            int o=1, x=1;
            for(int i=0; i<4; i++) {
                if(v[i][i] != 'O' && v[i][i] != 'T') o=0;
                if(v[i][i] != 'X' && v[i][i] != 'T') x=0;
            }
            if(o) res = 1;
            if(x) res = 2;
        }
        {
            int o=1, x=1;
            for(int i=0; i<4; i++) {
                if(v[3-i][i] != 'O' && v[3-i][i] != 'T') o=0;
                if(v[3-i][i] != 'X' && v[3-i][i] != 'T') x=0;
            }
            if(o) res = 1;
            if(x) res = 2;
        }
        if(res == 0)
        {
            for(int i=0; i<4; i++) {
                for(int j=0; j<4; j++) {
                    if(v[i][j] == '.') res = 3;
                }
            }
        }
        cout<<"Case #"<<t<<": ";
        if(res==1) cout<<"O won\n";
        else if(res==2) cout<<"X won\n";
        else if(res==3) cout<<"Game has not completed\n";
        else cout<<"Draw\n";
    }
    return 0;
}