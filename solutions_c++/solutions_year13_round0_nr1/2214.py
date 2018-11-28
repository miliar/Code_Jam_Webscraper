#include <iostream>
#include <fstream>

#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <string>

#include <algorithm>
#include <functional>
#include <sstream>
#include <utility>

#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>

using namespace std;

typedef vector<int>     vi;
typedef pair<int,int>   ii;
typedef vector<ii>      vii;
typedef long long       ll;
typedef set<int>        si;
typedef map<string,int> msi;

#define sz(a)   int((a).size())
#define all(c)  (c).begin(),(c).end()
#define pb(a)      push_back(a);
#define rep(i,n)    for(int i(0);i<int(n);i++)
#define TRvi(c,it)  for(vi::iterator it=(c).begin();it!=(c).end();it++)
#define INF 2E9

vector<char> a(4);
vector<vector<char> > board(4,a);

bool Xpred(char c)
{
    return (c!='.' && c!='O');
}

bool Opred(char c)
{
    return (c!='.' && c!='X');
}

bool Xwon(){
    //Rows
    rep(i,4)
    if(Xpred(board[i][0]) && Xpred(board[i][1]) && Xpred(board[i][2]) && Xpred(board[i][3]))    return true;
    //Columns
    rep(i,4)
    if(Xpred(board[0][i]) && Xpred(board[1][i]) && Xpred(board[2][i]) && Xpred(board[3][i]))    return true;
    //Diagonals
    if(Xpred(board[0][0]) && Xpred(board[1][1]) && Xpred(board[2][2]) && Xpred(board[3][3]))    return true;
    if(Xpred(board[3][0]) && Xpred(board[2][1]) && Xpred(board[1][2]) && Xpred(board[0][3]))    return true;
    return false;
}

bool Owon(){
    //Rows
    rep(i,4)
    if(Opred(board[i][0]) && Opred(board[i][1]) && Opred(board[i][2]) && Opred(board[i][3]))    return true;
    //Columns
    rep(i,4)
    if(Opred(board[0][i]) && Opred(board[1][i]) && Opred(board[2][i]) && Opred(board[3][i]))    return true;
    //Diagonals
    if(Opred(board[0][0]) && Opred(board[1][1]) && Opred(board[2][2]) && Opred(board[3][3]))    return true;
    if(Opred(board[3][0]) && Opred(board[2][1]) && Opred(board[1][2]) && Opred(board[0][3]))    return true;
    return false;
}

bool isFull()
{
    rep(i,4)
        rep(j,4)
        if(board[i][j]=='.')    return false;
    return true;
}

int main()
{
    ifstream cin("A-large.in");
    ofstream cout("out.txt");

    int T;
    cin>>T;
    rep(i,T){
        cout<<"Case #"<<i+1<<": ";
        rep(i,4)
            rep(j,4){
                char c; cin>>c;
                board[i][j]=c;
            }
        /*rep(i,4){
            rep(j,4){
                cout<<board[i][j];
            }
            cout<<endl;
        }*/
        if(Xwon())  cout<<"X won"<<endl;
        else if(Owon()) cout<<"O won"<<endl;
        else if(isFull())   cout<<"Draw"<<endl;
        else                cout<<"Game has not completed"<<endl;
    }

    return 0;
}
