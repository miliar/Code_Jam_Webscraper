#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <cstdlib>
#include <map>
#include <cmath>

using namespace std;

int main()
{
    ifstream fin;
    ofstream fout;

    fin.open("A-large.txt", ios::in);
    if (!fin.is_open())
    {
        cerr << "Unable to open file" << endl;
        exit(10);
    }

    fout.open("A-large solution.txt", ios::out);
    if(!fout.is_open())
    {
        cerr << "Unable to open file" << endl;
        exit(10);
    }

    int numOfCases;
    fin >> numOfCases;

    char empty;
    //fin >> empty;

    char matrix [4][4];
    int countX(0), countO(0), countDot(0);

    for (int i = 1; i < numOfCases+1; i++)
    {
        for (int row = 0; row < 4; row++)
        {
            for (int col = 0; col < 4; col++)
            {
                fin >> matrix [row][col];
            }
        }

        /*for (int row = 0; row < 4; row++)
        {
            for (int col = 0; col < 4; col++)
            {
                cout << matrix [row][col];
            }
            cout << endl;
        }*/

        int row(0), col(0);
        for (row = 0; row < 4; row++)
        {
            countX = 0;
            countO = 0;
            for (col = 0; col < 4; col++)
            {
                if (matrix[row][col] == 'X' || matrix[row][col] == 'T')
                {
                    countX++;
                }
                if (matrix[row][col] == 'O' || matrix[row][col] == 'T')
                {
                    countO++;
                }
                if (matrix[row][col] != 'X' && matrix[row][col] != 'O' && matrix[row][col] != 'T')
                {
                    countDot++;
                }
            }
//cout << "countX is: " << countX << " " << "countDot is: " << countDot << endl;
            if (countX == 4)
            {
                fout << "Case #" << i << ": X won" << endl;
                col = 4;
                row = 4;
            }
            else if (countO == 4)
            {
                fout << "Case #" << i << ": O won" << endl;
                col = 4;
                row = 4;
            }

        }

        if (countX != 4 && countO != 4)
        {
            for (row = 0; row < 4; row++)
            {
                countX = 0;
                countO = 0;

                for (col = 0; col < 4; col++)
                {
                    if (matrix[col][row] == 'X' || matrix[col][row] == 'T')
                    {
                        countX++;
                    }
                    if (matrix[col][row] == 'O' || matrix[col][row] == 'T')
                    {
                        countO++;
                    }
                    if (matrix[row][col] != 'X' && matrix[row][col] != 'O' && matrix[row][col] != 'T')
                    {
                        countDot++;
                    }
                }

                if (countX == 4)
                {
                    fout << "Case #" << i << ": X won" << endl;
                    col = 4;
                    row = 4;
                }
                else if (countO == 4)
                {
                    fout << "Case #" << i << ": O won" << endl;
                    col = 4;
                    row = 4;
                }

            }

            if (countX != 4 && countO != 4)
            {
                row = 0;
                countX = 0;
                countO = 0;

                for (col = 0; col < 4; col++)
                {
                    if (matrix[row][col] == 'X' || matrix[row][col] == 'T')
                    {
                        countX++;
                    }
                    if (matrix[row][col] == 'O' || matrix[row][col] == 'T')
                    {
                        countO++;
                    }
                    if (matrix[row][col] != 'X' && matrix[row][col] != 'O' && matrix[row][col] != 'T')
                    {
                        countDot++;
                    }

                    row++;
                }
                    if (countX == 4)
                    {
                        fout << "Case #" << i << ": X won" << endl;
                        col = 4;
                        row = 4;
                    }
                    else if (countO == 4)
                    {
                        fout << "Case #" << i << ": O won" << endl;
                        col = 4;
                        row = 4;
                    }

                if (countX != 4 && countO != 4)
                {
                    row = 0;
                    countX = 0;
                    countO = 0;

                    for (col = 3; col >= 0; col--)
                    {
                        if (matrix[row][col] == 'X' || matrix[row][col] == 'T')
                        {
                            countX++;
                        }
                        if (matrix[row][col] == 'O' || matrix[row][col] == 'T')
                        {
                            countO++;
                        }
                        if (matrix[row][col] != 'X' && matrix[row][col] != 'O' && matrix[row][col] != 'T')
                        {
                            countDot++;
                        }

                        row++;
                    }
                        if (countX == 4)
                        {
                            fout << "Case #" << i << ": X won" << endl;
                            col = 4;
                            row = 4;
                        }
                        else if (countO == 4)
                        {
                            fout << "Case #" << i << ": O won" << endl;
                            col = 4;
                            row = 4;
                        }
                }
            }
        }

        if (countDot > 0 && countX != 4 && countO != 4)
        {
            fout << "Case #" << i << ": Game has not completed" << endl;
        }
        else if (countDot == 0 && countX != 4 && countO != 4)
        {
            fout << "Case #" << i << ": Draw" << endl;
        }cout << "countDot is:" << countDot << endl;
countDot = 0;

    }


















        /*for (int row = 0; row < 4; row++)
        {
            for (int col = 0; col < 4; col++)
            {
                cout << matrix [row][col];
            }
            cout << endl;
        }*/









    return 0;
    }
