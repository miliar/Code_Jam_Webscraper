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


string engines[102];
int engdone[102];
string q[1002];

int ne,nq;


int checkzero()
{
  for(int i=0;i<ne;i++)
    if(engdone[i]==0)
      return -1;

return 1;
}
   
  

int fn()
{

//all the arrays and array sizes are already perfect when it comes here
 int tot=0;

  for(int i=0;i<102;i++) engdone[i]=0;
  
  ////int dun=0;
  
    
   for(int i=0;i<nq;i++)
   {
     int xe;
     for(int j=0;j<ne;j++)
      if(engines[j]==q[i]){xe=j; break;}
     if(engdone[xe]==1) continue;
     
     engdone[xe]=1; //reverse?
     int z=checkzero();
     if(z==-1) continue;
     return i;
   } 
         
   return -1; 
  
}


int mn()
{
 //data entry already done when it comes to this function.
 int tot=0;
 
 
 int dun=0;
 
 while(dun==0)
 {
 int rf=fn();
 
 
 /*just for test */if(rf==0) cout<<"something is wierd";
 
 
 if (rf==-1)
  {
   ///tot++;
   dun=1;
   return tot;
  }
 else
  {
   //make array from i onwards (included) ....call fn[calling will happen automatically in next iteration of while]
  
    for(int i=0;i<(nq-rf);i++)
      q[i]=q[i+rf];
    nq=nq-rf;
    tot++;
    dun=0;
   
  }//else 
 
 }//while 
 
 cout<<"AA";
 return tot;
 
}
  
  
  
int main()
{
 
 int outs[22];
 fstream f("Asmall.in",ios::in);
 int number;
 f>>number; 
 for(int i=0;i<number;i++)// total sets
 {
    f>>ne;
        
   
      string extr;
      getline(f,extr);

        
    for(int j=0;j<ne;j++)
     {
     getline(f,engines[j]);
     }
    
    f>>nq;
    
    getline(f,extr);    
    for(int j=0;j<nq;j++)
     {
      getline(f,q[j]);
     }
          
    int xo=mn();
    
    outs[i]=xo;
    
}    
    
 
 
 f.close();
 
 
 ofstream os("output.txt",ios::out);
 
for(int i=0;i<number;i++)
{
  cout<<"Case #"<<i+1<<": "<<outs[i]<<"\n";
  os<<"Case #"<<i+1<<": "<<outs[i]<<"\n";
}

os.close();

  



 int y; cin>>y;
   
 
 
 
/* 
 fstream f("test1.txt",ios::in);

 cin>>ne;
 for(int i=0;i<ne;i++)
  cin>>engines[i];
 

 cin>>nq;
 for(int i=0;i<nq;i++)
   cin>>q[i];
   
   int r=mn();
   cout<<"\n"<<r;
   
   
   int y;
   cin>>y;
  */
   
}
   
  
  
  
  
  
  

