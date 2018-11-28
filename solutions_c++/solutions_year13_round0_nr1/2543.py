#include<iostream>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
    int cN;
    cin >> cN;
    char board[4][4];
    for(int ci=0; ci<cN; ++ci)
    {
        for(int row=0; row<4; ++row)
        {
            char input[80]={0};
            cin.getline(input, 80);
            if(strlen(input)==0)
            {
                --row;
                continue;
            }
            for(int c=0; c<4; ++c)
            {
                board[row][c]=input[c];
            }
        }        
        bool notComplete = false;
        bool won = false;
        //check row
        for(int row=0; row<4; ++row)
        {
            int c = 0;
            char p='?';
            //++c;
            for(; c<4; ++c)
            {
                p = board[row][c];
                if(p!='T')
                {
                    break;
                }
            }
            if(p=='.')
            {
                notComplete = true;
                continue;
            }
            bool allSame = true;
            for(; c<4; ++c)
            {
                char nt = board[row][c];
                if(nt!=p && nt!='T')
                {
                    allSame = false;
                    break;
                }
            }
            if(allSame)
            {
                won = true;
                printf("Case #%d: %c won\n", ci+1, p);
                break;
            }
        }
        if(won) continue;
        //check col
        for(int col=0; col<4; ++col)
        {
            int r = 0;
            char p='?';
            for(; r<4; ++r)
            {
                p = board[r][col];
                if(p!='T')
                {
                    break;
                }
            }
            if(p=='.')
            {
                notComplete = true;
                continue;
            }
            bool allSame = true;
            for(; r<4; ++r)
            {
                char nt = board[r][col];
                if(nt!=p && nt!='T')
                {
                    allSame = false;
                    break;
                }
            }
            if(allSame)
            {
                won = true;
                printf("Case #%d: %c won\n", ci+1, p);
                break;
            }
        }
        if(won) continue;
        //check diag left-up to right-buttom
        {
            int d = 0;
            char p = board[d][d];
            ++d;
            for(; d<4; ++d)
            {
                p = board[d][d];
                if(p!='T')
                {
                    break;
                }
            }
            if(p!='.')
            {
                bool allSame = true;
                for(; d<4; ++d)
                {
                    char nt = board[d][d];
                    if(nt!=p && nt!='T')
                    {
                        allSame = false;
                        break;
                    }
                }
                if(allSame)
                {
                    won = true;
                    printf("Case #%d: %c won\n", ci+1, p);
                }
            }
        }
        if(won) continue;
        //check diag left-buttom to right-up
        {
            int d = 0;
            char p = board[3-d][d];
            ++d;
            for(; d<4; ++d)
            {
                p = board[3-d][d];
                if(p!='T')
                {
                    break;
                }
            }
            if(p!='.')
            {
                bool allSame = true;
                for(; d<4; ++d)
                {
                    char nt = board[3-d][d];
                    if(nt!=p && nt!='T')
                    {
                        allSame = false;
                        break;
                    }
                }
                if(allSame)
                {
                    won = true;
                    printf("Case #%d: %c won\n", ci+1, p);
                }
            }
        }
        if(won) continue;
        if(notComplete)
        {
            printf("Case #%d: Game has not completed\n", ci+1);
        }
        else
        {
            printf("Case #%d: Draw\n", ci+1);
        }

    }
	return 0;
}

