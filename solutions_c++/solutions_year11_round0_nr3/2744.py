#include <iostream>
#include <sstream>
#include <fstream>
#include <cmath>
#include <cstring>
#include <cassert>
#include <stdlib.h>
#include <list>

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
        int N;        
        if(getline(inFile, sLine))
        {
            istringstream buffer(sLine, istringstream::in);
            buffer >> N;
            int arr[N];
            if(getline(inFile, sLine))
            {
                istringstream buffer(sLine, istringstream::in);
                for(int i1 = 0; i1 < N; i1 ++){
                    buffer >> arr[i1];
                }
                
                int sum = 0;
                for(int i1 = 0; i1 < N; i1 ++){
                    sum = sum ^ arr[i1];
                }
                if(sum != 0){
                    outFile << "Case #" << i0+1 << ": ";
                    outFile << "NO" << endl;  
                }
                else{
                    for(int i1 = 1; i1 < N; i1 ++){
                        if(arr[0] > arr[i1]){
                            int tmp = arr[0];
                            arr[0] = arr[i1];
                            arr[i1] = tmp;
                        }
                    }
                    sum = 0;
                    for(int i1 = 1; i1 < N; i1 ++){
                        sum = sum + arr[i1];
                    }
                    
                    outFile << "Case #" << i0+1 << ": ";
                    outFile << sum << endl;                 
                }
                
            }//if(getline(inFile, sLine))
            else{
                cout << "ERROR in file format!" << endl;
                return -1;
            } 
        }
         else{
            cout << "ERROR in file format!" << endl;
            return -1;
        } 
    }//for(int i0 = 0; i0 < T; i0 ++)
}
