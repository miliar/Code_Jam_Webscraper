#include <iostream>
#include <fstream>

using namespace std;

int main()
{
  ofstream f_output("output");
  ifstream f_input("input");
  string x;
  int L, D, N;
  f_input >> L;
  f_input >> D;
  f_input >> N;
  string arrL[16];
  string arrD[5001];
  string arrN[501];
  int Case[501];
  for (int i=1; i<=D; i++)
    {
      f_input >> x;
      arrD[i] = x;
      cout << arrD[i] << endl;
    }

  for (int i=1; i<=N; i++)
    {
      f_input >> x;
      arrN[i] = x;
      cout << arrN[i] << endl;
    }
  cout << "=====================" << endl;
  int zgadzajace_sie=0;
  int i=0;
  for (int iN=1; iN<=N; iN++)
    {
      for (int iD=1; iD<=D; iD++) //słowa
	{
	  for ( int iL=0; iL<L; iL++) //znaki
	    {
	      //cout << arrN[iN][i] << endl;
	      while ( arrN[iN][i] == '(' )
		{
		  i++;
		  while ( arrN[iN][i] != ')' )
		    {
		      cout << arrN[iN][i] << endl;
		      if ( arrN[iN][i] == arrD[iD][iL] )
			{
			  cout << "arrN " << arrN[iN] << " " << i << endl;
			  cout << "arrD " << arrD[iD] << " " << iL << endl;
			  zgadzajace_sie++;
			}
		      i++;
		    }
		  i++;
		  iL++;
		}
		      while ( arrN[iN][i] == arrD[iD][iL] && arrN[iN][i] )
			{
			  cout << "arrN " << arrN[iN] << " " << i << endl;
			  cout << "arrD " << arrD[iD] << " " << iL << endl;
			  zgadzajace_sie++;
			  iL++;
			  i++;
			}
	      i=0;
	      cout << "~~~~~~~~~~~~~~~zgadajace_sie " << zgadzajace_sie << endl;
	      if ( zgadzajace_sie == L )
		Case[iN]++;
	      zgadzajace_sie=0;
	    }
	}
    }
  for (int i=1; i<=N; i++)
    {
      cout << "Case #" << i << ": " << Case[i] << endl;
      f_output << "Case #" << i << ": " << Case[i] << endl;
    }
return 0;
}
