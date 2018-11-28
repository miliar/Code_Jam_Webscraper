#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <vector>
#include <list>
#include <algorithm>
#include <cstring>

typedef unsigned long long ull;

using namespace std;

int main()
{
  int _N;
  cin >> _N;

  char S[1005];
  char S2[1005];
  int k;
  int P[5];

  for (int _n=0; _n<_N; _n++)
    {
      cout << "Case #" << _n+1 << ": ";

      scanf(" %d\n%s\n",&k,S);

      for (int i=0; i<k; i++)
	P[i]=i;

      int l=strlen(S);
      int sol=-1;
      int c;
      do
	{
	  for (int i=0; i<l; i+=k)
	    {
	      for (int j=0; j<k; j++)
		{
		  S2[i+j]=S[i+P[j]];
		}
	    }
	  c=0;
	  char prev='-';
	  for (int i=0; i<l; i++)
	    {
	      if (S2[i]!=prev)
		{
		  c++;
		  prev=S2[i];
		}
	    }
	  if (sol==-1)
	    sol=c;
	  else
	    {
	      if (c<sol)
		sol=c;
	    }

	} while (next_permutation(P,P+k));

      cout << sol;

      cout << endl;
    }

  return 0;
}
