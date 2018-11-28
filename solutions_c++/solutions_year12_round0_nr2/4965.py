#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>

using namespace std;

int main()
{
  char notsurp[31][11], surp[31][11];
  int i, j, k;
  int scorebuf[100];
//  char notsurppresent[31];

  for(i = 0; i < 31; i++)
  {
    for(j = 0; j < 11; j++)
    {
      if(i >= 3*j - 2 && i <= 3*j + 2)
	notsurp[i][j] = 1;
      else
	notsurp[i][j] = 0;

      if(i >= 3*j - min(4,i+2) && i <= 3*j + min(4,30-i+2))
	surp[i][j] = 1;
      else
	surp[i][j] = 0;
    }
  }

  char notsurpatleast[31][11], surpatleast[31][11];
  
  char hadhigher[2];
  
  for(i = 0; i < 31; i++)
  {
    hadhigher[0] = 0;
    hadhigher[1] = 0;
    for(j = 10; j >= 0; j--)
    {
      if(hadhigher[0])
      {
	notsurpatleast[i][j] = 1;
      }
      else
      {
	if(notsurp[i][j] == 1)
	{
	  notsurpatleast[i][j] = 1;
	  hadhigher[0] = 1;
	}
	else
	{
	  notsurpatleast[i][j] = 0;
	}
      }
      
      if(hadhigher[1])
      {
	surpatleast[i][j] = 1;
      }
      else
      {
	if(surp[i][j] == 1)
	{
	  surpatleast[i][j] = 1;
	  hadhigher[1] = 1;
	}
	else
	{
	  surpatleast[i][j] = 0;
	}
      }
    }
  }
/*
  for(i = 0; i < 31; i++)
  {
    for(j = 0; j < 11; j++)
    {
      cout << (int)surp[i][j] << " ";
    }
    cout << endl;
  }
*/  
  int T, N, S, p;
  ifstream input;
  ifstream output;
  input.open("/home/baran/projects/prjs/02/B-large.in");

  string line;
  istringstream linestream;
  input >> T;
  getline(input, line);
//  cout << T << endl;

  int rslt;
  
  for(i = 0; i < T; i++)
  {
    rslt = 0;
    getline(input, line);
//    cout << line << endl;
    linestream.clear();
    linestream.str(line);
    linestream >> N >> S >> p;
    for(j = 0; j < N; j++)
      linestream >> scorebuf[j];
/*    for(j = 0; j < 30; j++)
      notsurppresent[j] = 0;*/
    
    for(j = 0; j < N; j++)
    {
      if(notsurpatleast[scorebuf[j]][p])
      {
	rslt++;
      }
      else
      {
	if(S > 0 && surpatleast[scorebuf[j]][p])
	{
	  rslt++;
	  S--;
	}
      }
    }
    
    cout << "Case #" << i+1 << ": " << rslt << endl;
  }
  
  input.close();
}