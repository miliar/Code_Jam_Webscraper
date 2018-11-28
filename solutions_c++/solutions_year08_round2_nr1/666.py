#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <math.h>
using namespace std;

int main(int argc, char *argv[])
{
    ifstream in_file;
    ofstream out_file;
    string line;
    int test_case_count;                
    string buffer;
    vector<long double> tokens;    
    vector<long double> X;
    vector<long double> Y;
    long double n, A, B, C, D, x0, y0, M;
    long double xcod, ycod;
    long double temp_double;
    long mid_count;
    
    double xmid;
    double ymid;
    long xround;
    long yround;
    
    in_file.open("A-small.in", ios::binary);
    out_file.open("A-small.out", ios::binary);
    if(in_file.is_open()) 
    {
      getline(in_file, line);
      istringstream strin(line);
      strin >> test_case_count;
      //cout << "test case count = " << test_case_count << endl;
      
      for(int i=0; i < test_case_count; i++)
      {      
         tokens.clear();
         X.clear();
         Y.clear();
      
         getline(in_file, line);
         stringstream ss(line);
         //cout << "Line = " << line << endl;
         while (ss >> buffer)
         {
          //cout << "Buffer = " << buffer << endl;
          istringstream strin(buffer);
          strin >> temp_double;            
          tokens.push_back(temp_double);
          }  
      
          n = tokens[0];    
          A = tokens[1];
          B = tokens[2];
          C = tokens[3];
          D = tokens[4];
          x0 = tokens[5];
          y0 = tokens[6];  
          M = tokens[7];     
          
          X.push_back(x0);
          Y.push_back(y0);
          
          for(int z=1; z<n; z++)
          {
               //   cout << "orig coord = " << X[z-1] << ", " << Y[z-1] << endl;
               xcod = fmod(((A * X[z-1]) + B),M); 
               ycod = fmod(((C * Y[z-1]) + D),M); 
               X.push_back(xcod);
               Y.push_back(ycod);    
               //cout << "coords = " << xcod << ", " << ycod << endl;           
          }
          
          mid_count = 0;
          
          for(int j=0; j < (X.size()-2); j++)
          {
                  //cout << "j = " << j << endl;
                  for(int k=j+1; k < (X.size()-1); k++)
                  {
                          //cout << "k = " << k << endl;
                          for(int l=k+1; l < X.size(); l++)
                          {
                                  //cout << "l = " << l << endl;  
                                  xmid = (X[j]+X[k]+X[l])/3;
                                  ymid = (Y[j]+Y[k]+Y[l])/3;
                                  xround = (long)xmid;
                                  yround = (long)ymid;
                                  //cout << "X val = " << xmid << " round = " << xround << endl;
                                  //cout << "Y val = " << ymid << " round = " << yround << endl;                                  
                                  if(xround == xmid && yround == ymid)
                                  {
                                            mid_count++;          
                                  }
                                  
                          }        
                  }
          }
          
          //cout << "Case #" << i << ": " << mid_count << endl;
          out_file << "Case #" << i+1 << ": " << mid_count << "\n";
      }
    }
    
    in_file.close();
    out_file.close();
    system("PAUSE");
    return EXIT_SUCCESS;
}
