#include<iostream>
#include<istream>
#include<vector>
#include<string>
#include<bitset>
#include<algorithm>
#include<sstream>
#include<map>
#include<set>
#include<cmath>
#include<stack>
#include<queue>
#include<cstdio>
using namespace std;

string calc(vector<string>game){
    //case 0 will check this
    for(int row=0;row<4;++row){
            char rowCheck=game[row][0];
            int col=0,col1=3;
            for(col=1;col<4;++col){
                    if(rowCheck==game[row][col] || game[row][col]=='T')continue;
                    else break;
            }
            char rowCheck1=game[row][3];
            for(col1=2;col1>=0;--col1){
                    if(rowCheck1==game[row][col1] || game[row][col1]=='T')continue;
                    else break;
            }
            //cout<<"col1: "<<col1<<endl;
            if(col==4){
                       if(rowCheck=='X')return "X won";
                       if(rowCheck=='O')return "O won";
                       }
            if(col1<0){
                       if(rowCheck1=='X')return "X won";
                       if(rowCheck1=='O')return "O won";
                       }
    }
    //case 3 will check this
    for(int col=0;col<4;++col){
            char colCheck=game[0][col];
             char colCheck1=game[3][col];
            int row=0,row1=3;
            for(row=1;row<4;++row){
                    if(colCheck==game[row][col] || game[row][col]=='T')continue;
                    else break;
            }
            for(row1=2;row1>=0;--row1){
                    if(colCheck1==game[row1][col] || game[row1][col]=='T')continue;
                    else break;
            }
             //cout<<"row1: "<<row1<<endl;
            if(row==4){
                       if(colCheck=='X')return "X won";
                       if(colCheck=='O')return "O won";
                       }
            if(row1<0){
                       if(colCheck1=='X')return "X won";
                       if(colCheck1=='O')return "O won";
                       }
    }
    char diagonal=game[0][0];
    char diagonal1=game[0][3];
    char diagonal2=game[3][3];
    char diagonal3=game[3][0];
    int d=0,d1=0,d2=2,d3=2;
    for(d2=2;d2>=0;--d2){
              if(diagonal2!=game[d2][d2] && game[d2][d2]!='T')break;            
    }
    if(d2<0){
              if(diagonal2=='X')return "X won";
                       if(diagonal2=='O')return "O won";
    }
    for(d3=1;d3<4;++d3){
             if(diagonal3!=game[3-d3][d3] && game[3-d3][d3]!='T')break;           
    }
    if(d3==4){
              if(diagonal3=='X')return "X won";
                       if(diagonal3=='O')return "O won";
    }
    for(d=1;d<4;++d){
             if(diagonal!=game[d][d] && game[d][d]!='T')break;
    }
    if(d==4){
                       if(diagonal=='X')return "X won";
                       if(diagonal=='O')return "O won";
    }
    for(d1=1;d1<4;++d1){
             if(diagonal1!=game[d1][3-d1] && game[d1][3-d1]!='T')break;
    }
    if(d1==4){
                       if(diagonal1=='X')return "X won";
                       if(diagonal1=='O')return "O won";
    }
    for(int row=0;row<4;++row){
            for(int col=0;col<4;++col){
                    if(game[row][col]=='.')return "Game has not completed";
            }
    }
    return "Draw";
}

int main()
{
    int t;
    cin>>t;
    string s;
    getline(cin,s);
    for(int i=0;i<t;++i){
            vector<string>game;
            for(int j=0;j<4;++j){
                    getline(cin,s);   
                    game.push_back(s);
            }
            cout<<"Case #"<<i+1<<": "<<calc(game)<<endl;
           getline(cin,s);
    }
    return 0;
}
