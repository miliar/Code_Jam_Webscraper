#include <iostream>
#include <vector>
#include <string>
#include <sstream>


using namespace std;

bool check(string game[4], char P);
bool check1(string game[4], int col, char P);
bool check2(string game[4], int wier, char P);
bool check3(string game[4], char P);
bool check4(string game[4], char P);
bool isDraw(string game[4]);


int main()
{
    string game[4];
    
    int T;
    cin>>T;
    for(int i = 0; i < T; ++i)
    {
        ostringstream ss;
        ss << i+1;
        cout<<"Case #"<<ss.str()<<": ";
        
        for(int j = 0; j<4 ; ++j)
            cin>>game[j];
        
        if(check(game, 'X'))
             cout<<"X won\n";
        else if(check(game, 'O'))
             cout<<"O won\n";
        else if(isDraw(game))
             cout<<"Draw\n";
        else cout<<"Game has not completed\n";
    }
    
    
    return 0;   
}

bool check(string game[4], char P)
{
    for(int i = 0; i < 4; ++i)
        if(check1(game, i, P))
            return true;
            
    for(int i = 0; i < 4; ++i)
        if(check2(game, i, P))
            return true;
            
    if(check3(game, P))
        return true;
    if(check4(game, P))
        return true;
    
    return false;   
}

bool check1(string game[4], int col, char P)
{
    for(int j = 0; j < 4 ; ++j)
        if(game[col][j] != P && game[col][j]!='T')
            return false;
    
    return true;
}

bool check2(string game[4], int wier, char P)
{
    for(int j = 0; j < 4 ; ++j)
        if(game[j][wier] != P && game[j][wier]!='T')
            return false;
    
    return true;
}

bool check3(string game[4], char P)
{
    for(int i = 0; i < 4; ++i)
        if(game[i][i] != P && game[i][i]!='T')
            return false;
    
    return true;
}

bool check4(string game[4], char P)
{
    for(int i = 0; i < 4; ++i)
        if(game[i][3-i] != P && game[i][3-i]!='T')
            return false;
    
    return true;
}

bool isDraw(string game[4])
{
    for(int i = 0; i < 4; ++i)
        for(int j = 0; j < 4; ++j)
            if(game[i][j] == '.')
                return false;
    
    return true;
}
