#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int N, K;
char board[50][50];

bool isJoined(char c)
{
    for (int i = 0; i < N; ++i)
    {
        for (int j = 0; j <= N - K; ++j)
        {
            int matchH = true;
            int matchV = true;
            for (int k = 0; k < K; ++k)
            {
                if (board[i][j+k] != c)
                   matchH = false;
                if (board[j+k][i] != c)
                   matchV = false;
            }
            if (matchH || matchV)
                return true;
        }
    }
    for (int i = 0; i <= N - K; ++i)
    {
        for (int j = 0; j <= N - K; ++j)
        {
            int match1 = true;
            int match2 = true;
            int match3 = true;
            int match4 = true;
            for (int k = 0; k < K; ++k)
            {
                if (board[i+k][j+k] != c)
                   match1 = false;
                if (board[N-1-i-k][j+k] != c)
                   match2 = false;
                if (board[N-1-i-k][N-1-j-k] != c)
                   match3 = false;
                if (board[i+k][N-1-j-k] != c)
                   match4 = false;
            }
            if (match1 || match2 || match3 || match4)
                return true;
        }
    }
    return false;
}

int main()
{
    ifstream in("A.in");
    ofstream out("A.out");
    
    int T;
    in >> T;
    
    for (int tc = 1; tc <= T; ++tc)
    {
        in >> N >> K;
        for (int i = 0; i < N; ++i)
            for (int j = 0; j < N; ++j)
                in >> board[i][j];
        
        for (int i = 0; i < N; ++i)
        {
            int landIndex = N - 1;
            for (int j = N - 1; j >= 0; --j)
            {
                if (board[i][j] != '.')
                {
                    board[i][landIndex] = board[i][j];
                    landIndex--;
                }
            }
            for (; landIndex >= 0; --landIndex)
                board[i][landIndex] = '.';
        }
        
        bool redJoined = isJoined('R');
        bool blueJoined = isJoined('B');
        
        out << "Case #" << tc << ": ";
        if (redJoined)
        {
            if (blueJoined)
                out << "Both";
            else
                out << "Red";
        }
        else
        {
            if (blueJoined)
                out << "Blue";
            else
                out << "Neither";
        }
        out << endl;
    }
    
    in.close();
    out.close();
    return 0;
}
