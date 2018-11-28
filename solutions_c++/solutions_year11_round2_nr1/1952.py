#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <algorithm>
#include <cmath>

using namespace std;

string convertInt(int number)
{
    if (number == 0)
        return "0";
    string temp="";
    string returnvalue="";
    while (number>0)
    {
        temp+=number%10+48;
        number/=10;
    }
    for (int i=0;i<temp.length();i++)
        returnvalue+=temp[temp.length()-i-1];
    return returnvalue;
}

int main(int argc, char** argv)
{
  int T, N;
  string* sched;
  double* winp;
  double* owp;
  double* oowp;
  double* oppwp;
  size_t shead;
  double wing,totg,rpi,opponent;
  ifstream input("A-large.in");
  ofstream output("A-large.out");
  string str0,str1,strdot;

  input >> T;
  for(int i = 0; i < T; i++)
    {
      input >> N;
      sched = new string[N];
      winp = new double[N];
      owp = new double[N];
      oowp = new double[N];
      oppwp = new double[N];
      str0 = "0";
      str1 = "1";
      strdot = ".";
      for(int j = 0; j < N; j++)
	input >> sched[j];

      for(int j = 0; j < N; j++)
	{
	  totg = 0;
	  wing = 0;	  
	  for(int l = 0;l < N; l++)
	    {
	      shead = l;
	      if(sched[j].compare(shead,1,str0) == 0) 
		totg++;
	      else if(sched[j].compare(shead,1,str1) == 0)
		{
		  totg++;
		  wing++;
		}			      	     
	    }
	  winp[j] = wing/totg;
	}

      for(int j = 0; j < N; j++)
	{
	  opponent = 0;

	  for(int l = 0;l < N; l++)
	    {
	      if(l != j && sched[l].compare(j,1,strdot) != 0)
		{
		  totg = 0;
		  wing = 0;
		  shead = 0;
		  while(shead < N)
		    {
		      if(shead != j)
			{
			  if(sched[l].compare(shead,1,str0) == 0) 
			    totg++;
			  else if(sched[l].compare(shead,1,str1) == 0)
			    {totg++;wing++;}			      	     
			}		      
		      shead++;
		    }
		  oppwp[l] = wing/totg;
		  opponent++;
		}
	    }	  
	  
	  owp[j] = 0;
	  for(int l = 0;l < N; l++)
	    {
	      if(l != j && sched[l].compare(j,1,strdot) != 0)
		owp[j] = owp[j] + oppwp[l];		
	    }  
	  owp[j] = owp[j]/opponent;
	}

      for(int j = 0; j < N; j++)
	{
	  oowp[j] = 0;
	  opponent = 0;
	  for(int l = 0;l < N; l++)
	    {
	      if(l != j && sched[l].compare(j,1,strdot) != 0)
		{
		  oowp[j] = oowp[j] + owp[l];		
		  opponent++;
		}
	    }
	  oowp[j] = oowp[j] / opponent;
	}
         
      output<<"Case #"<<i+1<<": "<<endl;

      for(int j = 0; j < N; j++)
	{
	  rpi = 0.25*winp[j] + 0.50*owp[j] + 0.25*oowp[j];
	  output<<fixed<<setprecision(6)<<rpi<<endl;
	}
      delete[] sched;
      delete[] winp;
      delete[] owp;
      delete[] oowp;
      delete[] oppwp;
    }
 
  return 0;
}


