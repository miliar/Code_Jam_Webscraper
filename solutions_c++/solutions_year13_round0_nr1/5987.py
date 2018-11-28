#include <iostream>
#include <fstream>

using namespace std;

ofstream fout;

int sum_diag(int grid[4][4])
{
    int sum = 0;
    for (int i=0;i<4;++i)
        sum += grid[i][i];
    return sum;
}

int sum_rev_diag(int grid[4][4])
{
    return (grid[0][3] + grid[1][2] + grid[2][1] + grid[3][0]);
}

int sum_row(int grid[4][4], int n)
{
    int sum = 0;
    for (int i=0;i<4;++i)
        sum += grid[n][i];
    return sum;
}

int sum_col(int grid[4][4], int n)
{
    int sum = 0;
    for (int i=0;i<4;++i)
        sum += grid[i][n];
    return sum;
}

void print_won(int sum, int &won)
{
    if (sum == 4 || sum == 53)
    {
        fout << "X won";
        won = 1;
    }
    else if (sum == 40 || sum == 80)
    {
        fout << "O won";
        won = 1;
    }
}

void print_draw(int grid[4][4])
{
    for (int i=0;i<4;++i)
        for (int j=0;j<4;++j)
            if (grid[i][j] == 0)
            {
                fout << "Game has not completed";
                return;
            }
    fout << "Draw";
}

int main()
{
    ifstream fin;
    fin.open("A-large.in");
    if (!fin.is_open())
    {
        cout << "Error in Opening Input file ";
        return -1;
    }
    fout.open("A-large.out");
    int num_cases;

    int grid[4][4];

    fin >> num_cases;
    for (int n=0;n<num_cases;++n)
    {
        fout << "Case #" << n+1 << ": ";

        char a;
        for (int i=0;i<4;++i)
        {
            for (int j=0;j<4;++j)
            {
                fin >> a;
                if (a == 'X')
                    grid[i][j] = 1;
                else if (a == 'O')
                    grid[i][j] = 10;
                else if (a == 'T')
                    grid[i][j] = 50;
                else
                    grid[i][j] = 0;
            }
        }

        int won = 0;
        int sum = 0;
        for (int i=0;i<4;++i)
        {
            if (won == 1)
                break;
            sum = sum_row(grid, i);
            print_won(sum, won);
        }
        for (int i=0;i<4;++i)
        {
            if (won == 1)
                break;
            sum = sum_col(grid, i);
            print_won(sum, won);
        }
        if (won == 0)
        {
            sum = sum_diag(grid);
            print_won(sum, won);
        }
        if (won == 0)
        {
            sum = sum_rev_diag(grid);
            print_won(sum, won);
        }
        if (won == 0)
        {
            print_draw(grid);
        }

        fout << endl;
    }
    if (fin)
        fin.close();
    if (fout)
        fout.close();
    return  0;
}
