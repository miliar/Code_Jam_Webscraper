#include <iostream.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <fstream.h>
#include <stdlib.h>

#define MD 10

int p;

void init (int T[])
{
 for (int i=0; i<9; i++)
  T[i] = 0;
}

void count(char Num[], int T[])
{
 for (unsigned int i = 0; i <strlen(Num); i++)
  T[Num[i] - '0' - 1]++;
}

int match(int A[], int B[])
{
 for (int i = 0; i<9; i++)
  if (A[i] != B[i])
   return 0;

 return 1;
}

long next (long N)
{
 int Digits[9], tDigits[9];
 long int i = N+1;
 char t[MD]; 
 
 ltoa(N, t, 10);
 init(Digits);
 count(t, Digits);
  
 do
 {
  init(tDigits);
  ltoa(i, t, 10);
  count(t, tDigits);
  i++;
 }
 while(!match(Digits, tDigits));
 
 return (i - 1);
}

int main()
{
 ifstream fin("B-small-attempt0.in");
 ofstream fout("B-small-attempt0.out");
 
 int T;
 long int N, ans;

 fin>>T;
  
 for (p = 1; p <= T; p++)
 {
  fin>>N;
  ans = next(N);
  
  fout<<"Case #"<<p<<": "<<ans<<endl;
 }

 fin.close();
 fout.close();
 
 return 0;
}