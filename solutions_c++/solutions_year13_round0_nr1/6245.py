#include <iostream>
#include <cstdlib>
#include <fstream>

using namespace std;

int main() {

    fstream fileObj;
    int NUM_TESTS = 0;

    char fName[] = "A-large.in";
    fileObj.open(fName, ios::in);

    if (fileObj == NULL) {
        cerr << "Can't open file" << endl;
        exit(-1);
    }

    fileObj >> NUM_TESTS;
//    cout << "Number of test cases: " << NUM_TESTS << endl;

    for (int tIndex = 0; tIndex < NUM_TESTS; tIndex++) {
        
        int TicArray[4][4];
        int DrawFlag = 0;
        int ColCountX[4], ColCountO[4];

        int DiagCountX0 = 0, DiagCountX1 = 0;
        int DiagCountO0 = 0, DiagCountO1 = 0;
        
        int Winner = 0;

        for (int i = 0; i < 4; i++)
            ColCountX[i] = ColCountO[i] = 0;

        char curr = 0;
        for (int i = 0; i < 4; i++) {

            int RowCountX = 0, RowCountO = 0;
            for (int j = 0; j < 4; j++) {
                fileObj >> curr;
                
                switch(curr) {
                    
                    case 'X' :
                        RowCountX += 5;
                        ColCountX[j] += 5;
                        TicArray[i][j] = 1;
                        if (i == j) 
                            DiagCountX0 += 5;
                        if (i + j == 3)
                            DiagCountX1 += 5;
                        break;
                    
                    case 'O' :
                        RowCountO += 5;
                        ColCountO[j] += 5;
                        TicArray[i][j] = 2;
                        if (i == j) 
                            DiagCountO0 += 5;
                        if (i + j == 3)
                            DiagCountO1 += 5;
                        break;
                    
                    case 'T' :
                        RowCountX += 5;
                        ColCountX[j] += 5;
                        RowCountO += 5;
                        ColCountO[j] += 5;
                        TicArray[i][j] = 3;
                        if (i == j) {
                            DiagCountX0 += 5;
                            DiagCountO0 += 5;
                        }
                        if (i + j == 3) {
                            DiagCountX1 += 5;
                            DiagCountO1 += 5;
                        }
                        break;
                    
                    case '.' :
                        RowCountX = RowCountO = 0;
                        ColCountX[j] = ColCountO[j] = 0;
                        TicArray[i][j] = 0;
                        DrawFlag = 1;
                        break;

                    default:
                        cerr << "Unknown value in test case";
                }
//                cout << TicArray[i][j] << " ";
            }

            if (RowCountX == 20)
                Winner = 1;
            
            if (RowCountO == 20)
                Winner = 2;
        }

        if ((DiagCountX0 == 20) || (DiagCountX1 == 20))
            Winner = 1;

        if ((DiagCountO0 == 20) || (DiagCountO1 == 20))
            Winner = 2;

        for (int i = 0; !Winner && i < 4; i++) {

            if (ColCountX[i] == 20)
                Winner = 1;

            if (ColCountO[i] == 20)
                Winner = 2;
        }
        
        if (Winner == 1)
            cout << "Case #" << tIndex + 1 << ": X won" << endl;
        else if (Winner == 2)
            cout << "Case #" << tIndex + 1 << ": O won" << endl;
        else if ((Winner == 0) && (DrawFlag))
            cout << "Case #" << tIndex + 1 << ": Game has not completed" << endl;
        else
            cout << "Case #" << tIndex + 1 << ": Draw" << endl;
    }

    return 0;
}

