#include<iostream>
#include<fstream>
#include<cstdlib>
using namespace std;

int main()
{
  ifstream in("A-small-attempt2.in");
  ofstream out("output.txt");

  char str1[]="ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv";
  char str2[]="our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up";
  char maps[26]="";
  maps[0]='y';
  maps[25]='q';
  maps[16]='z';

  for(int i=0;i<strlen(str1);i++)
  {      
	  maps[str1[i]-97]=str2[i];
  }

  char dummy[255];
  in.getline(dummy,255);
  int cases=atoi(dummy);
  int times=1;
  while(times<=cases)
  {
   char in1[255]="";
   char in2[255]="";
   in.getline(in1,255);
   out<<"Case #"<<times<<": ";
   for(int i=0;in1[i]!='\x0';i++)
   {
     out<<maps[in1[i]-97];
   }out<<endl;
   times++;
  }
  
  
  system("pause");
  return 0;
}
