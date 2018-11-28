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
            int R, C;
            buffer >> R; //!!
            buffer >> C; //!!
            char tiles[R][C];
            for(int i1 = 0; i1 < R; i1 ++)
            {
                getline(inFile, sLine);
                char * cstr;
                cstr = new char [C+1];
                strcpy (cstr, sLine.c_str());
                for(int i2 = 0; i2 < C; i2 ++)
                    tiles[i1][i2] = cstr[i2];
            }
            outFile << "Case #" << i+1 << ": " << endl; int i1, i2;
            for(i1 = 0; i1 < R; i1 ++){
                for(i2 = 0; i2 < C; i2 ++){
                    if(tiles[i1][i2] == '#'){
                        if(i1+1 < R && i2+1<C && tiles[i1][i2+1] == '#' && tiles[i1+1][i2] == '#' && tiles[i1+1][i2+1] == '#')
                        { 
                            tiles[i1][i2] = '/'; tiles[i1][i2+1] = '\\'; 
                            tiles[i1+1][i2] = '\\'; tiles[i1+1][i2+1] = '/';
                        }
                        else{
                            break;
                        }
                    }//if(tiles[i1][i2] == '#')                    
                }
                if(i2 < C)
                    break;
            }
            if(i1 < R )
                outFile << "Impossible" << endl;
            else{
                for(i1 = 0; i1 < R; i1 ++){
                    for(i2 = 0; i2 < C; i2 ++){
                        outFile << tiles[i1][i2];
                    }
                    outFile << endl;
                }
            }
            
         }//if(getline(inFile, sLine))
        else{
            cout << "ERROR in file format!" << endl;
            return -1;
        }
    }//for(int i = 0; i < T; i ++)
}
