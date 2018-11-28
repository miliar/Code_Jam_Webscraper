#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

int main () {
  ofstream outputfile;
  outputfile.open ("output.txt");

  ifstream inputfile("input.txt");
  int nT;
  inputfile >> nT;
  
  for (int i=1; i<= nT; i++)
    {
      int nK, nN;
      std::string onoff = "OFF";
      inputfile >> nN;
      inputfile >> nK;
      int pow = 1<<nN ;
      //cout << pow << endl;
      if ( nK%pow == pow - 1)
	{
	  onoff = "ON";
	}
      outputfile << "Case #" << i << ": " << onoff << endl;
      cout << "Case #" << i << ": " << onoff << endl;
    }
  outputfile.close();
  return 0;
}
