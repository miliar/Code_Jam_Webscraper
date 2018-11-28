#include <iostream>
#include <limits>
#include <string>

std::string winner_from_score(const int score)
{
    switch(score)
    {
        case 3:
        case 4:
            return "X won";
        case -3:
        case -4:
            return "O won";
    }
    return "";
}

std::string calc_result(const int board[])
{
    //Winning row?
    for(int r=0 ; r<4 ; ++r)
    {
        int row_val = board[r*4]+board[r*4+1]+board[r*4+2]+board[r*4+3];
        std::string winner = winner_from_score(row_val);
        if(winner!="") { return winner; }
    }

    //Winning col?
    for(int c=0 ; c<4 ; ++c)
    {
        int col_val = board[c]+board[c+4]+board[c+8]+board[c+12];
        std::string winner = winner_from_score(col_val);
        if(winner!="") { return winner; }
    }

    //Winning diags?
    {
        int diag_val = board[0]+board[5]+board[10]+board[15];
        std::string winner = winner_from_score(diag_val);
        if(winner!="") { return winner; }
    }
    {
        int diag_val = board[3]+board[6]+board[9]+board[12];
        std::string winner = winner_from_score(diag_val);
        if(winner!="") { return winner; }
    }

    //Board full?
    int board_tot = 0;
    for(int i=0 ; i<16 ; ++i) { board_tot += board[i]; }
    if(board_tot < 900) { return "Draw"; }

    return "Game has not completed";
}

int main()
{
    int N;
    std::cin >> N;
    ++N;//test cases are indexed from 1

    //now ingore the rest of the line inc newline, eases some tests that
	//try to read a line at a time (and stick on this \n if not removed)
    std::cin.ignore( std::numeric_limits<std::streamsize>::max() , '\n' );

    for( int test_case=1 ; test_case<N ; ++test_case )
    {
    //Prep
        int board[16];

        for(int r=0 ; r<4 ; ++r)
        {
            std::string row;

            std::cin >> row;

            for(int c=0 ; c<4 ; ++c)
            {
                switch(row[c])
                {
                case 'X':
                    board[r+c*4] = 1;
                    break;
                case 'O':
                    board[r+c*4] = -1;
                    break;
                case 'T':
                    board[r+c*4] = 0;
                    break;
                case '.':
                    board[r+c*4] = 1000;
                    break;
                }
            }
        }

    //Work
        std::cout << "Case #" << test_case << ": " << calc_result(board) << std::endl;

    //Clean Up
    }
}
