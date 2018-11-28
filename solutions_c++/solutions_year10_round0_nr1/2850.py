// writing on a text file
#include <iostream>
#include <fstream>
using namespace std;

int main () 
{
  string line;
  ifstream inFile("A-large.in");
  ofstream outFile("out.txt");
  int T;
  if (inFile.is_open())
  {
    /*while (! inFile.eof() )
    {*/
      //getline (inFile,line);
      //cout << line << endl;
	  inFile >> T;
	  for(int i = 0; i<T; i++)
	  {
			int N;
			int K;
			int pow = 0;
			int state = 0;
			inFile >> N >> K;
			int switc = 1 << (N - 1);
			int test = N;
			outFile << "Case #" << i+1;
			if((K + 1) % (1 << N) == 0)
				outFile << ": ON" << endl;
			else
				outFile << ": OFF" << endl;
	  }
    //}
  }
  outFile.close();
  inFile.close();

  return 0;
}