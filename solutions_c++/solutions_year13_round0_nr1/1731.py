#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
using namespace std;
int main() {
    freopen("inp.txt","r",stdin);
    freopen("out.txt","w",stdout);
    char mat[4][4];
    int t;
    cin >> t;
    for(int cases=1; cases<=t; cases++) {
        for(int i=0; i<4; i++) {
            for(int j=0; j<4; j++) {
                cin >> mat[i][j];
            }
        }
        cout << "Case #" << cases << ": ";
        int cnt=0;
        char winner;
        char res;
        int draw=-1;
        bool completed=true;
        for(int i=0; i<4; i++) for(int j=0; j<4; j++) if(mat[i][j]=='.') completed=false;
        for(int player=0; player<=1; player++) {

            winner='-';
            char c = (player==0)?'X':'O';
            //for all rows
            for(int i=0; i<4; i++) {
                cnt=0;
                for(int j=0; j<4; j++)
                    if(mat[i][j] == c || mat[i][j]=='T') cnt++;
                if(cnt==4) {
                    winner=c; break;
                }
            }
            //for all columns
            if(winner=='-')
                for(int i=0; i<4; i++) {
                    cnt=0;
                    for(int j=0; j<4; j++)
                        if(mat[j][i] == c || mat[j][i]=='T') cnt++;
                    if(cnt==4) {
                        winner=c; break;
                    }
                }
            /*for \ */
            if(winner=='-') {
                cnt=0;
                for(int i=0; i<4; i++) {
                    if(mat[i][i]==c || mat[i][i]=='T') cnt++;
                    if(cnt==4) {
                        winner=c; break;
                    }
                }
            }
            /*for / */
            if(winner=='-') {
                cnt=0;
                for(int i=0; i<4; i++) {
                    if(mat[i][3-i]==c || mat[i][3-i]=='T') cnt++;
                    if(cnt==4) {
                        winner=c; break;
                    }
                }
            }

            if(winner=='X' || winner=='O') {
                res=winner;
                draw++;
            }
        }
        if(draw==-1 && completed) {
            cout << "Draw\n";
        }
        else if(draw==0) {
            cout << res << " won\n";
        }
        else
            cout << "Game has not completed\n";
    }
    return 0;
}
