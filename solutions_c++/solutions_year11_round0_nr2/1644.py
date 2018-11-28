#include <iostream>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <algorithm>

using namespace std;

int main(int argc, char** argv)
{
  int T, C, D, N, flen;
  ifstream input("B-large.in");
  ofstream output("B-large.out");
  string* combo;
  string* oppo;
  string wand, fcharm, temp1, temp2, ftemp;
  string sout;
  size_t found;
  bool combo_call;

  input >> T;
  //Check for the test cases
  for(int i = 0; i < T; i++)
    {
      input >> C; //0 possible
      if(C != 0)
	{
	  combo = new string[C];          
	  for(int j = 0; j < C; j++)
	    input >> combo[j];
	}
      input >> D; //0 possible
      if(D != 0)
	{
	  oppo = new string[D];          
	  for(int j = 0; j < D; j++)
	    input >> oppo[j];
	}
      input >> N;
      input >> wand;
      fcharm = "";
      //prepare final charm
      for(int j = 0; j < N; j++)
	{
	  fcharm = fcharm + wand[j];	  
	  combo_call = false;

	  //check for combo in the fcharm list
	  if(fcharm.length() > 1 && C!=0)
	    {
	      ftemp = fcharm.substr(fcharm.length()-2,2);       
	      for(int k = 0; k < C; k++)
		{
		  temp1 = combo[k].substr(0,1) + combo[k].substr(1,1);
		  temp2 = combo[k].substr(1,1) + combo[k].substr(0,1);
		  if(ftemp == temp1 || ftemp == temp2)
		    {
		      ftemp = combo[k].substr(2,1);
		      combo_call = true;;
		      break;			  
		    }
		}
	      fcharm = fcharm.substr(0,fcharm.length()-2) + ftemp;
	    }
	  
	  //check for oppo in the fcharm list
	  if(fcharm.length() > 1 && D != 0 && !(combo_call))
	    {
	      //check for opposing elements in the list
	      for(int k = 0; k < D; k++)
		{
		  temp1 = oppo[k].substr(0,1);  
		  temp2 = oppo[k].substr(1,1);
		  if(fcharm.find(temp1) != string::npos && fcharm.find(temp2) != string::npos)
		    {
		      fcharm = "";
		      break;
		    }
		}	      
	    }	  	  
	}
      
      flen = fcharm.length();
      sout = "[";
      for(int k = 0; k < flen-1; k++)
	sout = sout + fcharm[k]+", ";
      
      if(flen > 0) sout = sout + fcharm[flen-1]+"]";
      else sout = sout + "]";

      output<<"Case #"<<i+1<<": "<<sout<<endl;
      
      if(C !=0) delete[] combo;
      if(D !=0) delete[] oppo;	  
    }
  return 0;
}
