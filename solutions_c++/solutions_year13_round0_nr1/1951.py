
#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <set>

using namespace std;

int rotate_integer( int target, int biggest_power_of_ten )
{
    int low_digit = target%10;
    return (target/10) + low_digit*biggest_power_of_ten;
    
}

struct set_of_four
{
    char pos[4];
};

int is_winner( set_of_four* current_set, char possible_winner )
{
    int answer = 1;
    for (int i=0; i<4; i++)
    {
        if ((current_set->pos[i] != possible_winner) && 
            (current_set->pos[i] != 'T'))
        {
            answer = 0;
            break;
        }
    }
    return answer;
}

char get_winner( set_of_four* current_set )
{
    // Check for 'X' winning
    if (is_winner( current_set, 'X' ))
    {
        return 'X';
    }
    // Check for 'O' winning
    if (is_winner( current_set, 'O' ))
    {
        return 'O';
    }
    return '.';

}

int main( int argc, char ** argv )
{
    fstream input_file;
    input_file.open( argv[1] );
    int num_cases;
    input_file >> num_cases;

   
    char current_grid[4][4];
    //string current_string;
    // Eat the line that had the number of lines
    //getline( input_file, current_string );

    for (int i=0; i<num_cases; i++)
    {
        // Read it in
        for (int j=0; j<4; j++)
        {
            for (int k=0; k<4; k++)
            {
                input_file >> current_grid[j][k];
            }
        }

        // Check the rows
        char winner = '.';
        for (int j=0; j<4; j++)
        {
            set_of_four current_row;
            for (int k=0; k<4; k++)
            {
                current_row.pos[k] = current_grid[j][k];
            }

            winner = get_winner( &current_row );
            if (winner != '.')
            {
                break;
            }
        }

        // Check the columns
        if (winner == '.')
        {
            for (int j=0; j<4; j++)
            {
                set_of_four current_col;
                for (int k=0; k<4; k++)
                {
                    current_col.pos[k] = current_grid[k][j];
                }
    
                winner = get_winner( &current_col );
                if (winner != '.')
                {
                    break;
                }
            }
        }

        // Check the diagonals
        if (winner == '.')
        {
            set_of_four first_diagonal;
            for (int j=0; j<4; j++)
            {
                first_diagonal.pos[j] = current_grid[j][j];
            }
            winner = get_winner( &first_diagonal );
        }
        if (winner == '.')
        {
            set_of_four second_diagonal;;
            for (int j=0; j<4; j++)
            {
                second_diagonal.pos[j] = current_grid[j][3-j];
            }
            winner = get_winner( &second_diagonal );
        }

        cout << "Case #" << i+1 << ": ";
        if (winner == 'X')
        {
            cout << "X won" << endl;
        }
        else if (winner == 'O')
        {
            cout << "O won" << endl;
        }
        else if (winner == '.')
        {
            // Check for draw
            int is_draw = 1;
            for (int j=0; j<4; j++)
            {
                for (int k=0; k<4; k++)
                {
                    if (current_grid[j][k] == '.')
                    {
                        is_draw = 0;
                        break;
                    }
                }
                if (!is_draw)
                {
                    break;
                }
            }   
            if (is_draw)
            {
                cout << "Draw" << endl;
            }
            else
            {
                cout << "Game has not completed" << endl;
            }
        }

        //char A, B;
        //input_file >> A >> B;
        //cout << current_grid[0][0] << " " << current_grid[3][3] << endl;
    }

    input_file.close();

    return 0;

}
