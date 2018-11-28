#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <bitset>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>

#define FOR(k,x,n) for(int k=x;k<n;k++)
#define SORT(x) sort(x.begin(),x.end())

using namespace std;
vector<string> board;bool isfull();
int checkR(int x,int y);
int checkL(int x,int y);
int checkU(int x,int y);
int checkD(int x,int y);
int diag1(int x,int y);
int diag2(int x,int y);
int diag3(int x,int y);
int diag4(int x,int y);
int main()
{
    ios_base::sync_with_stdio(false);

    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);

    int tests,cases=1;
    cin>>tests;

    for(int k=0;k<tests;k++){
    board.clear();
    int x=0,zero=0,maxx=0,maxz=0;bool full=false;

    for(int i=0;i<4;i++)
    {
        string s;
        cin>>s;
        board.push_back(s);
    }
        for(int h=0;h<4;h++)
        for(int y=0;y<4;y++){

        if(board[h][y]=='X'){
        int val=checkL(h,y);
        if(val >maxx ) maxx=val;
        val=checkD(h,y);
        if(val >maxx ) maxx=val;
        val=checkU(h,y);
        if(val >maxx ) maxx=val;
        val=checkR(h,y);
        if(val >maxx ) maxx=val;
        val=diag1(h,y);
        if(val >maxx ) maxx=val;
        val=diag2(h,y);
        if(val >maxx ) maxx=val;
        val=diag3(h,y);
        if(val >maxx ) maxx=val;
        val=diag4(h,y);
        if(val >maxx ) maxx=val;

        }
        if(board[h][y]=='O'){
        int val=checkL(h,y);
        if(val >maxz ) maxz=val;
        val=checkD(h,y);
        if(val >maxz ) maxz=val;
        val=checkU(h,y);
        if(val >maxz ) maxz=val;
        val=checkR(h,y);
        if(val >maxz ) maxz=val;
        val=diag1(h,y);
        if(val >maxz ) maxz=val;
        val=diag2(h,y);
        if(val >maxz ) maxz=val;
        val=diag3(h,y);
        if(val >maxz ) maxz=val;
        val=diag4(h,y);
        if(val >maxz ) maxz=val;

        }


        }

    //isfull();
   // if(!isfull() ) cout<<"NO FULL"<<endl;
    if(maxz==4 && maxx <4)cout<<"Case #"<<cases<<": "<<"O won";
    else if(maxx==4 && maxz <4)cout<<"Case #"<<cases<<": "<<"X won";
    else if(!isfull() && maxz <=4 && maxx <=4)cout<<"Case #"<<cases<<": "<<"Game has not completed";
    else if(isfull() && maxz <4 && maxx<4) cout<<"Case #"<<cases<<": "<<"Draw";

    cases++;
    //cout<<" "<<maxx<<" "<<maxz<<endl;
    cout<<endl;

    }

    return 0;
}

int checkL(int x,int y){

    int c=0;

    for(int i=y;i>=0;i--){

    if(i>=0 && i<4 && (board[x][i]==board[x][y] ||board[x][i]=='T'  )  )
        c++;
    else return c;

    }
    return c;

}
int checkR(int x,int y){

    int c=0;

    for(int i=y;i<4;i++){

    if(i>=0 && i<4 && (board[x][i]==board[x][y]||board[x][i]=='T'  )  )
        c++;
    else return c;

    }
    return c;

}
int checkU(int x, int y){

    int c=0;

    for(int i=x;i>=0;i--){

    if(i>=0 && i<4 && (board[i][y]==board[x][y] ||board[x][i]=='T'  ) )
        c++;
    else return c;

    }
    return c;

}
int checkD(int x, int y){


    int c=0;

    for(int i=x;i<4;i++){

    if(i>=0 && i<4 && (board[i][y]==board[x][y] ||board[x][i]=='T'  ))
        c++;
    else return c;

    }
    return c;

}
int diag1(int x, int y){


    int c=1;

    if(x+1 <4 && y+1 <4)
    if( board[x+1][y+1] == board[x][y]|| board[x+1][y+1]=='T' )c++;
    if(x+2 <4 && y+2 <4)
    if( board[x+2][y+2] == board[x][y]|| board[x+2][y+2]=='T' )c++;
    if(x+3 <4 && y+3 <4)
    if(board[x+3][y+3] == board[x][y]|| board[x+3][y+3]=='T' )c++;


    return c;

}
int diag2(int x, int y){

   int c=1;

    if(x-1 >=0 && y-1 >=0)
    if(board[x-1][y-1] == board[x][y]|| board[x-1][y-1]=='T' )c++;
    if(x-2 >=0 && y-2 >=0)
    if(board[x-2][y-2] == board[x][y]|| board[x-2][y-2]=='T' )c++;
    if(x-3 >=0 && y-3 >=0)
    if(board[x-3][y-3] == board[x][y]|| board[x-3][y-3]=='T' )c++;

    return c;

}
int diag3(int x, int y){

   int c=1;

    if(x-1 >=0 && y+1 <4)
    if(board[x-1][y+1] == board[x][y]|| board[x-1][y+1]=='T' )c++;
    if(x-2 >=0 && y+2 <4 )
    if(board[x-2][y+2] == board[x][y]|| board[x-2][y+2]=='T' )c++;
    if(x-3 >=0 && y+3 <4)
    if(board[x-3][y+3] == board[x][y]|| board[x-3][y+3]=='T' )c++;

    return c;

}
int diag4(int x, int y){

   int c=1;

    if(x+1 <4 && y-1 >=0)
    if(board[x+1][y-1] == board[x][y]|| board[x+1][y-1]=='T' )c++;
    if(x+2 <4 && y-2 >=0)
    if(board[x+2][y-2] == board[x][y]|| board[x+2][y-2]=='T' )c++;
    if(x+3 <4&&  y-3 >=0)
    if(board[x+3][y-3] == board[x][y]|| board[x+3][y-3]=='T' )c++;

    return c;

}

bool isfull(){
int c=0;

for(int k=0;k<4;k++)
    for(int i=0;i<4;i++){
    if(board[k][i]!='X'&&board[k][i]!='O'&&board[k][i]!='T')
    return false;
    }

return true;
}
