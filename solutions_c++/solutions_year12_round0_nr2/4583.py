#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>

using namespace std;

int main(int argc, char *argv[])
{
  ifstream fp(argv[1],ifstream::in);
  string line;
  fp >> line; // number of test cases      
  int T = atoi(line.c_str());
  cout << line << endl;
  int N = 1;
  int S = 0; // surprising
  int t[100]; // total points
  int Case[100]; // number of test cases
  int p; // how many googlers scored at least p?
  int c=0; // case
  while(!fp.eof())
    {
      fp >> line; // number of googlers
      N = atoi(line.c_str());
      fp >> line; // surprising
      S = atoi(line.c_str());
      fp >> line; // min max score
      p = atoi(line.c_str());
      for (int i=0;i<N;i++) // get scores
	{
	  fp >> line;
	  t[i] = atoi(line.c_str());
	}
      
      // compute output for this test case
      int atleast = 3*p-2; // made at least a p
      int maybe = 3*p-3; // need to be surprising
      int no = 3*p-4; // didn't make it
      if (p==1) no = 31; // special case when no is negative
      Case[c] = 0;
      for (int i=0;i<N;i++)
	{
	  if(t[i] >= atleast) // made it
            {
	      Case[c] ++;
	      continue;
	    }
	  else if( t[i] >= no) // need to be surprising
            {
	      if (S>0) // can use a surprising
		{
		  S--;
		  Case[c]++; // surprisingly made it
		}
	    }	  
	}
      c++; // next test case
    }

  // done, print output
  ofstream fout("bout",ofstream::out);
  for (int i=1;i<=T;i++)
    {
      fout << "Case #" << i << ": " << Case[i-1] << endl;
    }
  cout << "wrote file bout" << endl;
}
