//
//  Qualification Round 2011 - A
//
//  Diogo Tridapall
//

#include <iostream>
#include <string>
#include <cstdlib>
#include <fstream>
#include <cmath>

using namespace std;

struct robot_t{
    int pos;
    int time;
};

typedef enum{
    kOrange = 0,
    kBlue
} colors_t; 

int main (int argc, const char * argv[]){

    string inFileName;
    string outFileName;

    
    switch (argc) {
        case 2:
            inFileName = argv[1];
            outFileName.assign(inFileName, 0, inFileName.find_last_of(".in")-2);
            outFileName+=".out";
            break;
        default:
            cout << "Usage: " << argv[0] << " inputFile" << endl;
            exit(0);
            break;
    }
    
    fstream inFile(inFileName.c_str(),fstream::in);
    if (!inFile.is_open()) {
        cout << "File " << inFileName << " is not open!" << endl;
        exit(1);
    }
    fstream outFile(outFileName.c_str(),fstream::out);
    if (!outFile.is_open()) {
        cout << "File " << outFileName << " is not open!" << endl;
        exit(1);
    }
    
    
    int T;    
    
    if(!(inFile >> T)){
        cout << "Error, can't read T!" << endl;
        exit(1);
    }
    
    for (int iT = 0; iT < T; ++iT) {
        robot_t robot[2];
        for (int robotI = kOrange; robotI<=kBlue; ++robotI) {
            robot[robotI].pos = 1;
            robot[robotI].time = 0;
        }
        
        int time=0;
        
        int N;
        inFile >> N;
        char R;
        int P;
        int inRound=-1;
        for (int iN=0; iN<N; ++iN) {
            if(!(inFile >> R >> P)){
                cout << "Error, can't read R and P!" << endl;
                exit(1);
            }
            switch (R) {
                case 'O':
                    inRound = kOrange;
                    break;
                case 'B':
                    inRound = kBlue;
                    break;
                default:
                    cout<< "Robot " << R <<  " not found!" << endl;
                    break;
            }
            int timeToDo = abs(P-robot[inRound].pos) + 1;
            int deltaTime = time - robot[inRound].time;
            int extraTime = timeToDo - deltaTime;
            time += (extraTime<=0) ? 1 : extraTime;
            
            robot[inRound].pos = P;
            robot[inRound].time = time;
        }
        
        outFile << "Case #" << iT+1 << ": " << time << endl;
        
    
    }
    
    
    inFile.close();
    outFile.close();
    return 0;
}


















