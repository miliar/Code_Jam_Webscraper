#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <iterator>
#include <cmath>
#include <queue>
#include <algorithm>

using namespace std;

int main(){
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int n;
    cin >> n;
    for (int rt=1;rt<=n;rt++){
        string s[4];
        for (int i=0;i<4;i++) cin>>s[i];
        bool O=0,X=0;
        for (int i=0;i<4;i++){
            bool flag=true;
            for (int j=0;j<4;j++)
                if (s[i][j]=='.'||s[i][j]=='X') flag=false;
            if (flag) O=true;
        }
        for (int i=0;i<4;i++){
            bool flag=true;
            for (int j=0;j<4;j++)
                if (s[i][j]=='.'||s[i][j]=='O') flag=false;
            if (flag) X=true;
        }
        
        for (int i=0;i<4;i++){
            bool flag=true;
            for (int j=0;j<4;j++)
                if (s[j][i]=='.'||s[j][i]=='X') flag=false;
            if (flag) O=true;
        }
        for (int i=0;i<4;i++){
            bool flag=true;
            for (int j=0;j<4;j++)
                if (s[j][i]=='.'||s[j][i]=='O') flag=false;
            if (flag) X=true;
        }
        
       
        bool flag=true;
        for (int i=0;i<4;i++)
            if (s[i][i]=='.'||s[i][i]=='X') flag=false;
        if (flag) O=true;
        
        flag=true;
        for (int i=0;i<4;i++)
            if (s[i][i]=='.'||s[i][i]=='O') flag=false;
        if (flag) X=true;
        
        flag=true;
        for (int i=0;i<4;i++)
            if (s[i][4-i-1]=='.'||s[i][4-i-1]=='X') flag=false;
        if (flag) O=true;
        
        flag=true;
        for (int i=0;i<4;i++)
            if (s[i][4-i-1]=='.'||s[i][4-i-1]=='O') flag=false;
        if (flag) X=true;
        
        bool comp=true;
        for (int i=0;i<4;i++)
            for (int j=0;j<4;j++)
                if (s[i][j]=='.') comp=false;
        
        printf("Case #%d: " ,rt);
        if (X){
            cout << "X won" << endl;
        }else if (O){
            cout << "O won" << endl;
        }else if (comp) {
            cout << "Draw" << endl;
        }else {
            cout << "Game has not completed" << endl;
        }
    }
}
