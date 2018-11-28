#include <algorithm>  
#include <iostream>  
#include <iomanip>  
#include <fstream>  
#include <sstream>  
#include <string>  
#include <list>  
#include <queue>  
#include <set>  
#include <map>  
#include <cstdio>  
#include <cstdlib>  
#include <cctype>  
#include <cmath>  
using namespace std;  

#define FOR(i,a,b) for(long i=(a);i<(b);++i)  
#define REP(i,n) FOR(i,0,n)  

enum Result {
    XWON,
    OWON,
    DRAW,
    INC
};

Result checkRows(char board[4][4])
{
    bool anyIncomplete = false;
    REP(i,4)
    {
        char resChar = '?';
        REP(j,4)
        {
            if(resChar != board[i][j])
            {
                if(board[i][j] == '.')
                {
                    resChar = '.';
                    break;
                }
                else if(board[i][j] == 'T')
                {
                    continue;
                }
                else if(resChar == '?')
                {
                    resChar = board[i][j];
                }
                else 
                {
                    resChar = '?';
                    break;
                }
            }
        }
        if(resChar == 'X')
            return XWON;
        else if(resChar == 'O')
            return OWON;
        else if(resChar == '.')
            anyIncomplete = true;
    }
    return anyIncomplete ? INC : DRAW;
}

Result checkCols(char board[4][4])
{
    bool anyIncomplete = false;
    REP(j,4)
    {
        char resChar = '?';
        REP(i,4)
        {
            if(resChar != board[i][j])
            {
                if(board[i][j] == '.')
                {
                    resChar = '.';
                    break;
                }
                else if(board[i][j] == 'T')
                {
                    continue;
                }
                else if(resChar == '?')
                {
                    resChar = board[i][j];
                }
                else 
                {
                    resChar = '?';
                    break;
                }
            }
        }
        if(resChar == 'X')
            return XWON;
        else if(resChar == 'O')
            return OWON;
        else if(resChar == '.')
            anyIncomplete = true;
    }
    return anyIncomplete ? INC : DRAW;
}

Result checkDiags(char board[4][4])
{
    bool anyIncomplete = false;
    char resChar = '?';
    REP(i,4)
    {
        if(resChar != board[i][i])
        {
            if(board[i][i] == '.')
            {
                resChar = '.';
                break;
            }
            else if(board[i][i] == 'T')
            {
                continue;
            }
            else if(resChar == '?')
            {
                resChar = board[i][i];
            }
            else 
            {
                resChar = '?';
                break;
            }
        }
    }
    if(resChar == 'X')
        return XWON;
    else if(resChar == 'O')
        return OWON;
    else if(resChar == '.')
        anyIncomplete = true;

    resChar = '?';
    REP(i,4)
    {
        if(resChar != board[i][3-i])
        {
            if(board[i][3-i] == '.')
            {
                resChar = '.';
                break;
            }
            else if(board[i][3-i] == 'T')
            {
                continue;
            }
            else if(resChar == '?')
            {
                resChar = board[i][3-i];
            }
            else 
            {
                resChar = '?';
                break;
            }
        }
    }

    if(resChar == 'X')
        return XWON;
    else if(resChar == 'O')
        return OWON;
    else if(resChar == '.')
        anyIncomplete = true;
    
    return anyIncomplete ? INC : DRAW;

}

Result solveCase(char board[4][4])
{
    Result res = checkRows(board);
    cout << "Rows returned " << res << endl;
    if(res == DRAW or res == INC)
    {
        res = checkCols(board);
    cout << "cols returned " << res << endl;
    }
    if(res == DRAW or res == INC)
    {
        res = checkDiags(board);
    cout << "diag returned " << res << endl;
    }

    return res;
}

int main(int argc, char** argv)
{
    ifstream in;
    in.open("test.in",ios::in);
    ofstream out;
    out.open("test.out",ios::out);
    int N = 0;
    in>>N;
    cout << " Total  " << N <<endl;
    REP(caseN,N)
    {
        cout<<"solving case "<<caseN+1<<endl;
        char board[4][4];
        REP(i,4)
            REP(j,4)
            {
                char c;
                in >> c;

                board[i][j] = c;
            }


        Result res = solveCase(board);

        out << "Case #"<<caseN+1<<": ";

        switch(res)
        {
            case XWON : out << "X won"; break;
            case OWON : out << "O won"; break;
            case DRAW : out << "Draw"; break;
            case INC  : out << "Game has not completed"; break;
        }
        out << endl;
    }
        
    in.close();
    out.close();
    return 0;
}
