#include <iostream.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <fstream.h>

#define lmax 15
#define dmax 5000

int L, D, N;
char Words[dmax][lmax], Patterns[100*lmax];

int findNumWords(char *w, char *p) 
{
 char hash[26];
 int i = 0;
 
 for (int token = 0; token < L; token++) 
 {
  memset(hash, 0, sizeof(hash));
  if (p[i] == '(') 
  {
	i++;
	while (p[i] != ')')
	 hash[p[i++] - 'a'] = 1;
	 ++i;
  }
  else 
   hash[p[i++] - 'a'] = 1;
  
  if (!hash[w[token] - 'a'])
	return 0;
  }
  return 1;
}

int solve()
{
 int WMP = 0;
 for (int i = 0; i < D; i++) 
 {
  if (findNumWords(Words[i], Patterns))
	WMP++;
 }
 return WMP;
}

int main()
{
 ifstream fin("A-large.in");
 ofstream fout("A-large.out");

 fin>>L>>D>>N;
 
 for (int i = 0; i < D; i++)
  fin>>Words[i];

 for (int c = 1; c <= N; c++) 
 {
  fin>>Patterns;
  fout<<"Case #"<<c<<": "<<solve()<<endl;
 }

 fin.close();
 fout.close();
 
 return 0;
}