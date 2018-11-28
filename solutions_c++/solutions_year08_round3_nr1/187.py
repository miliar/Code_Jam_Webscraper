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
#include <string>
#include <fstream>


#define Z size()
#define pb(x) push_back(x)
#define beg begin()
#define F(x,y) for(int x=0;x<y;x++)
#define Fn(x,y) for(x=0;x<y;x++)
#define FR(x,y) for(int x=y;x>0;x--)
#define FRn(x,y) for(x=y;x>0;x--)


using namespace std;

vector <long long>  outs;

vector <long long> fq;
int m,k,l;


int mn()
{
 /////
  
 
   sort(fq.beg,fq.end());
   reverse(fq.beg,fq.end());
   
   
   long long tot=0;
   int ctr=1;
   int mul=1;
   for(int i=0;i<fq.Z;i++)
   {
      tot+=(fq[i]*mul); //cout<<"\n"<<fq[i]<<"*"<<mul;
      ctr++;
      if(ctr>k) {mul++; ctr=1;}
      }
     
  
  

   outs.push_back(tot);//global vector
  
}//function
 







int main()
{
 
 fstream f("Al.in",ios::in);
 int number;
 f>>number; 
 for(int i=0;i<number;i++)// total sets
 { 
  //cout<<i<<".";
  
  fq.clear();
  
  f>>m>>k>>l;


 F(z,l)
 { long long t;
   f>>t;
   fq.pb(t);
 }  
 
 mn();
 }
  
 
 f.close();
 
 ofstream os("output.txt",ios::out);
 
 
 for(int i=0;i<outs.size();i++)
 { cout<<"Case #"<<i+1<<": "<<outs[i]<<"\n";
   os<<"Case #"<<i+1<<": "<<outs[i]<<"\n";
 }
os.close(); 
  

 int y; cin>>y;
   
 
 
}






