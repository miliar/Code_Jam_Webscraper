#include<iostream>
#include<fstream>
using namespace std;

char a[6][6];
int n;
bool done=true;
 
string pan()
{
 bool tempX=false;
 bool tempO=false;
 bool p=true;
 bool q=true;

 for(int i=1;i<=4;i++)
   {
    p=true;q=true;
    for(int j=1;j<=4;j++)
      {
        if((a[i][j]!='X')&&(a[i][j]!='T')) p=false;    
        if((a[i][j]!='O')&&(a[i][j]!='T')) q=false;
      }
    if(p) tempX=true;
    if(q) tempO=true;
   }
  
  for(int i=1;i<=4;i++)
   {
    p=true;q=true;
    for(int j=1;j<=4;j++)
      {
        if((a[j][i]!='X')&&(a[j][i]!='T')) p=false;    
        if((a[j][i]!='O')&&(a[j][i]!='T')) q=false;
      }
    if(p) tempX=true;
    if(q) tempO=true;
   }

p=true;q=true;
for(int i=1;i<=4;i++)
{
 if((a[i][i]!='X')&&(a[i][i]!='T')) p=false;   
 if((a[i][i]!='O')&&(a[i][i]!='T')) q=false;
}
if(p) tempX=true;
if(q) tempO=true;
p=true;q=true;
 for(int i=1;i<=4;i++)
{
 if((a[i][5-i]!='X')&&(a[i][5-i]!='T')) p=false;      
 if((a[i][5-i]!='O')&&(a[i][5-i]!='T')) q=false;
}
if(p) tempX=true;
if(q) tempO=true;

   
 if((tempX)&&(tempO)) return "Draw";
   else if((!tempX)&&(!tempO)&&(done)) return "Draw";
    else if(tempX) return "X won";
     else if(tempO) return "O won";
      else if(!done) return "Game has not completed";
}

int main()
{
ifstream inf("A-large.in");
ofstream outf("A-large.out");
 
inf>>n;
 for(int k=1;k<=n;k++)
   {
     done=true;
     for(int i=1;i<=4;i++)
       for(int j=1;j<=4;j++)
         {
          inf>>a[i][j];
          if(a[i][j]=='.') done=false;
         }
            outf<<"Case #"<<k<<": "<<pan()<<endl;
   }
  inf.close();
  outf.close();      
 return 0;
 }
