#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>
#include <string>


#define Z size()
#define F(x,y) for(int x=0;x<y;x++)
#define Fn(x,y) for(x=0;x<y;x++)
#define FR(x,y) for(int x=y;x>0;x--)
#define FRn(x,y) for(x=y;x>0;x--)


using namespace std;


int T,ja,jb;

int a[102][2];
int b[102][2];

int ra[202][2];
int rb[202][2];

int conv(string x)
{
     int va=(((x[0]-'0')*10) + (x[1]-'0'))*60 ;
     va+=((x[3]-'0')*10) + (x[4]-'0');
     
     return va;
}


int mn(int &aa, int &bb)
{
  

//duplicate


int n=ja+jb;
int ac=0;
int bc=0;

for(int i=0;i<ja;i++)
  {
   ra[ac][0]=a[i][0];
   ra[ac++][1]=0;           //0=departure. 1=arrival
   
   rb[bc][0]=a[i][1]+T;
   rb[bc++][1]=1;
   }


for(int i=0;i<jb;i++)
  {
   rb[bc][0]=b[i][0];
   rb[bc++][1]=0;           //0=departure. 1=arrival
   
   ra[ac][0]=b[i][1]+T;
   ra[ac++][1]=1;
   }


for(int i=0;i<n;i++)
 for(int j=i+1;j<n;j++)
 {
   if((ra[i][0]>ra[j][0]) || ((ra[i][0]==ra[j][0]) && ra[i][1]==0 && ra[j][1]==1))
   {
     int t=ra[i][0];
     ra[i][0]=ra[j][0];
     ra[j][0]=t;
     
     t=ra[i][1];
     ra[i][1]=ra[j][1];
     ra[j][1]=t;
   }  
   
   

   if((rb[i][0]>rb[j][0]) || ((rb[i][0]==rb[j][0]) && rb[i][1]==0 && rb[j][1]==1))
   {
     int t=rb[i][0];
     rb[i][0]=rb[j][0];
     rb[j][0]=t;
     
     t=rb[i][1];
     rb[i][1]=rb[j][1];
     rb[j][1]=t;
   }  

}

/*
cout<<"---";

for(int i=0;i<n;i++)
  cout<<ra[i][0]<<" - "<<ra[i][1]<<"\n";
  
cout<<"\n";

for(int i=0;i<n;i++)
  cout<<rb[i][0]<<" - "<<rb[i][1]<<"\n";
  
cout<<"***\n";
  
  */








int resa=0;
int resb=0;

int mina=0;
int minb=0;

for(int i=0;i<n;i++)
{ 
   if(ra[i][1]==0) resa--; else resa++;
   if(resa<mina) mina=resa;
   
   if(rb[i][1]==0) resb--; else resb++;
   if(resb<minb) minb=resb;
}


//answer
aa=-mina;
bb=-minb;

}



int main()
{
 
  int outs[102][2];
  
 fstream f("Blarge.in",ios::in);
 int number;
 f>>number; 
 for(int bg=0;bg<number;bg++)// total sets
 {
   f>>T;
   f>>ja>>jb;
   
   ////cout<<"("<<T<<")("<<ja<<")("<<jb<<")\n";
   
          
   for(int i=0;i<ja;i++)
   {
     string x;

     for(int j=0;j<2;j++)
     { f>>x;
       a[i][j]=conv(x);
     }  
   } 
   
   
   for(int i=0;i<jb;i++)
   {
     string x;
     
          
     for(int j=0;j<2;j++)
     { f>>x;
       b[i][j]=conv(x);
     }  
   } 
int aa=0,bb=0;
  mn(aa,bb);
  outs[bg][0]=aa;
  outs[bg][1]=bb;
  
    
}//big for lop for total sets
  
  
 
 f.close();
 
 
 ofstream os("output.txt",ios::out);
 
for(int i=0;i<number;i++)
{
  cout<<"Case #"<<i+1<<": "<<outs[i][0]<<" "<<outs[i][1]<<"\n";
  os<<"Case #"<<i+1<<": "<<outs[i][0]<<" "<<outs[i][1]<<"\n";
  
}

os.close();


 int tp;
 cin>>tp;
 
}







