#include <iostream>

using namespace std;

// Kikou les gens !
int main(int argc, char **argv) {
    
    int nbtests;
    cin >> nbtests;
  
    int N;
    int S;
    int p;
    for (int test = 0; test < nbtests; test++)
    {
      cin >> N;
      cin >> S;
      cin >> p;
      
      int result = 0;
      int SommeMini = 3*p-4;
      int SommeMiniSansSurprise = 3*p-2;
      int ti;
      
      if(p == 0)
      {
	result = N;
	for (int i = 0; i < N; i++)
	  cin >> ti;
      }
      else if(p == 1)
      {
	for (int i = 0; i < N; i++)
	{
	  cin >> ti;
	  if(ti > 0)
	    result++;
	}
	
      }
      else
      {
	for (int i = 0; i < N; i++)
	{
	  cin >> ti;
	  if(ti == SommeMini || ti == (SommeMini+1))
	  {
	    if(S > 0)
	    {
	      S--;
	      result++;
	    }
	  }
	  else if (ti >= SommeMiniSansSurprise)
	  {
	    result++;
	  }

	}
      }
      
      cout << "Case #" << test+1 << ": " << result << endl;
      
    }
    
    return 0;
}
