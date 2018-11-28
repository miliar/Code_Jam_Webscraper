#include<iostream>
#include<sstream>
#include<string>
using namespace std;

#define ll long long
bool isDiagonalSame(string *g){
    if(g[0][0] == 'T')
        return g[2][2]==g[1][1] && g[2][2]==g[3][3];
    if(g[1][1] == 'T')
        return g[2][2]==g[0][0] && g[2][2]==g[3][3];
    if(g[2][2] == 'T')
        return g[0][0]==g[1][1] && g[1][1]==g[3][3];
    if(g[3][3] == 'T')
        return g[0][0]==g[1][1] && g[2][2]==g[3][3];
    return (g[0][0] == g[1][1] && g[1][1] == g[2][2] && g[2][2] == g[3][3]);
}
bool isBackDiagonalSame(string *g){
    if(g[0][3] == 'T')
        return g[2][1]==g[1][2] && g[2][1]==g[3][0];
    if(g[1][2] == 'T')
        return g[2][1]==g[0][3] && g[2][1]==g[3][0];
    if(g[2][1] == 'T')
        return g[0][3]==g[1][2] && g[1][2]==g[3][0];
    if(g[3][0] == 'T')
        return g[0][3]==g[1][2] && g[2][1]==g[1][2];
    return (g[0][3] == g[1][2] && g[1][2] == g[2][1] && g[2][1] == g[3][0]);
}
bool isDotPresent(string *g){
    for(int i=0; i<4; i++)
    for(int j=0; j<4; j++)
    if(g[i][j] == '.')
        return true;
    return false;
}
bool isRowSame(int row, string* g){
    string s = g[row];
    if(s[0] == 'T')
        return s[2]==s[1] && s[2]==s[3];
    if(s[1] == 'T')
        return s[2]==s[0] && s[2]==s[3];
    if(s[2] == 'T')
        return s[0]==s[1] && s[1]==s[3];
    if(s[3] == 'T')
        return s[0]==s[1] && s[1]==s[2];
    return s[0]==s[1] && s[2]==s[1] && s[2]==s[3];
}
bool isColSame(int col, string* g){
    if(g[0][col] == 'T')
        return g[2][col]==g[1][col] && g[2][col]==g[3][col];
    if(g[1][col] == 'T')
        return g[2][col]==g[0][col] && g[2][col]==g[3][col];
    if(g[2][col] == 'T')
        return g[0][col]==g[1][col] && g[1][col]==g[3][col];
    if(g[3][col] == 'T')
        return g[0][col]==g[1][col] && g[1][col]==g[2][col];
    return g[0][col]==g[1][col] && g[2][col]==g[1][col] && g[2][col]==g[3][col];
}
int main()
{
    unsigned ts;
    cin>>ts;
    for(unsigned t=1; t<=ts; t++){
        //cout<<"DEBUG: started test case "<<t<<endl;
        string* g = new string[4];
        cin>>g[0]>>g[1]>>g[2]>>g[3];
        char winner = '\0';
        for(unsigned index=0; index<4; index++){
            if(isRowSame(index, g)){
                winner = ((g[index][0]=='T')?g[index][1]:g[index][0]);
                //cout<<"DEBUG: row "<<index<<" true with winner "<<winner<<"\n";
                break;
            }
            if(isColSame(index, g)){
                winner = g[0][index]=='T'?g[1][index]:g[0][index];
                //cout<<"DEBUG: col "<<index<<" true\n";
                break;
            }
            if(isDiagonalSame(g)){
                winner = g[0][0]=='T'?g[1][1]:g[0][0];
                //cout<<"DEBUG: Dia true\n";
                break;
            }
            if(isBackDiagonalSame(g)){
                winner = g[0][3]=='T'?g[2][1]:g[0][3];
                //cout<<"DEBUG: BackDia true\n";
                break;
            }
        }
        if(winner && winner != '.'){
            //stringstream ss;
            //ss<<winner + " won";
            //ans = ss.str();
            //cout<<"DEBUG: winner "<<winner<<" true. ans:"<<ans<<"\n";
            cout<<"Case #"<<t<<": "<<winner<<" won"<<endl;
        }else if(isDotPresent(g)){
            //cout<<"DEBUG: isDotPresent() true\n";
            cout<<"Case #"<<t<<": Game has not completed"<<endl;
        }else{
            cout<<"Case #"<<t<<": Draw"<<endl;
        }
        delete[] g;
    }
    return 0;
}
