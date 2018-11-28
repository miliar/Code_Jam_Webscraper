#include <iostream>
using namespace std;
char a[4][4];
bool testrow(char c1,char c2,char c3, char c4){
    if ( (c1 == 'T' && c2 == c3 && c3 == c4)||
        (c2=='T' && c1==c3 && c3== c4)||
        (c3=='T' && c1==c2 && c2==c4)||
        (c4=='T' && c1==c2 && c2==c3)||
        (c1==c2 && c2==c3 && c3==c4))
    return true;
    return false;
}
int test(){
    bool completeness = true;
    for (int i = 0; i < 4; ++i){
        for (int j = 0; j < 4; ++j){
            if (a[i][j]=='.'){
                completeness = false;
            }
        }
    }
    for (int i = 0; i < 4; ++i){
        if (a[i][0]!='.'){
            bool result = testrow(a[i][0],a[i][1],a[i][2],a[i][3]);
            if (result){
                if (a[i][0]=='X'|| a[i][1]=='X'){
                    return 2;
                }
                else return 1;
            }
        }
    }
    for (int j = 0; j < 4; ++j){
        if (a[0][j]!='.'){
            bool result = testrow(a[0][j],a[1][j],a[2][j],a[3][j]);
            if (result){
                if (a[0][j]=='X'|| a[1][j]=='X'){
                    return 2;
                }
                else return 1;
            }
        }
    }
    if (a[0][0]!='.'){
        bool result = testrow(a[0][0],a[1][1],a[2][2],a[3][3]);
        if (result){
            if (a[0][0]=='X'|| a[1][1]=='X'){
                return 2;
            }
            else return 1;
        }
    }
    if (a[0][3]!='.'){
        bool result = testrow(a[0][3],a[1][2],a[2][1],a[3][0]);
        if (result){
            if (a[0][3]=='X'|| a[1][2]=='X'){
                return 2;
            }
            else return 1;
        }
    }
    if (completeness){
        return 3;
    }
    return 0;
}

int main(){
    int t;
    cin >> t;
    for (int tcount=1;tcount<=t;++tcount){
        for (int i = 0; i < 4; ++i){
            for (int j = 0; j < 4; ++j){
                cin >> a[i][j];
            }
        }
        
        int ans = test();
        cout << "Case #"<< tcount<<": ";
        switch (ans){
            case 0: cout << "Game has not completed\n";
            break;
            case 1: cout << "O won\n";
            break;
            case 2: cout << "X won\n";
            break;
            case 3: cout << "Draw\n";
            break;
        }
    }

    
}
