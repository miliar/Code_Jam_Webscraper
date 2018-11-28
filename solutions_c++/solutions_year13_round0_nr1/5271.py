#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;

int main(int argc, char **argv) {
    if (argc < 2) {
        cout << "Please specify input file" << endl;
        return 1;
    }
    ifstream in(argv[1]);

    int testCases;
    in >> testCases;
    in.get();
    for (int testCase =0; testCase < testCases; testCase++) {
        char *result = (char*)"Game has not completed";
        // Read test case
        char field[4][4];
        char line[10];
        for(int i=0; i<4; i++) {
            in.getline(line,10);
//            cout << "Line: " << line << endl;
            for(int j=0; j<4; j++) {
                field[i][j] = line[j];
            }
        }
        in.get(); // read next \n

        // Test if X won (horz):
        for (int i=0; i<4; i++) {
            bool won = true;
            for(int j=0; j<4; j++) {
                if(field[i][j] != 'X' && field[i][j] != 'T') {
                    won = false;
                    break;
                }
            }
            if (won) {
                result = (char*)"X won";
                goto print_result;
            }
        }

        // Test if X won (vert):
        for (int i=0; i<4; i++) {
            bool won = true;
            for(int j=0; j<4; j++) {
                if(field[j][i] != 'X' && field[j][i] != 'T') {
                    won = false;
                    break;
                }
            }
            if (won) {
                result = (char*)"X won";
                goto print_result;
            }
        }

        // Test if X won (diag1):
        {
            bool won = true;
            for (int i=0; i<4; i++) {
                if(field[i][i] != 'X' && field[i][i] != 'T') {
                    won = false;
                    break;
                }
            }
            if (won) {
                result = (char*)"X won";
                goto print_result;
            }
        }

        // Test if X won (diag2):
        {
            bool won = true; 
            for (int i=0; i<4; i++) {
                if(field[i][3-i] != 'X' && field[i][3-i] != 'T') {
                    won = false;
                    break;
                }
            }
            if (won) {
                result = (char*)"X won";
                goto print_result;
            }
        }
        
        
        // Test if O won (horz):
        for (int i=0; i<4; i++) {
            bool won = true;
            for(int j=0; j<4; j++) {
                if(field[i][j] != 'O' && field[i][j] != 'T') {
                    won = false;
                    break;
                }
            }
            if (won) {
                result = (char*)"O won";
                goto print_result;
            }
        }

        // Test if O won (vert):
        for (int i=0; i<4; i++) {
            bool won = true;
            for(int j=0; j<4; j++) {
                if(field[j][i] != 'O' && field[j][i] != 'T') {
                    won = false;
                    break;
                }
            }
            if (won) {
                result = (char*)"O won";
                goto print_result;
            }
        }

        // Test if O won (diag1):
        {
            bool won = true;
            for (int i=0; i<4; i++) {
                if(field[i][i] != 'O' &&  field[i][i] != 'T') {
                    won = false;
                    break;
                }
            }
            if (won) {
                result = (char*)"O won";
                goto print_result;
            }
        }

        // Test if O won (diag2):
        {
            bool won = true; 
            for (int i=0; i<4; i++) {
                if(field[i][3-i] != 'O' && field[i][3-i] != 'T') {
                    won = false;
                    break;
                }
            }
            if (won) {
                result = (char*)"O won";
                goto print_result;
            }
        }

        // Test draw:
        {
            bool draw = true;
            for(int i=0; i<4; i++) {
                for(int j=0; j<4; j++) {
                    if(field[i][j] == '.') {
                        draw = false;
                        break;
                    }
                }
            }
            if (draw) {
                result = (char*)"Draw";
                goto print_result;
            }
        }
        
        print_result:

        cout << "Case #" << (testCase+1) << ": " << result << endl;
    } 
    
    return 0;
}
