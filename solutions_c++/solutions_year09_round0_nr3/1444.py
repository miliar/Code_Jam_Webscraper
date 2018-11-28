#include <stdio.h>
#include <string>
#include <vector>
#include "stdlib.h"

using namespace std;
int LL,K,N;

string s;
vector<string> strs;
string st;
int A[501][501];

int main()
{

  st = "welcome to code jam";
  FILE* f = fopen("in.in", "r");
  FILE* out = fopen("out.out", "w");

  char c;
  fscanf(f, "%d", &K);
  fgetc(f);
  for (int io=0; io<K; io++)
  {
    s="";
    
    while((c=fgetc(f))!='\n' && c!=EOF)
    {
      s+=c;
    }
    for (int k=0; k<501; k++)
      for (int l=0; l<501; l++)
	A[k][l] = 0;
    A[0][0] = 1;
    for (int i = 0; i < s.size(); i++)
    {
      for (int j = 0; j <= st.size(); j++)
	A[i + 1][j] = A[i][j];
      for (int j = 0; j < st.size(); j++)
	if (s[i] == st[j])
	  A[i + 1][j + 1] = (A[i + 1][j + 1] + A[i][j])%10000;
    }
    fprintf(out,"Case #%d: %d%d%d%d\n",io+1,A[s.size()][st.size()]/1000,
	    A[s.size()][st.size()]/100%10,
	    A[s.size()][st.size()]/10%10,
	    A[s.size()][st.size()]%10);

  }
  

fclose(out);
   fclose(f);
   return 0;
}