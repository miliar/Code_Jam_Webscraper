#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <utility>
#include <sstream>
#include <iomanip>
#include <list>

using namespace std;
#define deb(a) cout<<#a<<":"<<a<<endl;

char c[] = {'X', 'O'};
int main() {
    string ln;
    int T;
    
    cin>>T;
    getline(cin, ln);
    
    for(int t=1; t<=T; t++) {
        vector<string> v;
        string res;
        
        for(int i=0; i<4; i++) {
            getline(cin, ln);
            v.push_back(ln);
        }
        
        getline(cin, ln);
        
        int i=0;
        int j=0;
        for(; i<4; i++) {
            for(; j<4; j++) {
                if(v[i][j]=='.') {break;}
            }
            if(j!=4) {break;}
        }
        
        if((i!=4) || (j!=4)) {
            res = "Game has not completed";
        } else {
            res = "Draw";
        }
        
        for(int i=0; i<2; i++) {
            for(int a=0; a<4; a++) {
                
                int b=0;
                for(; b<4; b++) {
                    if( !(v[a][b]=='T' || v[a][b]==c[i]) ) {break;}
                }
                if(b==4) {
                    res = (c[i]=='X')?"X won":"O won";
                    break;
                }
                
                b = 0;
                for(; b<4; b++) {
                    if( !(v[b][a]=='T' || v[b][a]==c[i]) ) {break;}
                }
                if(b==4) {
                    res = (c[i]=='X')?"X won":"O won";
                    break;
                }
            }
            
            int a=0;
            for(; a<4; a++) {
                if( !(v[a][a]=='T' || v[a][a]==c[i]) ) {break;}
            }
            if(a==4) {
                res = (c[i]=='X')?"X won":"O won";
                break;
            }
            
            a=0;
            for(; a<4; a++) {
                if( !(v[a][3-a]=='T' || v[a][3-a]==c[i]) ) {break;}
            }
            if(a==4) {
                res = (c[i]=='X')?"X won":"O won";
            }
        }
        
        cout<<"Case #"<<t<<": "<<res<<endl;
    }
    
    return 0;
}