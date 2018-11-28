#include <iostream>
#include <string>
#include <vector>
using namespace std;

int value(char c)
{
    switch(c)
    {
        case '.':
            return 0;
        case 'X':
            return 1;
        case 'O':
            return 2;
        case 'T':
            return 3;
    }
    return -1;
}

int check(int c0, int c1, int c2, int c3)
{
    if (c0 == 1 && c1 == 1 && c2 == 1 && c3 == 1)
        return 1;
    if (c0 == 3 && c1 == 1 && c2 == 1 && c3 == 1)
        return 1;
    if (c0 == 1 && c1 == 3 && c2 == 1 && c3 == 1)
        return 1;
    if (c0 == 1 && c1 == 1 && c2 == 3 && c3 == 1)
        return 1;
    if (c0 == 1 && c1 == 1 && c2 == 1 && c3 == 3)
        return 1;
    
    if (c0 == 2 && c1 == 2 && c2 == 2 && c3 == 2)
        return 2;
    if (c0 == 3 && c1 == 2 && c2 == 2 && c3 == 2)
        return 2;
    if (c0 == 2 && c1 == 3 && c2 == 2 && c3 == 2)
        return 2;
    if (c0 == 2 && c1 == 2 && c2 == 3 && c3 == 2)
        return 2;
    if (c0 == 2 && c1 == 2 && c2 == 2 && c3 == 3)
        return 2;
    
    return 0;
}

int main (int argc, char * const argv[])
{
	freopen("input1.txt", "rt", stdin);
	freopen("output1.txt", "wt", stdout);
	
	int T;
	cin >> T;
	
    int board[4][4];
    
    for(int i = 0; i < T; i++)
    {
        char b0[5], b1[5], b2[5], b3[5];
        cin >> b0;
        cin >> b1;
        cin >> b2;
        cin >> b3;
        cin.get();
        
		bool finished = true;
        
		for (int j = 0; j < 4; j++)
        {
            board[0][j] = value(b0[j]);
            board[1][j] = value(b1[j]);
            board[2][j] = value(b2[j]);
            board[3][j] = value(b3[j]);
            
            if (board[0][j] == 0 || board[1][j] == 0 || board[2][j] == 0 || board[3][j] == 0)
                finished = false;
        }
        
        if (check(board[0][0], board[0][1], board[0][2], board[0][3]) == 1 ||
            check(board[1][0], board[1][1], board[1][2], board[1][3]) == 1 ||
            check(board[2][0], board[2][1], board[2][2], board[2][3]) == 1 ||
            check(board[3][0], board[3][1], board[3][2], board[3][3]) == 1 ||
            check(board[0][0], board[1][0], board[2][0], board[3][0]) == 1 ||
            check(board[0][1], board[1][1], board[2][1], board[3][1]) == 1 ||
            check(board[0][2], board[1][2], board[2][2], board[3][2]) == 1 ||
            check(board[0][3], board[1][3], board[2][3], board[3][3]) == 1 ||
            check(board[0][0], board[1][1], board[2][2], board[3][3]) == 1 ||
            check(board[0][3], board[1][2], board[2][1], board[3][0]) == 1)
        {
            cout << "Case #" << i+1 << ": X won" << endl;
            continue;
        }
        if (check(board[0][0], board[0][1], board[0][2], board[0][3]) == 2 ||
            check(board[1][0], board[1][1], board[1][2], board[1][3]) == 2 ||
            check(board[2][0], board[2][1], board[2][2], board[2][3]) == 2 ||
            check(board[3][0], board[3][1], board[3][2], board[3][3]) == 2 ||
            check(board[0][0], board[1][0], board[2][0], board[3][0]) == 2 ||
            check(board[0][1], board[1][1], board[2][1], board[3][1]) == 2 ||
            check(board[0][2], board[1][2], board[2][2], board[3][2]) == 2 ||
            check(board[0][3], board[1][3], board[2][3], board[3][3]) == 2 ||
            check(board[0][0], board[1][1], board[2][2], board[3][3]) == 2 ||
            check(board[0][3], board[1][2], board[2][1], board[3][0]) == 2)
        {
            cout << "Case #" << i+1 << ": O won" << endl;
            continue;
        }
        if (finished)
            cout << "Case #" << i+1 << ": Draw" << endl;
        else
            cout << "Case #" << i+1 << ": Game has not completed" << endl;
        
	}
	
	return 0;
}

