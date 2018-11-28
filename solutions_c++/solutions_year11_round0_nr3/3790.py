#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> mas;
char buff[100];

int main()
{
 ifstream read; read.open("input.in");
 ofstream f; f.open("output.in");

 int size;
 
 read>>size;

 for(int j=0;j<size;++j) 
 {
  int n;
 int value;
  read>>n;
  read>>value;
  mas.push_back(value);
  for(int i=1;i<n;++i)
  {
   int x;
   read>>x; 
   mas.push_back(x);
   value^=x;
  }

  if(value!=0) 
  {
   string str = "";
   str += "Case #";
   str += itoa(j+1,buff,10);
   str += ": NO";
   str += "\n";
   f<<str;
  } 
  else
  {
   int sum = 0;
   int min = 1000000;
   for(int i=0;i<mas.size();++i)
   {
    if(min>mas[i])
     min = mas[i];
    sum+=mas[i];
   }
   sum -= min;

   string str = "";
   str += "Case #";
   str += itoa(j+1,buff,10);
   str += ": ";
   str += itoa(sum,buff,10);
   str += "\n";
   f<<str;
  }

  mas.clear();
 }

 return 0;
}