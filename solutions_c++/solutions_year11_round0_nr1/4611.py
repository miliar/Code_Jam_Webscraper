#include <iostream>
#include <fstream>
#include <string>
#include <new>

using namespace std;

int main() {
    ofstream fout ("gift1.out");
    ifstream fin ("gift1.in");
    int N;
    fin >> N;
    
    for (int i = 0; i < N; i++) {
        int posO = 1;int posB = 1;
        int iO = 0;int iB = 0;
        
        int moves;
        fin >> moves;
        
        int *Omoves = new int[moves];
        int *Bmoves = new int[moves];
        int *waitingOnOs = new int[moves];
        char character;
        
        bool waitingOnO = false;
        for (int j = 0; j < moves; j++) {
            fin >> character;
            if (character == 'O') {
                fin >> Omoves[iO++];
            } else {
                fin >> Bmoves[iB++];
            }  
            waitingOnOs[j] = character == 'O';
        }
        int Ocount ;
        Ocount = iO;
        int Bcount;
        Bcount= iB;
        iO = 1, iB = 1;
        
        bool Opushed = false, Bpushed = false;
        
                int Obutton = 1, Bbutton = 1;
        if (Bcount == 0) 
            Bpushed = true;
        else 
            Bbutton = Bmoves[0];
        if (Ocount == 0)
            Opushed = true;
        else
            Obutton = Omoves[0];        
        int M = 0;
        waitingOnO = waitingOnOs[M++];
        
        int numberOfMoves = 0;
        while ( !(iO > Ocount && iB > Bcount) ) {
            numberOfMoves++;
            
            bool Omoved = false, Bmoved = false;
            
            if (waitingOnO) {
                if (Obutton == posO ) {
                    Obutton = Omoves[iO++];
                    waitingOnO = waitingOnOs[M++];
                    Omoved = true;
                } 
            } else {
                if (Bbutton == posB ) {
                    Bbutton = Bmoves[iB++];
                    waitingOnO = waitingOnOs[M++];
                    Bmoved = true;
                } 
            }
            
            
            if (iO <= Ocount && !Omoved) {
                if (Obutton > posO)
                    posO ++;
                else if (Obutton < posO)
                    posO --;
            } 
            
            if (iB <= Bcount && !Bmoved) {
                if (Bbutton > posB)
                    posB ++;
                else if (Bbutton < posB)
                    posB --;
            }  
            
        }   // while
        
        fout << "Case #" << i+1 << ": " << numberOfMoves << "\n";
        cout << "Case #" << i+1 << ": " << numberOfMoves << "\n";
        
        delete [] Omoves;
        delete [] Bmoves;
        
    }	
    
    
}

