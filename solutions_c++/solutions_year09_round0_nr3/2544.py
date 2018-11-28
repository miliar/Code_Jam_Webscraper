#include <iostream>
#include <string>
#include <set>
#include <fstream.h>
#include <string.h>
#include <stdlib.h>

using namespace std;

int start = 0;
const string welcome = "welcome to code jam";

string buffResult(int count)
{
 char temp[4];
 itoa(count, temp, 10);
 
 string ret (temp);
 while (ret.length()!=4)
  ret.insert(start, 1, '0');
  
 return ret;
}

int countOccurences(string input, string Pattern, string BuildPattern)
{
 int count = 0;
  
 if (Pattern.length() <= 0)
 {
  reverse(BuildPattern.begin(), BuildPattern.end());
  if (BuildPattern == welcome)
   return 1;
  else
   return 0;
  }
  
 for (unsigned int i = 0; i<input.length(); i++)
 {
  if (Pattern[0] == input[i])
  {
   BuildPattern.insert(start, 1, input[i]);
   count += countOccurences(input.substr(i+1), Pattern.substr(1), BuildPattern)%10000;
   BuildPattern.erase(start, 1);
  }  
 }
 
 return count;
}

int main() 
{
  ifstream fin("C-small-attempt0.in");
  ofstream fout("C-small-attempt0.out");

  int N;
  string input, Pattern = "welcome to code jam", BuildPattern;
  
  getline(fin, input, '\n');
  N = atoi(input.c_str());
  
  for (int c = 0; c < N; c++)
  {
   getline(fin, input, '\n');
   fout<<"Case #"<<c+1<<": "<<buffResult(countOccurences(input, Pattern, BuildPattern))<<endl;
 }
 
 fin.close();
 fout.close();

 return 0;
}