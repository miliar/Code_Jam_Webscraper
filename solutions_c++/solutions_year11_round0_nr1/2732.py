#include <iostream>
#include <sstream>
#include <fstream>
#include <cmath>
#include <cstring>
#include <cassert>
#include <stdlib.h>

using namespace std;

int main(int argc, char *argv[])
{
    ifstream inFile(argv[1], ifstream::in);
    ofstream outFile(argv[2], ofstream::out);
    string sLine; int T;

    //The function prototype for getline is:
    //istream& getline(istream& is, string& s, char delimiter = '\n');
    //There's a conversion operator defined that converts an istream to a void*, 
    //which is further converted to a bool by using a simple != NULL rule. 
    //The void* converter will be a non-NULL value if the stream is ready and NULL if an error occurs.
    if(getline(inFile, sLine)) //!! global "getline()"
    {
        //Do here whatever you need to do
        istringstream buffer(sLine, istringstream::in);
        buffer >> T;
    }
    else{
        cout << "ERROR in file format!" << endl;
        return -1;
    }

    for(int i0 = 0; i0 < T; i0 ++){
        int N; int arr_O[101]; int arr_B[101]; int max_O = 0; int max_B = 0;    
        for(int i1 = 0; i1 < 101; i1 ++) arr_B[i1] = 0;
        for(int i1 = 0; i1 < 101; i1 ++) arr_O[i1] = 0;            
        if(getline(inFile, sLine))
        {
            char *line = (char*)sLine.c_str();
            N = atoi(strtok(line, " "));
            int num1 = 0; int num2 = 0; int num = 0;
            int curr_B = 1; int curr_O = 1; int isFirst = -1;
            int delta1 = 0; int delta2 = 0;
            while(line = strtok(NULL, " ")){
                if(strcmp(line, "B") == 0)
                {
                    int idx = atoi(strtok(NULL, " ")); // button no
                    if(isFirst == -1 || isFirst == 1){                        
                        if(idx > curr_B) delta1 += idx - curr_B;
                        else
                            delta1 += curr_B - idx;
                        delta1 += 1;
                        
                        isFirst = 1;
                        curr_B = idx;
                    }
                    if(isFirst == 2){
                        isFirst = 1; num += delta2;
                        //cout << num << endl;
                        if(idx > curr_B) delta1 += idx - curr_B;
                        else
                            delta1 += curr_B - idx;
                        if(delta1 < delta2)
                            delta1 = 1;
                        else
                            delta1 = delta1 - delta2 + 1; 
                        curr_B = idx; delta2 = 0;
                    }

                }
                if(strcmp(line, "O") == 0)
                {
                    int idx = atoi(strtok(NULL, " ")); // button no
                    if(isFirst == -1 || isFirst == 2){                        
                        if(idx > curr_O) delta2 += idx - curr_O;
                        else
                            delta2 += curr_O - idx;
                        delta2 += 1;
                        
                        isFirst = 2;
                        curr_O = idx;
                    }
                    
                    if(isFirst == 1){
                        isFirst = 2; num += delta1; 
                        //cout << "Delta2 " << delta2 << endl;
                        //cout << num << endl;
                        if(idx > curr_O) delta2 += idx - curr_O;
                        else
                            delta2 += curr_O - idx;
                        //cout << delta1 << " " << delta2 << " " << curr_O << " " << idx << endl;
                        if(delta2 < delta1)
                            delta2 = 1;
                        else
                            delta2 = delta2 - delta1 + 1; 
                        
                        curr_O = idx; delta1 = 0;
                    }
                  
                }
            }
            if(isFirst == 1) num += delta1;
            else num += delta2;
            //cout << num << endl;
            //cout << endl;
         
            outFile << "Case #" << i0+1 << ": ";
            outFile << num << endl;  //use "%"
            
        }//if(getline(inFile, sLine))
        else{
            cout << "ERROR in file format!" << endl;
            return -1;
        } 
    }
}
