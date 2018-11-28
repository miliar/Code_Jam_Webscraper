#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <string>
#include <cstring>
#include <cmath>
#include <functional>
#include <set>
using namespace std;
#define foreach(x,v) for( typeof(v.begin()) x = v.begin(); x != v.end(); x++)
#define For(i,n) for(int i = 0; i < n; i++)
#define pf printf
#define sc scanf
#define pb push_back

string answ(vector<string> b){
    
    int Or = 0, Xr = 0, T = 0, points = 0;
    For(i,4){
        Or = 0, Xr = 0, T = 0;
        For(j,4){
            
            if(b[i][j] == 'X')Xr++;
            else if(b[i][j] == 'O') Or++;
            else if(b[i][j] == 'T') T++;
            else if(b[i][j] == '.')points++;
        }

        if(Xr == 3 && T == 1 || Xr == 4) return "X won";
        else if(Or == 3 && T == 1 || Or == 4) return "O won";
    }

    For(i,4){
        Or = 0, Xr = 0, T = 0;
        For(j,4){
            
            if(b[j][i] == 'X')Xr++;
            else if(b[j][i] == 'O') Or++;
            else if(b[j][i] == 'T') T++;

        }

        if(Xr == 3 && T == 1 || Xr == 4) return "X won";
        else if(Or == 3 && T == 1 || Or == 4) return "O won";
    }
    
    Or = 0, Xr = 0, T = 0;
    
    For(i,4){
            if(b[i][i] == 'X')Xr++;
            else if(b[i][i] == 'O') Or++;
            else if(b[i][i] == 'T') T++;

    }

    if(Xr == 3 && T == 1 || Xr == 4) return "X won";
    else if(Or == 3 && T == 1 || Or == 4) return "O won";
    
    Or = 0, Xr = 0, T = 0;
    For(i,4){
            if(b[i][3-i] == 'X')Xr++;
            else if(b[i][3-i] == 'O') Or++;
            else if(b[i][3-i] == 'T') T++;

    }

    if(Xr == 3 && T == 1 || Xr == 4) return "X won";
    else if(Or == 3 && T == 1 || Or == 4) return "O won";
    
    if(points == 0) return "Draw";
    else return "Game has not completed";
}
int main (int argc, char const* argv[])
{
    int T;
    scanf("%d\n", &T);
    For(cases,T){
        string line;
        vector<string> board;
        while(true){
            getline(cin,line);
            if(line == "") break;
            board.pb(line);
        }
        
        pf("Case #%d: %s\n",cases+1,answ(board).c_str());
    }
    return 0;
}
