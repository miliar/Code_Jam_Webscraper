#include <iostream>
#include <fstream>
using namespace std;
enum ResultT{O_win,X_win,Draw,The_game_not_complete};
ResultT JudgeResult(char*);

int main(int argc,char* argv[])
{
    ifstream fin(argv[1]);
    ofstream fout("output.txt");
    int counter=0;
    fin>>counter;
    char* chessboard=new char[16];
    for(int i=0;i<counter;i++)
    {
        for(int j=0;j<16;j++)
        {
            fin>>chessboard[j];
        }
        ResultT result=JudgeResult(chessboard);
        fout<<"Case #"<<(i+1)<<": ";
        switch(result)
        {
            case O_win:
            {
                fout<<"O won"<<endl;
                break;
            }
            case X_win:
            {
                fout<<"X won"<<endl;
                break;
            }
            case Draw:
            {
                fout<<"Draw"<<endl;
                break;
            }
            default:
            {
                fout<<"Game has not completed"<<endl;
            }
        }
    }
    return 0;
}

ResultT JudgeResult(char* cb)
{
    ResultT result;
    for(int round=0;round<4;round++)
    {
        if(cb[round*4]=='.'||cb[round*4+1]=='.'||cb[round*4+2]=='.'||cb[round*4+3]=='.')
            continue;
        if(cb[round*4]==cb[round*4+1]&&cb[round*4]==cb[round*4+2]&&cb[round*4]==cb[round*4+3]&&cb[round*4]!='T')
        {
            if(cb[round*4]=='X')
                result=X_win;
            else if(cb[round*4]=='O')
                result=O_win;
            return result;
        }
        if(cb[round*4]=='T'&&cb[round*4+1]==cb[round*4+2]&&cb[round*4+1]==cb[round*4+3]&&cb[round*4+1]!='T')
        {
            if(cb[round*4+1]=='X')
                result=X_win;
            else if(cb[round*4+1]=='O')
                result=O_win;
            return result;
        }
        if(cb[round*4+1]=='T'&&cb[round*4]==cb[round*4+2]&&cb[round*4]==cb[round*4+3]&&cb[round*4]!='T')
        {
            if(cb[round*4]=='X')
                result=X_win;
            else if(cb[round*4]=='O')
                result=O_win;
            return result;
        }
        if(cb[round*4+2]=='T'&&cb[round*4]==cb[round*4+1]&&cb[round*4]==cb[round*4+3]&&cb[round*4]!='T')
        {
            if(cb[round*4]=='X')
                result=X_win;
            else if(cb[round*4]=='O')
                result=O_win;
            return result;
        }
        if(cb[round*4+3]=='T'&&cb[round*4]==cb[round*4+1]&&cb[round*4]==cb[round*4+2]&&cb[round*4]!='T')
        {
            if(cb[round*4]=='X')
                result=X_win;
            else if(cb[round*4]=='O')
                result=O_win;
            return result;
        }
    }
    for(int round=0;round<4;round++)
    {
        if(cb[round]=='.'||cb[round+4]=='.'||cb[round+8]=='.'||cb[round+12]=='.')
            continue;
        if(cb[round]==cb[round+4]&&cb[round]==cb[round+8]&&cb[round]==cb[round+12])
        {
            if(cb[round]=='X')
            {
                result=X_win;
                return result;
            }
            else if(cb[round]=='O')
            {
                result=O_win;
                return result;
            }
            else continue;
        }
        if(cb[round]=='T'&&cb[round+4]==cb[round+8]&&cb[round+4]==cb[round+12])
        {
            if(cb[round+4]=='X')
                result=X_win;
            else if(cb[round+4]=='O')
                result=O_win;
            return result;
        }
        if(cb[round+4]=='T'&&cb[round]==cb[round+8]&&cb[round]==cb[round+12])
        {
            if(cb[round]=='X')
                result=X_win;
            else if(cb[round]=='O')
                result=O_win;
            return result;
        }
        if(cb[round+8]=='T'&&cb[round]==cb[round+4]&&cb[round]==cb[round+12])
        {
            if(cb[round]=='X')
                result=X_win;
            else if(cb[round]=='O')
                result=O_win;
            return result;
        }
        if(cb[round+12]=='T'&&cb[round]==cb[round+4]&&cb[round]==cb[round+8])
        {
            if(cb[round]=='X')
                result=X_win;
            else if(cb[round]=='O')
                result=O_win;
            return result;
        }
    }
    for(int i=0;i<2;i++)
    {
        if(!i)
        {
            if(cb[0]=='.'||cb[5]=='.'||cb[10]=='.'||cb[15]=='.')
                continue;
            if(cb[0]==cb[5]&&cb[0]==cb[10]&&cb[0]==cb[15])
            {
                if(cb[0]=='X')
                    result=X_win;
                else if(cb[0]=='O')
                     result=O_win;
                return result;
            }
            if(cb[0]=='T'&&cb[5]==cb[10]&&cb[5]==cb[15])
            {
                if(cb[5]=='X')
                    result=X_win;
                else if(cb[5]=='O')
                    result=O_win;
                return result;
            }
            if(cb[5]=='T'&&cb[0]==cb[10]&&cb[0]==cb[15])
            {
                if(cb[0]=='X')
                    result=X_win;
                else if(cb[0]=='O')
                    result=O_win;
                return result;
            }
            if(cb[10]=='T'&&cb[0]==cb[5]&&cb[0]==cb[15])
            {
                if(cb[0]=='X')
                    result=X_win;
                else if(cb[0]=='O')
                    result=O_win;
                return result;
            }
            if(cb[15]=='T'&&cb[0]==cb[5]&&cb[0]==cb[10])
            {
                if(cb[0]=='X')
                    result=X_win;
                else if(cb[0]=='O')
                    result=O_win;
                return result;
            }
        }
        else
        {
            if(cb[3]=='.'||cb[6]=='.'||cb[9]=='.'||cb[12]=='.')
                continue;
            if(cb[3]==cb[6]&&cb[3]==cb[9]&&cb[3]==cb[12])
            {
                if(cb[3]=='X')
                    result=X_win;
                else if(cb[3]=='O')
                     result=O_win;
                return result;
            }
            if(cb[3]=='T'&&cb[6]==cb[9]&&cb[6]==cb[12])
            {
                if(cb[6]=='X')
                    result=X_win;
                else if(cb[6]=='O')
                    result=O_win;
                return result;
            }
            if(cb[6]=='T'&&cb[3]==cb[9]&&cb[3]==cb[12])
            {
                if(cb[3]=='X')
                    result=X_win;
                else if(cb[3]=='O')
                    result=O_win;
                return result;
            }
            if(cb[9]=='T'&&cb[3]==cb[6]&&cb[3]==cb[12])
            {
                if(cb[3]=='X')
                    result=X_win;
                else if(cb[3]=='O')
                    result=O_win;
                return result;
            }
            if(cb[12]=='T'&&cb[3]==cb[6]&&cb[3]==cb[9])
            {
                if(cb[3]=='X')
                    result=X_win;
                else if(cb[3]=='O')
                    result=O_win;
                return result;
            }
        }
    }
    for(int i=0;i<16;i++)
    {
        if(cb[i]=='.')
        {
            result=The_game_not_complete;
            return result;
        }
    }
    result=Draw;
    return result;
}

