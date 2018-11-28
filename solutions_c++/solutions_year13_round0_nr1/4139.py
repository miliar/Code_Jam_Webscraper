#include <iostream>
using namespace std;

#if 0
#define INPUT_FILE  "A-small.in.txt"
#define OUTPUT_FILE "A-small.out.txt"
#else
#define INPUT_FILE  "A-large.in.txt"
#define OUTPUT_FILE "A-large.out.txt"
#endif


void scorePoint(char c, int &xcount, int &ocount)
{
    if (c == 'O')
        ocount++;
    else if (c == 'X')
        xcount++;
    else if (c == 'T')
    {
        xcount++;
        ocount++;
    }
}

int main(int argc, const char * argv[])
{
    freopen(INPUT_FILE, "r", stdin);
	freopen(OUTPUT_FILE, "w+", stdout);
    
    char board [16];
    int T, t;
    
    scanf("%i\n", &T);
    
    // For each test case
    for (t = 0; t < T; t++)
    {
        bool boardFull = true;
        int ocount, xcount;
        
        for (int i = 0; i<16; i++)
        {
            scanf("%c\n",&board[i]);
            if (board[i]=='.') boardFull = false;
        }
        
        // Check rows
        for (int r=0; r<4; r++)
        {
            xcount = 0;
            ocount = 0;
            for (int c=0; c<4; c++)
            {
                scorePoint(board[r*4+c], xcount, ocount);
            }
            if (xcount == 4 || ocount == 4) goto resolve;
        }
        
        // Check colums
        for (int c=0; c<4; c++)
        {
            xcount = 0;
            ocount = 0;
            for (int r=0; r<4; r++)
            {
                scorePoint(board[r*4+c], xcount, ocount);
            }
            if (xcount == 4 || ocount == 4) goto resolve;
        }
                
        // Check diagonals
        xcount = 0;
        ocount = 0;
        for (int i=0; i<4; i++)
        {
            scorePoint(board[i*4+i], xcount, ocount);
        }
        if (xcount == 4 || ocount == 4) goto resolve;
  
        xcount = 0;
        ocount = 0;
        for (int i=0; i<4; i++)
        {
            scorePoint(board[i*4+(3-i)], xcount, ocount);
        }
        
    resolve:
        cout << "Case #" << t+1 << ": ";
        
        if (xcount == 4)
            cout << "X won";
        else if (ocount == 4)
            cout << "O won";
        else if (boardFull)
            cout << "Draw";
        else
            cout << "Game has not completed";
        
		cout << endl;
    }
    return 0;
}