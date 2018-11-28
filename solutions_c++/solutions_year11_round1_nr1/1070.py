#include <iostream>
#include <sstream>
#include <fstream>
#include <cmath>

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
            int N, PD, PG;
            buffer >> N; //!!
            buffer >> PD; //!!
            buffer >> PG; //!!
            
            outFile << "Case #" << i+1 << ": "; 
            if(PG == 100 && PD < 100)
                outFile << "Broken" << endl;
            else if(PG == 0 && PD > 0)
                outFile << "Broken" << endl;
            else{
                int i1 = N;
                for(; i1 >= 1; i1 --)
                    if(i1 * PD % 100 == 0) break;
                if(i1 < 1) outFile << "Broken" << endl;
                else
                    outFile << "Possible" << endl;
            }
            
         }//if(getline(inFile, sLine))
        else{
            cout << "ERROR in file format!" << endl;
            return -1;
        }
    }//for(int i = 0; i < T; i ++)
}
