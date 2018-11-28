#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int main()
{
    ios::sync_with_stdio(0);

    freopen("in.in", "r", stdin);
    freopen("out.out", "w", stdout);
    char arr[5][6];
    int Test; cin >> Test;

    for (int i=1; i<=Test; ++i){
        int T=0, X=0, D=0, O=0, chk=1; char s[10];

        for (int j=1; j<=4; ++j){
            T=0; X=0; O=0; cin >> s;
            for (int k=1; k<=4; ++k){
                arr[j][k]=s[k-1];
                if (arr[j][k]==84)T++;
                else if (arr[j][k]==79)O++;
                else if (arr[j][k]==88)X++;
                else if (arr[j][k]==46) D++;
            }
            if (T+X==4 && chk) {cout << "Case #" << i << ": " << "X won\n"; chk=0;}
            else if (T+O==4 && chk) {cout << "Case #" << i << ": " << "O won\n"; chk=0;}
        }

        for (int j=1; j<=4; ++j){
            T=0; X=0; O=0;
            for (int k=1; k<=4; ++k){
                if (arr[k][j]==84)T++;
                else if (arr[k][j]==79)O++;
                else if (arr[k][j]==88)X++;
                else if (arr[k][j]==46) D++;
            }
            if (T+X==4 && chk) {cout << "Case #" << i << ": " << "X won\n"; chk=0;}
            else if (T+O==4 && chk) {cout << "Case #" << i << ": " << "O won\n"; chk=0;}
        }

        if (chk){
        T=0; X=0; O=0;
        for(int j=1; j<=4; ++j){
            if (arr[j][j]==84)T++;
            else if (arr[j][j]==79)O++;
            else if (arr[j][j]==88)X++;
            else if(arr[j][j]==46)D++;
        }
        if (T+X==4) {cout << "Case #" << i << ": " << "X won\n"; chk=0;}
        else if (T+O==4) {cout << "Case #" << i << ": " << "O won\n"; chk=0;}

        T=0; X=0; O=0;
        for(int j=1; j<=4; ++j){
            if (arr[j][5-j]==84)T++;
            else if (arr[j][5-j]==79)O++;
            else if (arr[j][5-j]==88)X++;
            else if(arr[j][5-j]==46) D++;
        }
        if (T+X==4) {cout << "Case #" << i << ": " << "X won\n"; chk=0;}
        else if (T+O==4) {cout << "Case #" << i << ": " << "O won\n"; chk=0;}
        }

        if (chk){
            if (D>0){cout << "Case #" << i << ": " << "Game has not completed\n";}
            else if(D==0) {cout << "Case #" << i << ": " << "Draw\n";}
        }
    }
    return 0;
}
