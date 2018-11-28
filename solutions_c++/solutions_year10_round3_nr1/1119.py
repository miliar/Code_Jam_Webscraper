#include <iostream>
#include <fstream>

using namespace std;


int main()
{
  ifstream ifs;
  ifs.open("case.txt", ifstream::in);

  ofstream ofs;
  ofs.open("output.txt", ofstream::out);

  int nCases = 0;

  ifs>>nCases;

  for(int i=0; i < nCases; i++)
  {
    int nWires = 0;

    ifs>>nWires;

    int A[1001];
    int B[1001];

    for(int j = 0; j < nWires; j++)
    {
      ifs>>A[j]>>B[j];
    }

    int inter = 0;

    for(int j = 0; j < nWires; j++)
    {
      for(int k = j + 1; k < nWires; k++)
      {
	if(A[k] > A[j] )
	{
	  if(B[k] < B[j])
	  {
	    inter++;
	  }
	}
	else
	{
	  if(B[k] > B[j])
	  {
	    inter++;
	  }
	}
      }
    }

    // Print out the output
    ofs<<"Case #"<<(i+1)<<": "<<inter <<endl;
  }


  ofs.close();
  ifs.close();
  return 0;

}
