#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <list>

#define MATRIX_X_SIZE 4
#define MATRIX_Y_SIZE 4

#define VAL_EMPTY 0
#define VAL_X 1
#define VAL_O 2
#define VAL_T 3

int matrix[MATRIX_X_SIZE][MATRIX_Y_SIZE];

using namespace std;

void checkWinner(string & result) {
    bool isFull = true;
    for(int indexX = 0; indexX < MATRIX_X_SIZE; ++indexX)
    {
        int totalX = 0;
        int totalO = 0;
        for(int indexY = 0; indexY < MATRIX_Y_SIZE; ++indexY)
        {

            switch(matrix[indexX][indexY])
            {
                case 1:
                  ++totalX;
                  break;
                case 2:
                  ++totalO;
                  break;
                case 3:
                  ++totalX;
                  ++totalO;
                  break;
                default:
                  isFull = false;
                  break;                                               
            }
        }
        if(totalX == MATRIX_Y_SIZE) {
                  result = "X won";
                  return;
        }
        if(totalO == MATRIX_Y_SIZE) {
                  result = "O won";
                  return;
        }
    }
    for(int indexY = 0; indexY < MATRIX_Y_SIZE; ++indexY)
    {
        int totalX = 0;
        int totalO = 0;
        for(int indexX = 0; indexX < MATRIX_X_SIZE; ++indexX)
        {

            switch(matrix[indexX][indexY])
            {
                case 1:
                  ++totalX;
                  break;
                case 2:
                  ++totalO;
                  break;
                case 3:
                  ++totalX;
                  ++totalO;
                  break;
                default:
                  isFull = false;
                  break;                                               
            }
        }
        if(totalX == MATRIX_Y_SIZE) {
                  result = "X won";
                  return;
        }
        if(totalO == MATRIX_Y_SIZE) {
                  result = "O won";
                  return;
        }
    }
    {
        int totalX = 0;
        int totalO = 0;
        for(int indexX = 0, indexY = 0; indexX < MATRIX_X_SIZE; ++indexX,++indexY)
        {

            switch(matrix[indexX][indexY])
            {
                case 1:
                  ++totalX;
                  break;
                case 2:
                  ++totalO;
                  break;
                case 3:
                  ++totalX;
                  ++totalO;
                  break;
                default:
                  isFull = false;
                  break;                                               
            }
        }
        if(totalX == MATRIX_Y_SIZE) {
                  result = "X won";
                  return;
        }
        if(totalO == MATRIX_Y_SIZE) {
                  result = "O won";
                  return;
        }
    }
    {
        int totalX = 0;
        int totalO = 0;
        for(int indexX = MATRIX_X_SIZE - 1, indexY = 0; indexX >= 0; --indexX,++indexY)
        {

            switch(matrix[indexX][indexY])
            {
                case 1:
                  ++totalX;
                  break;
                case 2:
                  ++totalO;
                  break;
                case 3:
                  ++totalX;
                  ++totalO;
                  break;
                default:
                  isFull = false;
                  break;                                               
            }
        }
        if(totalX == MATRIX_Y_SIZE) {
                  result = "X won";
                  return;
        }
        if(totalO == MATRIX_Y_SIZE) {
                  result = "O won";
                  return;
        }
    }
    if(isFull)
    {
                  result = "Draw";
                  return;
    }
    else
    {
                  result = "Game has not completed";
                  return;
    }
}

bool readInput(list<string> & results) {
    string line;
    ifstream inFile;
    inFile.open ("A-large.in", ifstream::in);
    if(inFile.good())
    {
        getline(inFile, line);
        int numberOfTestCases;
        istringstream(line) >> numberOfTestCases;
        for(int i = 0; i < numberOfTestCases; ++i)
        {
                for(int indexX = 0; indexX < MATRIX_X_SIZE; ++indexX)
                {
                    getline(inFile, line);
                    if(line.size() != MATRIX_Y_SIZE)
                    {
                        cout<<"line.size() != "<<MATRIX_Y_SIZE<<endl;
                        return false;
                    }
                    for(int indexY = 0; indexY < MATRIX_Y_SIZE; ++indexY)
                    {
                        switch(line[indexY])
                        {
                            case 't':
                            case 'T':
                              matrix[indexX][indexY] = VAL_T;
                              break;
                            case 'o':
                            case 'O':
                              matrix[indexX][indexY] = VAL_O;
                              break;
                            case 'x':
                            case 'X':
                              matrix[indexX][indexY] = VAL_X;
                              break;
                            default: 
                              matrix[indexX][indexY] = VAL_EMPTY;
                              break;                                               
                        }
                    }
                }
                ostringstream preResultString;
                preResultString<<"Case #"<<i+1<<": ";
                string result;
                checkWinner(result);
                results.push_back(preResultString.str() + result);
                getline(inFile, line);
        }
        inFile.close();
    }
    else
    {
        cout<<"File couldnt open : "<<endl;
        return false;
    }
    return true;
}

void writeOutput(const list<string> & results)
{
    ofstream outFile("out.txt", ios_base::binary);
    int counter = 0;
    for(list<string>::const_iterator it = results.begin(); it != results.end(); ++it)
    {
        outFile<<(*it);
        ++counter;
        //if(results.size() != counter) {
                          outFile<<'\n';
        //}
    }
    outFile.close();
}

int main(int argc, char *argv[])
{
    system("PAUSE");
    list<string> results;
    readInput(results);
    writeOutput(results);
    return EXIT_SUCCESS;
}
