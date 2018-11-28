#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <algorithm>
using namespace std;

int main () {
  ofstream outputfile;
  outputfile.open ("outputA.txt");

  ifstream inputfile("inputA.txt");
  int nT;
  inputfile >> nT;
  
  for (int testcase=1; testcase<= nT; testcase++)
    {
      int N;
      inputfile >> N;
      vector<int> A;
      vector<int> B;
      int temp;
      for (int i=0; i<N; i++)
      {
        inputfile >> temp;
        A.push_back(temp);
        inputfile >> temp;
        B.push_back(temp);
      }
      int intersections = 0;
      for (int i=0; i<N-1; i++)
      {
        //cout << "i: " << i << endl;
        for (int j=i+1; j<N; j++)
        {
          //cout << "i: " << i << ", j: " << j << endl;
          //cout << "A: " << A.at(i) << ", B: " << B.at(i) << endl;
          //cout << "A: " << A.at(j) << ", B: " << B.at(j) << endl;
          if ( ((A.at(i)>A.at(j)) && (B.at(i)<B.at(j))) || ((A.at(i)<A.at(j)) && (B.at(i)>B.at(j))) )
          {
            //cout << "got it" << endl;
            intersections ++;
          }
        }
      }
      outputfile << "Case #" << testcase << ": " << intersections << endl;
      cout << "Case #" << testcase << ": " << intersections << endl;
    }
  outputfile.close();
  return 0;
}
