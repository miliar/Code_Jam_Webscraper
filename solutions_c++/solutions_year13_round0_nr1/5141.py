#include <iostream>
#include <fstream>
#include <cstdlib>

void count(char value, int& xCount, int& oCount, int& eCount) {
    if( value == 'X' ) xCount++;
    else if( value == 'O' ) oCount++;
    else if( value == '.' ) eCount++;
    else if( value == 'T') {
        xCount++;
        oCount++;
    }

}


int main(int argc, char* argv[]) {

    std::ifstream myFile(argv[1]);
    std::ofstream outFile("out.txt");
    std::string line;
    myFile >> line;
    int cases = atoi(line.c_str());
    char board[4][4];
    
    for(int c=1; c <= cases; c++) {

        for(int i=0; i<4;i++) {
            myFile >> line;
            for(int j=0; j<line.length() && j<4; j++) {
                board[i][j] = line[j];
                std::cout << board[i][j] ;;
            }
            std::cout << "\n";
        }
        std::cout << "\n";

        //check and write to outFile case result
        int xCount=0;
        int oCount=0;
        int eCount=0;
        bool isEnded=true;
        bool checkNextCase=false;

        //check horizontal
        for(int i=0; i < 4 && !checkNextCase; i++) {

            xCount=0;
            oCount=0;
            
            for(int j=0; j < 4 && !checkNextCase; j++) {
                count(board[i][j],xCount,oCount,eCount);
            }

            if( eCount > 0) isEnded = false;
            if( xCount == 4 ) {
                
                outFile << "Case #" << c << ": X won\n";
                checkNextCase = true;
            
            } else if( oCount == 4 ) {
                
                outFile << "Case #" << c << ": O won\n";
                checkNextCase = true;

                
            }
        }

        if( checkNextCase ) continue;
        
        xCount=0;
        oCount=0;
        eCount=0;

        //check vertical
        for(int i=0; i < 4 && !checkNextCase; i++) {
            
            xCount=0;
            oCount=0;
            
            for(int j=0; j < 4 && !checkNextCase; j++) {
                count(board[j][i],xCount,oCount,eCount);
            }

            if( xCount == 4 ) {
                
                outFile << "Case #" << c << ": X won\n";
                checkNextCase = true;
            
            } else if( oCount == 4 ) {
                
                outFile << "Case #" << c << ": O won\n";
                checkNextCase = true;

                
            }
        }

        if( checkNextCase ) continue;
        
        xCount=0;
        oCount=0;
        
        //check first diagonal
        for(int i=0; i < 4; i++) {
            count(board[i][i],xCount,oCount,eCount);
            
            if( xCount == 4 ) {
                
                outFile << "Case #" << c << ": X won\n";
                checkNextCase = true;
            
            } else if( oCount == 4 ) {
                
                outFile << "Case #" << c << ": O won\n";
                checkNextCase = true;
                
            }
        }

        if( checkNextCase ) continue; 
        
        xCount=0;
        oCount=0;
        
        //check second diagonal
        for(int i=0; i < 4; i++) {
            count(board[i][3-i],xCount,oCount,eCount);
            
            if( xCount == 4 ) {
                
                outFile << "Case #" << c << ": X won\n";
                checkNextCase = true;
            
            } else if( oCount == 4 ) {
                
                outFile << "Case #" << c << ": O won\n";
                checkNextCase = true;
                
            }
        }

        if( checkNextCase ) continue; 

        if( isEnded == false ) {
            outFile << "Case #" << c << ": Game has not completed\n";
        } else {
            outFile << "Case #" << c << ": Draw\n";
        }
        
        
    }

    myFile.close();
    outFile.close();

}
