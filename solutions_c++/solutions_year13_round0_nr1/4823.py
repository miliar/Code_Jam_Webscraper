#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

struct GCase
{
    int board[4][4];

    int finish(int xCnt, int yCnt)
    {
        //if (xCnt == 4 && yCnt == 4)
        //    return 3;
        if (xCnt == 4)
            return 1;
        if (yCnt == 4)
            return 2;
        return 0;
    }
    int checkWin()
    {
        bool bFull = true;
        for (int y = 0; y < 4; ++y)
        {
            int tCnt = 0;
            int oCnt = 0;
            for (int x = 0; x < 4; ++x)
            {
                switch(board[y][x])
                {
                case 0:
                    bFull = false;
                    break;
                case 1:
                    tCnt++;
                    break;
                case 2:
                    oCnt++;
                    break;
                case 3:
                    tCnt++;
                    oCnt++;
                    break;
                } 
            }
            int r = finish(tCnt, oCnt);
            if (r != 0)
                return r;
        }

        for (int y = 0; y < 4; ++y)
        {
            int tCnt = 0;
            int oCnt = 0;
            for (int x = 0; x < 4; ++x)
            {
                switch(board[x][y])
                {
                case 0:
                    bFull = false;
                    break;
                case 1:
                    tCnt++;
                    break;
                case 2:
                    oCnt++;
                    break;
                case 3:
                    tCnt++;
                    oCnt++;
                    break;
                } 
            }
            int r = finish(tCnt, oCnt);
            if (r != 0)
                return r;
        }

        {
            int tCnt = 0;
            int oCnt = 0;
            for (int x = 0; x < 4; ++x)
            {
                switch(board[x][x])
                {
                case 0:
                    bFull = false;
                    break;
                case 1:
                    tCnt++;
                    break;
                case 2:
                    oCnt++;
                    break;
                case 3:
                    tCnt++;
                    oCnt++;
                    break;
                } 
            }
            int r = finish(tCnt, oCnt);
            if (r != 0)
                return r;
        }
        {
            int tCnt = 0;
            int oCnt = 0;
            for (int x = 0; x < 4; ++x)
            {
                switch(board[x][3-x])
                {
                case 0:
                    bFull = false;
                    break;
                case 1:
                    tCnt++;
                    break;
                case 2:
                    oCnt++;
                    break;
                case 3:
                    tCnt++;
                    oCnt++;
                    break;
                } 
            }
            int r = finish(tCnt, oCnt);
            if (r != 0)
                return r;
        }

        if (bFull)
            return 3;
        return 0;
    }
};

int g_nCases = 0;
vector<GCase*> g_cases;

void read_input()
{
    cin >> g_nCases;
    for (int i = 0; i < g_nCases; ++i)
    {
        GCase* gc = new GCase;
        // do sth
        for (int y = 0; y < 4; ++y)
        {
            for (int x = 0; x < 4; ++x)
            {
                char ch;
                cin >> ch;
                switch (ch)
                {
                case '.':
                    gc->board[y][x] = 0;
                    break;
                case 'X':
                    gc->board[y][x] = 1;
                    break;
                case 'O':
                    gc->board[y][x] = 2;
                    break;
                case 'T':
                    gc->board[y][x] = 3;
                    break;
                }
            }
        }
        g_cases.push_back(gc);
    }
}

int main(int argc, char**argv)
{
    read_input();

    for (int i = 0; i < g_nCases; ++i)
    {
        //g_cases[i]->debugOutput();
        cout << "Case #" << i+1 << ": " ;
        int r = g_cases[i]->checkWin();
        switch(r)
        {
        case 0:
            cout << "Game has not completed" << endl;
            break;
        case 1:
            cout << "X won" << endl;
            break;
        case 2:
            cout << "O won" << endl;
            break;
        case 3:
            cout << "Draw" << endl;
            break;
        }
    }
    return 0;
}
