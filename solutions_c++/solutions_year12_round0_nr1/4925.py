//*** Problem A - Speaking in Tongues
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int T,N;     
char L[26];
char s1[100],s2[100];
int l;

int main()
{
 string line;     

 for (int i=0;i<26;i++)  L[i]=0;
 
 //READ THE SAMPLES (INITIALIZATION)

 L['a'-97]='y'; // a->y
 L['o'-97]='e'; // o->e
 L['z'-97]='q'; // z->q
 L['q'-97]='z'; // z->q (the missing character)

 ifstream fin1 ("input1.in");
 ifstream fin2 ("input2.in");

 fin1>>line; //No. of test cases
 
 cout<<line<<endl;
 T = atoi(line.c_str());

 for (int i=0;i<T+1;i++)
 {
  fin1.getline(s1,'endl');
  fin2.getline(s2,'endl');
  l=strlen(s1);
  for (int j=0;j<l;j++)
   if ((s1[j]>=97)&&(s1[j]<122))                
     L[s1[j]-97]=s2[j];
}

 for(int i=0;i<26; i++)
  cout<<char(i+97)<<"-"<<L[i]<<endl;

fin1.close();
fin2.close();


//SOLUTION
ifstream fin ("input.in");
ofstream fout ("output");

cout<<line<<endl;
T = 30;

fin.getline(s1,'endl');//dummy read;

for (int i=0;i<T;i++)
 {
  fin.getline(s1,'endl');

  l=strlen(s1);

  for (int j=0;j<l;j++)
   if ((s1[j]>=97)&&(s1[j]<=122))                
     s2[j]=L[s1[j]-97];
   else
    s2[j]=s1[j];

  s2[l]='\0';  
  fout<<"Case #"<<i+1<<": "<<s2<<endl;
 }

fin.close();
fout.close();

system("pause");

 }

