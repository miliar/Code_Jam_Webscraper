#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>
#define sz(X) ((int)X.size())
#define FOR(i,x,y) for(int i=x; i<y; ++i)

using namespace std;

bool check(char player, vector<string> &board)
{
    vector<string> pboard = board;
    string HWin(4,player);
    FOR(i,0,4)FOR(j,0,4)if(board[i][j] == 'T'){pboard[i][j] = player; break;}
    //H
    FOR(i,0,4)if(pboard[i] == HWin)return true;

    //V
    vector<int> v(4,0);
    FOR(i,0,4)FOR(j,0,4)if(pboard[i][j] == player)++v[j];
    FOR(i,0,4)if(v[i]==4)return true;

    //D
    int dCount = 0;
    FOR(i,0,4)FOR(j,0,4)if(i==j && pboard[i][j] == player) ++dCount;
    if(dCount == 4) return true;

    //D
    if(pboard[0][3] == player && pboard[1][2] == player && pboard[2][1] == player && pboard[3][0] == player) return true;

    return false;

}
string status(vector<string> &board)
{
    FOR(i,0,4) FOR(j,0,4) if(board[i][j] == '.')return "Game has not completed";
    return "Draw";
}
int main()
{
    ifstream cin ("input.txt");
    ofstream cout ("output.txt");

    int T;
    cin>>T;
    vector<string> board(4);
    FOR(i,1,T+1)
    {
        FOR(j,0,4)cin>>board[j];
        string ans = "";
        if(check('X', board)) ans = "X won";
        else if(check('O', board)) ans = "O won";
        else ans = status(board);
        cout<<"Case #"<<i<<": "<<ans<<endl;
    }
    return 0;
}