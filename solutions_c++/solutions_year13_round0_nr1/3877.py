#include<iostream>
#include<string>
#include<vector>
using namespace std;
int main() {
    int T,i,j,fx,fo,cnt,fo1,fx1,k;
    cin>>T;
    vector<string> v(4);
    for(k=1; k<=T; k++) {
        v.clear();
        cnt=0;
        for(i=0; i<4; i++) {
            cin>>v[i];
        }
        for(i=0; i<4; i++) {
            fo=fx=1;
            for(j=0; j<4; j++) {
                fo&=(v[i][j]=='O' || v[i][j]=='T');
                fx&=(v[i][j]=='X' || v[i][j]=='T');
                if(v[i][j]=='.') cnt=1;
            }
            if(fo || fx) {
                break;
            }
        }
        if(fo) {
            cout<<"Case #"<<k<<": O won\n";
            continue;
        }
        if(fx) {
            cout<<"Case #"<<k<<": X won\n";
            continue;
        }
        
        for(i=0; i<4; i++) {
            fo=fx=1;
            for(j=0; j<4; j++) {
                fo&=(v[j][i]=='O' || v[j][i]=='T');
                fx&=(v[j][i]=='X' || v[j][i]=='T');
                if(v[j][i]=='.') cnt=1;
            }
            if(fo || fx) {
                break;
            }
        }
        if(fo) {
            cout<<"Case #"<<k<<": O won\n";
            continue;
        }
        if(fx) {
            cout<<"Case #"<<k<<": X won\n";
            continue;
        }
        fo=fx=fo1=fx1=1;
        for(i=0; i<4; i++) {
            fo&=(v[i][i]=='O' || v[i][i]=='T');
            fx&=(v[i][i]=='X' || v[i][i]=='T');
            fo1&=(v[i][3-i]=='O' || v[i][3-i]=='T');
            fx1&=(v[i][3-i]=='X' || v[i][3-i]=='T');
            if(v[i][i]=='.') cnt=1;
        }
        if(fo || fo1) {
            cout<<"Case #"<<k<<": O won\n";
            continue;
        }
        if(fx || fx1) {
            cout<<"Case #"<<k<<": X won\n";
            continue;
        }
        if(cnt) {
            cout<<"Case #"<<k<<": Game has not completed\n";
        } else {
            cout<<"Case #"<<k<<": Draw\n";
        }
    }
    return 0;
}
