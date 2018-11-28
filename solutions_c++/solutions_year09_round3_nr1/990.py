#include <iostream.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <fstream.h>
#include <math.h>

#define Replace 45
#define MaxLength 10

int Order [] = { 1, 0, 2, 3, 4, 5, 6, 7, 8, 9 };
int next = 0;
int Base = 0;

int countDistinct(string Case, string &Temp)
{
 int distinct = 0; 
 next = 0;
  
 for (unsigned int i = 0; i<Case.length(); i++)
 {
  while (Case[i] == '-')
   i++;
  for (int j = i+1; j<Case.length(); j++)
   if (Case[i] == Case[j])
   {
    Case[j] = '-';  
	Temp[j] = Order[next] + 48;
   }
  Temp[i] = Order[next] + 48;
  next++;
 }
 
 for (unsigned int i = 0; i<Case.length(); i++)
 {
  if (Case[i]!='-')
   distinct++;
 }
 return distinct;
}

string solve(string Case)
{
 string temp = Case;
 Base = countDistinct(Case, temp);
 if (Base == 1)
  Base = 2;
 return temp;
}

int main()
{
 ifstream fin("A-small-attempt1.in");
 ofstream fout("A-small-attempt1.out");
 
 int T;
 unsigned long int ans;
 string Case, temp;

 fin>>T;
 
 for (int c = 1; c <= T; c++) 
 {
  fin>>Case;
  temp = solve(Case);
    
  ans = 0;
  for (int j = temp.length()-1, power = 0; j>=0; j--)
  {
   ans+=(pow(Base, power) * (temp[j] - 48));
   power++;
  }
  
  fout<<"Case #"<<c<<": "<<ans<<endl;
 }

 fin.close();
 fout.close();
 
 return 0;
}