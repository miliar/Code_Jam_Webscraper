using namespace std;

#include <iostream>
#include <string>
#include <cstdlib>
#include <cctype>
#include <fstream>

int main()
{
    ifstream in;
    in.open ("A-large.in");
    ofstream out;
    out.open ("A-large.out");
    int n, count, xs, os, j, k;
    in >> n;
    char board[4][4], ch;
    in.get(ch);
    string result = "", response[4] = {"Game has not completed", "X won", "O won", "Draw"};

    for(int i = 0; i < n; i++)
    {
        result = "";
        count = 0;
        for(j = 0; j < 4; j++)
        {
            for(k = 0; k < 4; k++)
            {
                in.get(ch);
                if(ch != '\n')
                {
                    board[j][k] = ch;
                    if(ch == '.')
                        count++;
                }
            }
            in.get(ch);
        }

        for(j = 0; j < 4; j++)
        {
            xs = 0;
            os = 0;
            for(k = 0; k < 4; k++)
            {
                if(board[j][k] == 'X')
                    xs++;
                if(board[j][k] == 'O')
                    os++;
            }
            if((xs == 3 && (board[j][0] == 'T' || board[j][1] == 'T' || board[j][2] == 'T' || board[j][3] == 'T')) || xs == 4)
                {result = response[1]; break;}
            if((os == 3 && (board[j][0] == 'T' || board[j][1] == 'T' || board[j][2] == 'T' || board[j][3] == 'T')) || os == 4)
                {result = response[2]; break;}
        }

        for(j = 0; j < 4; j++)
        {
            xs = 0;
            os = 0;
            for(k = 0; k < 4; k++)
            {
                if(board[k][j] == 'X')
                    xs++;
                if(board[k][j] == 'O')
                    os++;
            }
            if((xs == 3 && (board[0][j] == 'T' || board[1][j] == 'T' || board[2][j] == 'T' || board[3][j] == 'T')) || xs == 4)
                {result = response[1]; break;}
            if((os == 3 && (board[0][j] == 'T' || board[1][j] == 'T' || board[2][j] == 'T' || board[3][j] == 'T')) || os == 4)
                {result = response[2]; break;}
        }

        xs = 0;
        os = 0;
        for(j = 0; j < 4; j++)
        {
            for(k = 0; k < 4; k++)
                if(j == k)
                {
                    if(board[j][k] == 'X')
                        xs++;
                    if(board[j][k] == 'O')
                        os++;
                }
        }
            if((xs == 3 && (board[0][0] == 'T' || board[1][1] == 'T' || board[2][2] == 'T' || board[3][3] == 'T')) || xs == 4)
                {result = response[1];}
            if((os == 3 && (board[0][0] == 'T' || board[1][1] == 'T' || board[2][2] == 'T' || board[3][3] == 'T')) || os == 4)
                {result = response[2];}

        xs = 0;
        os = 0;
        for(j = 0; j < 4; j++)
        {
            for(k = 0; k < 4; k++)
                if(j + k == 3)
                {
                    if(board[j][k] == 'X')
                        xs++;
                    if(board[j][k] == 'O')
                        os++;
                }
        }
            if((xs == 3 && (board[0][3] == 'T' || board[1][2] == 'T' || board[2][1] == 'T' || board[3][0] == 'T')) || xs == 4)
                {result = response[1];}
            if((os == 3 && (board[0][3] == 'T' || board[1][2] == 'T' || board[2][1] == 'T' || board[3][0] == 'T')) || os == 4)
                {result = response[2];}

        if(result == "")
        {
            if(count == 0)
                result = response[3];
            else
                result = response[0];
        }

        out << "Case #" << i+1 << ": " << result << endl;
        in.get(ch);
    }

    in.close();
    out.close();

    return 0;
}
