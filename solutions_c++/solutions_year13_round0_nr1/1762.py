#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() 
{
    int loops;
    bool finished;
    string input;
    char array[4][4];
    ifstream myfile("A-large.in");
    ofstream outputfile;
    outputfile.open("output.txt");
    myfile >> loops;

    for (int loopnumber = 0; loopnumber < loops; loopnumber++)
    {
        finished = false;
        for (int i = 0; i < 4; i++)
        {
            myfile >> input;
            for (int j = 0; j < 4; j++)
                array[i][j] = input[j];
        }

        // Rows and Columns
        for (int i = 0; i < 4; i++)
        {
            if(
                    (array[i][0] == 'X' || array[i][0] == 'T') &&
                    (array[i][1] == 'X' || array[i][1] == 'T') &&
                    (array[i][2] == 'X' || array[i][2] == 'T') &&
                    (array[i][3] == 'X' || array[i][3] == 'T') )
            {
                outputfile << "Case #" << loopnumber+1 << ": X won" << endl;
                finished = true;
                break;
            }
            if(
                    (array[i][0] == 'O' || array[i][0] == 'T') &&
                    (array[i][1] == 'O' || array[i][1] == 'T') &&
                    (array[i][2] == 'O' || array[i][2] == 'T') &&
                    (array[i][3] == 'O' || array[i][3] == 'T') )
            {
                outputfile << "Case #" << loopnumber+1 << ": O won" << endl;
                finished = true;
                break;
            }
            if(
                    (array[0][i] == 'X' || array[0][i] == 'T') &&
                    (array[1][i] == 'X' || array[1][i] == 'T') &&
                    (array[2][i] == 'X' || array[2][i] == 'T') &&
                    (array[3][i] == 'X' || array[3][i] == 'T') )
            {
                outputfile << "Case #" << loopnumber+1 << ": X won" << endl;
                finished = true;
                break;
            }
            if(
                    (array[0][i] == 'O' || array[0][i] == 'T') &&
                    (array[1][i] == 'O' || array[1][i] == 'T') && 
                    (array[2][i] == 'O' || array[2][i] == 'T') &&
                    (array[3][i] == 'O' || array[3][i] == 'T') )
            {
                outputfile << "Case #" << loopnumber+1 << ": O won" << endl;
                finished = true;
                break;
            }
        }

        // Diagonals
        if(
                (array[0][0] == 'X' || array[0][0] == 'T') &&
                (array[1][1] == 'X' || array[1][1] == 'T') && 
                (array[2][2] == 'X' || array[2][2] == 'T') &&
                (array[3][3] == 'X' || array[3][3] == 'T') &&
                !finished)
        {
            outputfile << "Case #" << loopnumber+1 << ": X won" << endl;
            finished = true;
        }
        if(
                (array[0][0] == 'O' || array[0][0] == 'T') &&
                (array[1][1] == 'O' || array[1][1] == 'T') && 
                (array[2][2] == 'O' || array[2][2] == 'T') &&
                (array[3][3] == 'O' || array[3][3] == 'T') &&
                !finished)
        {
            outputfile << "Case #" << loopnumber+1 << ": O won" << endl;
            finished = true;
        }
        if(
                (array[0][3] == 'X' || array[0][3] == 'T') &&
                (array[1][2] == 'X' || array[1][2] == 'T') && 
                (array[2][1] == 'X' || array[2][1] == 'T') &&
                (array[3][0] == 'X' || array[3][0] == 'T') &&
                !finished)
        {
            outputfile << "Case #" << loopnumber+1 << ": X won" << endl;
            finished = true;
        }
        if(
                (array[0][3] == 'O' || array[0][3] == 'T') &&
                (array[1][2] == 'O' || array[1][2] == 'T') && 
                (array[2][1] == 'O' || array[2][1] == 'T') &&
                (array[3][0] == 'O' || array[3][0] == 'T') &&
                !finished)
        {
            outputfile << "Case #" << loopnumber+1 << ": O won" << endl;
            finished = true;
        }

        if (!finished)
            for (int i = 0; i < 4; i++)
                for (int j = 0; j < 4; j++)
                    if (array[i][j] == '.' && !finished)
                    {
                        finished = true;
                        outputfile << "Case #" << loopnumber+1 << ": Game has not completed" << endl;
                    }

        if (!finished)
            outputfile << "Case #" << loopnumber+1 << ": Draw" << endl;

    }

    outputfile.close();

    return 0;
}
