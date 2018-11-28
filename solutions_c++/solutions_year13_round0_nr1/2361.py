#include<iostream>
#include<cstdio>

using namespace std;

char a[100][100];

bool ok(char c) {
    bool flag;
    for(int i=0; i<4; i++) {
        flag=false;
        for(int j=0; j<4; j++)
            if ((a[i][j] != c) && (a[i][j] != 'T')) {flag = true;  break;}
        if (!flag) return true;
    }
    for(int j=0; j<4; j++) {
        flag=false;
        for(int i=0; i<4; i++)
            if ((a[i][j] != c) && (a[i][j] != 'T')) {flag = true;  break;}
        if (!flag) return true;
    }
    flag = false;
    for(int i=0; i<4; i++)
        if (a[i][i] != c && a[i][i] != 'T') { flag = true; break;}
    if (!flag) return true;
    flag = false;
    for(int i=0; i<4; i++)
        if (a[i][3-i] != c && a[i][3-i] != 'T') { flag = true; break;}
    if (!flag) return true;
    return false;
}
int main() {
    int ntest;
    
    freopen("a.in", "r", stdin);
    freopen("a.txt", "w", stdout);
    scanf("%d", &ntest);
    for(int test=0; test<ntest; test++) {
        cout << "Case #" << test+1 << ": ";
        for(int i=0; i<4; i++)
            scanf("%s", &a[i]);
        if (ok('X')) 
            cout << "X won";
        else    
        if (ok('O'))
            cout << "O won";
        else {
            bool check = true;
            for(int i=0; i<4; i++)
                for(int j=0;j<4; j++)
                    if (a[i][j] == '.') {
                        check = false;
                        break;
                    }
            if (!check)
                cout << "Game has not completed";
            else    
                cout << "Draw";
        }
        cout << endl;
    }
    
    return 0;
}
