#include <iostream>
#include <sstream>
#include <fstream>
#include <cmath>
#include <vector>
#include <iomanip>
#include <cstring>
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
            int N; 
            buffer >> N; //!!
            char schedule[N][N];
            for(int i1 = 0; i1 < N; i1 ++){
                getline(inFile, sLine);
                char * cstr = new char [sLine.size()+1];
                strcpy (cstr, sLine.c_str());
                for(int i2 = 0; i2 < N; i2 ++) schedule[i1][i2] = cstr[i2];
            }
            double wp[N][N+1]; double owp[N]; double oowp[N];
            for(int i1 = 0; i1 < N; i1 ++){
                int total = 0, total1 = 0;
                for(int i2 = 0; i2 < N; i2 ++){
                    if(schedule[i1][i2] != '.') total ++;
                    if(schedule[i1][i2] == '1') total1 ++;
                }
                wp[i1][N] = (double)total1 / (double)total;
                for(int i2 = 0; i2 < N; i2 ++){
                    if(schedule[i1][i2] == '1') wp[i1][i2] = (double)(total1-1) / (double)(total-1);
                    else if(schedule[i1][i2] == '0') wp[i1][i2] = (double)(total1) / (double)(total-1);
                    else wp[i1][i2] = -1.0;
                }
            }
            
            for(int i2 = 0; i2 < N; i2 ++){
                int total = 0; double sum = 0.0;
                for(int i1 = 0; i1 < N; i1 ++){
                    if(abs(wp[i1][i2]+1.0) < 1e-6) continue;
                    else{
                        sum += wp[i1][i2]; total ++;
                    }
                }
                owp[i2] = sum / total;
                //cout << owp[i2] << " ";
            }
            //cout << endl;
            
            for(int i1 = 0; i1 < N; i1 ++){
                int total = 0; double sum = 0;
                for(int i2 = 0; i2 < N; i2 ++){
                    if(schedule[i1][i2] != '.') { total ++; sum += owp[i2]; }
                }
                oowp[i1] = sum / total;
                //cout << oowp[i1] << " ";
            }
            //cout << endl;
            
            double rpi[N];
            outFile << "Case #" << i+1 << ": " << endl;
            for(int i1 = 0; i1 < N; i1 ++){
                rpi[i1] = 0.25 * wp[i1][N] + 0.5 * owp[i1] + 0.25 * oowp[i1];
                outFile << fixed;
                outFile << setprecision (12) << rpi[i1] << endl;
            }
            
        }//if(getline(inFile, sLine))
        else{
            cout << "ERROR in file format!" << endl;
            return -1;
        }
    }//for(int i = 0; i < T; i ++)
}
