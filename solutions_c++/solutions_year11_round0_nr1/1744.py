#include <iostream>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <algorithm>

using namespace std;

int main(int argc, char** argv)
{
  int T, N, ocount, bcount;
  long long tottime;
  ifstream input("A-large.in");
  ofstream output("A-large.out");
  int obot_t, obot_t1, obot_x, obot_x1;
  int bbot_t, bbot_t1, bbot_x, bbot_x1;
  char temp;
  //  string* rseq;

  input >> T;
  //Check for the test cases
  for(int i = 0; i < T; i++)
    {
      input >> N;
      obot_x = 1;
      bbot_x = 1;
      obot_t = 0;
      bbot_t = 0;
      obot_t1 = 0;
      bbot_t1 = 0;
      tottime = 0;
      for(int j = 0; j < N; j++)
	{
	  input >> temp;
	  
	  if(temp == 'O')
	    {
	      input >> obot_x1;
	      obot_t = abs(obot_x1 - obot_x) - obot_t1; //travel time
	      if(obot_t < 0)
		obot_t = 1; //time to push
	      else
		obot_t += 1;
	      
	      obot_t1 = 0;
	      bbot_t1 += obot_t;
	      obot_x = obot_x1;	      
	      tottime += obot_t;
	      //obot_t = 0;
	    }
	  else
	    {
	      input >> bbot_x1;
	      bbot_t = abs(bbot_x1 - bbot_x) - bbot_t1;
	      if(bbot_t < 0)
		bbot_t = 1; //time to push
	      else
       		bbot_t += 1;
	      
	      bbot_t1 = 0;
	      obot_t1 += bbot_t;
	      bbot_x = bbot_x1;	      
	      tottime += bbot_t;
	      //bbot_t = 0;
	    }
	}
      output<<"Case #"<<i+1<<": "<<tottime<<endl;
    }
  return 0;
}
