#include <iostream>
#include <fstream>
using namespace std;


bool check(int x, int Lst[], int MAX){
    for (int i=0; i<MAX; i++){
        if (((x % Lst[i]) != 0)&&((Lst[i] % x) != 0)){
            return 0;
            }
        }
    return 1;
    }

int main() {
    
    ifstream srcfile;
    ofstream outfile;
    
    
    srcfile.open("C-small-attempt3.in");
    outfile.open("output_file");

    if (srcfile.is_open()){
        
        int NumCases;
        int NumOthers;
        int LowNote;
        int HighNote;
        int * Others;
        int CaseNum = 1;
        
        srcfile >> NumCases;
        
        while (srcfile.good()){
            int Solution = -1;
            
            srcfile >> NumOthers >> LowNote >> HighNote;
            if (!srcfile.good()) break;
            Others = new (nothrow) int [NumOthers];
            
            for (int i=0; i<NumOthers; i++){
                srcfile >> Others[i];
                }
            // Computing
            for (int i=LowNote; i<=HighNote; i++){
                if (check(i, Others, NumOthers)==1){
                    Solution=i;
                    break;
                    }
                }
            
            if (Solution == -1){
                outfile << "Case #" << CaseNum << ": " << "NO" << endl;
                }
            else{
                outfile << "Case #" << CaseNum << ": " << Solution << endl;
                }
            
                
            delete [] Others;
            Others = NULL;
            if (!srcfile.good()) break;
            CaseNum++;
            }
        
        }    
    else{
        cerr << "Unable to open " << srcfile << endl;
        cerr << "Program Terminated...\n";
        exit(1);
        }
        
    //delete [] Others;
    srcfile.close();
    
    outfile.close();
    }