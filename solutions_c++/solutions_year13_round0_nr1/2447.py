#include<iostream>
#include <fstream>

using namespace std;

char a[4][4];

char checkRows()
{
char v;
int dot=0;

for(int i=0;i<4;i++)
{
  v='T';
  for(int j=0;j<4;j++)
  {
      if(a[i][j]=='.')
         {
        dot =1;
        v='T';
        break;
        }
      if(v=='T' || a[i][j]=='T')
        v= v=='T'?a[i][j]:v;
      else if(v!=a[i][j])
       {
         v='T';
         break;
         }
  }
  if(v!='T')
   return v;
}
if(dot==1)
  return 'U';
return 'T';
}


char checkCols()
{
char v;
int dot=0;

for(int j=0;j<4;j++)
{
  v='T';
	for(int i=0;i<4;i++)  
  {
      if(a[i][j]=='.')
         {
        dot =1;
        v='T';
        break;
        }
      if(v=='T' || a[i][j]=='T')
        v= v=='T'?a[i][j]:v;
      else if(v!=a[i][j])
       {
         v='T';
         break;
         }
  }
  if(v!='T')
   return v;
}
if(dot==1)
  return 'U';
return 'T';
}

char checkDiags()
{
char v='T';
int dot=0;

for(int i=0;i<4;i++)
{
   if(a[i][i]=='.')
    { dot=1;
    v='T';
     break;
     }
   else if(v=='T' || a[i][i]=='T')
     {
     v= v=='T'?a[i][i]:v;
     }
   else if(v!=a[i][i])
       {
         v='T';
         break;
         }  
}

if(v!='T')
   return v;

v='T';
for(int i=0;i<4;i++)
{
   if(a[i][3-i]=='.')
    { dot=1;
    v='T';
     break;
     }
   else if(v=='T' || a[i][3-i]=='T')
   {
     v= (v=='T')?a[i][3-i]:v;
     }
   else if(v!=a[i][3-i])
       {
         v='T';
         break;
         }  
}

if(v!='T')
   return v;

if(dot==1)
  return 'U';
  
return 'T';

}

int main(){
ifstream myInputFile ("../Downloads/A-small-attempt1.in");
ofstream myOutputFile;
myOutputFile.open ("output.txt");

int t;
myInputFile>>t;
//getline(myInputFile,t);

for(int i=1;i<=t;i++)
{

myInputFile>>a[0];
myInputFile>>a[1];
myInputFile>>a[2];
myInputFile>>a[3];

myOutputFile<<"Case #"<<i<<": ";
char a1=checkRows();
if(a1!='T' && a1!='U')
  myOutputFile<<a1<<" won";
else 
{
char a2=checkCols();
  if(a2!='T' && a2!='U')
  myOutputFile<<a2<<" won";
  
  else {
  char a3=checkDiags();
  if(a3!='T' && a3!='U')
  myOutputFile<<a3<<" won";
  else if(a1=='U' || a2=='U' || a3=='U')
    myOutputFile<<"Game has not completed";
  else
    myOutputFile<<"Draw";
    
//  myOutputFile<<a1<<","<<a2<<","<<a3;  
  }
}
 myOutputFile<<endl; 
}

  myOutputFile.close();
}
