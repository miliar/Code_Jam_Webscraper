#include <iostream>
#include <sstream>
#include <fstream>
#include <cmath>
#include <iomanip>
#include <cstring>
#include <cassert>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <stdlib.h>
using namespace std;

string cIntToStr(int number)
{
   //stringstream provides an interface to manipulate strings as if they were input/output streams.
   stringstream ss;//create a stringstream
   ss << number;//add number to the stream
   return ss.str();//return a string with the contents of the stream
}

int cStrToInt(string s) 
{
    //istringstream provides an interface to manipulate strings as input streams.
    istringstream buffer(s, istringstream::in);
    int value;
    buffer >> value;
    return value;
}

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
        cout << sLine << endl;
        buffer >> T;
        //cout << T << endl;
    }
    else{
        cout << "ERROR in file format!" << endl;
        return -1;
    }
    
    for(int i = 0; i < T; i ++){
        if(getline(inFile, sLine))
        {
            istringstream buffer(sLine, istringstream::in);
            int X, S, R, T, N;
            buffer >> X; //!!
            buffer >> S; //!!
            buffer >> R; //!!
            buffer >> T; //!!
            buffer >> N; //!!
            
            int B[N], E[N], W[N]; int ww = 0;
            for(int i1 = 0; i1 < N; i1 ++){
                if(getline(inFile, sLine))
                {
                    istringstream buffer2(sLine, istringstream::in);
                    buffer2 >> B[i1]; //!!
                    buffer2 >> E[i1]; //!!
                    buffer2 >> W[i1]; //!!
                    assert(B[i1] <= E[i1]);  
                    ww += E[i1]-B[i1];            
                }
                else{
                    cout << "ERROR in file format!" << endl;
                    return -1;
                }
            }//for(int i1 = 0; i1 < N; i1 ++)
            
            double sum = 0;             
            if(R*T <= X-ww){
                for(int i1 = 0; i1 < N; i1 ++){
                    sum += (double)(E[i1]-B[i1])/(double)(S+W[i1]);
                }  
                sum += T; //speed R
                sum += (double)(X-R*T-ww)/(double)(S); //speed S              
            }
            else{
                sum += (X-ww)/(double)(R);
                double T0 = T - (X-ww)/(double)(R); //left mins for speed R
            
                for(int i1 = 0; i1 < N-1; i1 ++){
                    for(int i2 = i1+1; i2 < N; i2 ++){
                        if(W[i2]<W[i1]){
                            int tmp = W[i2];
                            W[i2] = W[i1];
                            W[i1] = tmp;
                        
                            tmp = E[i2];
                            E[i2] = E[i1];
                            E[i1] = tmp;
                        
                            tmp = B[i2];
                            B[i2] = B[i1];
                            B[i1] = tmp;
                       }
                    }//for
                }//for
                bool isRunout = false;
                for(int i1 = 0; i1 < N; i1 ++){
                    if(isRunout == true) 
                    { sum += (double)(E[i1]-B[i1])/(double)(S+W[i1]); continue; }
                    
                    double T1 = (double)(E[i1]-B[i1])/(double)(R+W[i1]);
                    if(abs(T0-T1) < 1e-6) {sum += T1; T0 = 0; isRunout = true;}
                    else if(T0 > T1) {sum += T1; T0 -= T1;}
                    else{ //T0 < T1
                        sum += T0;
                        sum += (double)(E[i1]-B[i1]-(R+W[i1])*T0)/(double)(S+W[i1]);
                        T0 = 0; isRunout = true;
                    }
                }
            
            }//else
        
            outFile << "Case #" << i+1 << ": "; 
            outFile << fixed;
            outFile << setprecision (6) << sum << endl;
            
        }//if(getline(inFile, sLine))
        else{
            cout << "ERROR in file format!" << endl;
            return -1;
        }
        
        
                
        
    }//for(int i = 0; i < T; i ++)
}
