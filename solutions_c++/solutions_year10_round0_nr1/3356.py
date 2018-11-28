#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

int main()
{
  ifstream ifs;
  ifs.open("A-large.in", ifstream::in);

  ofstream ofs;
  ofs.open("output.txt", ofstream::out);

  int nCases = 0;
  ifs>>nCases;

  for(int i=0; i < nCases; i++)
  {
    long nSnappers = 0;
    long nClicks = 0;

    ifs>>nSnappers>>nClicks;

    long powS = (long)pow(2, nSnappers);

    nClicks++;

    if( nClicks%powS == 0  && nClicks != 1)
      ofs<<"Case #"<<(i+1)<<": "<<"ON"<<endl;
    else
      ofs<<"Case #"<<(i+1)<<": "<<"OFF"<<endl;



    // Print out the output
    //ofs<<"Case #"<<(i+1)<<"Ans"<<endl;
  }


  ofs.close();
  ifs.close();
  return 0;

}
