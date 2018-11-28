#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <cctype>
#include <cstring>
#include <string>

using namespace std;

int T,t;

int check(char x, char map[][5])
{
    for (int i = 0; i<=3; i++){
        if (map[i][0]==x || map[i][0]=='T'){
            int flag = 1;
            for (int j = 1; j<=3; j++){
                if (map[i][j]!=x && map[i][j]!='T'){
                    flag = 0; break;
                }
            }
            if (flag) return 1;
        }
    }
    
    for (int j = 0; j<=3; j++){
        if (map[0][j]==x || map[0][j]=='T'){
            int flag = 1;
            for (int i = 1; i<=3; i++){
                if (map[i][j]!=x && map[i][j]!='T'){
                    flag = 0; break;
                }
            }
            if (flag) return 1;
        }
    }
    
    int flag = 1;
    for (int i = 0; i<=3; i++){
        if (map[i][i]!=x && map[i][i]!='T'){
            flag = 0; break;
        }
    }
    if (flag) return 1;
    flag = 1;
    for (int i = 0; i<=3; i++){
        if (map[i][3-i]!=x && map[i][3-i]!='T'){
            flag = 0; break;
        }
    }
    if (flag) return 1;
    return 0;
}

int main()
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    cin>>T;
    while (t<T){
        t++;
        char map[5][5]={0};
        int empty = 0;
        for (int i = 0; i<4; i++){
            cin>>map[i];
            while (strlen(map[i])<4) cin>>map[i];
            if (strstr(map[i],".")) empty = 1;
        }
        string ans;
        if (check('O',map)) ans = "O won";
        else if (check('X',map)) ans = "X won";
        else if (!empty) ans = "Draw";
        else ans = "Game has not completed";
        cout<<"Case #"<<t<<": "<<ans<<endl;
    }
    fclose(stdin);
    fclose(stdout);
}
