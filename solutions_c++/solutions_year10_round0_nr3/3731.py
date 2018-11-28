#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric> 
#include <list>
#include <fstream>
#include <cstdlib>
#include <string>
#include <sstream>
using namespace std;


int main()
{
 int Rounds,K,sGroup;
 int money = 0,sum = 0,temp = 0,i;
 list< int > batch;
 vector<string> tokens;
 string buff;

 string line;
 ifstream INP ("input");
 ofstream OUP("output");

 getline(INP,line);
 int TestCases = atoi(line.c_str()); 
 int test = TestCases;

while(TestCases != 0)
{
  money = 0,sum = 0,temp = 0;
  batch.clear();
  tokens.clear();
  getline(INP,line);
  stringstream ss(line);
  
  ss>>buff;
  Rounds = atoi(buff.c_str());
  ss>>buff;
  K = atoi(buff.c_str());
  ss>>buff;
  sGroup = atoi(buff.c_str());

  tokens.clear();
 
  getline(INP,line);
  stringstream ss1(line);

  while(ss1>>buff)
  {
    sum = sum + atoi(buff.c_str());
    batch.push_back(atoi(buff.c_str()));
  }

  printf("\n Rounds...K...sGroup...  %d   %d    %d  ",Rounds,K,sGroup);


 if(sum <= K)
  money = sum*Rounds;
 else{
 
  temp = 0;

 while(Rounds > 0)
 {
   if(temp + batch.front() <= K)
     {
     temp += batch.front();
     i = batch.front();
     batch.push_back(i);
     batch.pop_front();
     money += i;
     }
  else
    {
      Rounds--;
      temp = 0;
    }
 }
   
  } 
 
 OUP<< "\nCase #"<<test-TestCases+1<<": "<< money;
 TestCases--; 
}

INP.close();
OUP.close();
return 0;
}
