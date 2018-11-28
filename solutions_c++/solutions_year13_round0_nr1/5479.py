#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <fstream>
using namespace std;
typedef long long ll;
typedef vector<int> vint;
typedef pair<int, int> pint;
#define INF 1000000000 //10^9
#define MOD 1000000007 //10^9+7
#define REP(i,a,b) for(int i=a;i<b;i++)
#define QSORT(a) sort(a.begin(),a.end());

string isWin(vector<string> board){
    bool win=0;
    string res="";
    
    //横
    for (int i=0; i<4; i++) {
        win=1;
        res=board[i][0];
        for (int j=0; j<4; j++) {
            if (board[i][j]!=board[i][0]) {
                win=0;
                break;
            }
        }
        if (win)return res;
    }
    
    
    //縦
    for (int i=0; i<4; i++) {
        win=1;
        res=board[0][i];
        for (int j=0; j<4; j++) {
            if (board[j][i]!=board[0][i]) {
                win=0;
                break;
            }
        }
        if (win)return res;
    }
    
    
    
    //ななめ１
    
    win=1;
    res=board[0][0];
    
    for (int i=0; i<4; i++) {
        if (board[i][i]!=board[0][0]) {
                win=0;
                break;
        }
        
    }
    if (win)return res;
    
    
    
    //ななめ２
    win=1;
    res=board[0][3];
    
    for (int i=0; i<4; i++) {
        if (board[i][3-i]!=board[0][3]) {
            win=0;
            break;
        }
        
    }
    if (win)return res;
    
    
    
    return "";
}

int main(){
    
    FILE* fin= freopen("/Users/w_shunn/Desktop/A-small-attempt1.in.txt", "r", stdin);
    
    FILE* fout= freopen("/Users/w_shunn/Desktop/output.txt", "w", stdout);
    
    
    int T;
    cin>>T;
    
    for (int a=1; a<=T; a++) {
        
        string board[4];
        
        for (int i=0; i<4; i++) {
            cin>>board[i];
        }
        
        vector<string>bx(4),bo(4);
        
        
        bool bl=0;
        for (int i=0; i<4; i++) {
            bx[i]=bo[i]=board[i];
            for (int j=0; j<4; j++) {
                if (board[i][j]=='.') bl=1;
                if (bx[i][j]=='T')bx[i][j]='X';
                if (bo[i][j]=='T')bo[i][j]='O';
                
            }
        }
        
        
        printf("Case #%d: ",a);
        if (isWin(bx)=="X") printf("X won\n");
        else if (isWin(bo)=="O") printf("O won\n");
        else if (bl) printf("Game has not completed\n");
        else printf("Draw\n");
        
    }
    
    fclose(fin);
    fclose(fout);
    
    
    return 0;
}
