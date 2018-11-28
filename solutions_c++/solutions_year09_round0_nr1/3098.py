#include <iostream.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <fstream.h>

#define lmaximum 15
#define dmaximum 5000

int l, d, n;
char Words[dmaximum][lmaximum], Patterns[100*lmaximum];

int searchWords(char *a, char *b) 
{
 char hash[26];
 int i = 0;
 
 for (int q = 0; q < l; q++) 
 {
  memset(hash, 0, sizeof(hash));
  if (b[i] == '(') 
  {
	i++;
	while (b[i] != ')')
	 hash[b[i++] - 'a'] = 1;
	 ++i;
  }
  else 
   hash[b[i++] - 'a'] = 1;
  
  if (!hash[a[q] - 'a'])
	return 0;
  }
  return 1;
}

int solve()
{
 int W = 0;
 for (int i = 0; i < d; i++) 
 {
  if (searchWords(Words[i], Patterns))
	W++;
 }
 return W;
}

int main()
{
 ifstream fin("A-large.in");
 ofstream fout("A-large.out");

 fin>>l>>d>>n;
 
 for (int i = 0; i < d; i++)
  fin>>Words[i];

 for (int c = 1; c <= n; c++) 
 {
  fin>>Patterns;
  fout<<"Case #"<<c<<": "<<solve()<<endl;
 }

 fin.close();
 fout.close();
 
 return 0;
}