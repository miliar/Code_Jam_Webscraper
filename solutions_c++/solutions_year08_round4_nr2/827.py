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
#define F(x,y) for(long long x=0;x<y;x++)
#define Fn(x,y) for(x=0;x<y;x++)
#define FR(x,y) for(int x=y;x>0;x--)
#define FRn(x,y) for(x=y;x>0;x--)


using namespace std;

vector <long long>  outs;

vector <long long> x2,y2,x3,y3;
//vector <long long> b;

long long a,m,n;







int mn()
{
  
   if(a>2500) {x2.push_back(-1); y2.push_back(-1); x3.push_back(-1); y3.push_back(-1);return -1;} ///small
   
   F(i,n+1)
   F(j,m+1)
   F(k,n+1)
   F(l,m+1)
   {
     long long h=(i*l)-(j*k);
     h=h>0?h:0-h;
     if(h==a)
     {x2.push_back(i); y2.push_back(j); x3.push_back(k); y3.push_back(l); return 1;}
     
   }
   
   
x2.push_back(-1); y2.push_back(-1); x3.push_back(-1); y3.push_back(-1);return -1; ///small      
     
    
   
   
  
}//function
 







int main()
{
 
 fstream f("in.in",ios::in);
 long long number;
 f>>number; 
 for(long long i=0;i<number;i++)// total sets
 { 
  cout<<i<<".";
   f>>n>>m>>a;

/* 
 F(z,n)
 { long long t;
   f>>t;
   a.pb(t);
 }  
 F(z,n)
 { long long t;
   f>>t;
   b.pb(t);
 }
   
*/
 
 mn();
 }
  
 
 f.close();
 
 ofstream os("output.txt",ios::out);
 
 
 for(int i=0;i<x2.size();i++)
 { 
   os<<"Case #"<<i+1<<": ";
   if(x2[i]!=-1)
       os<<"0 0 "<<x2[i]<<" "<<y2[i]<<" "<<x3[i]<<" "<<y3[i];
   else os<<"IMPOSSIBLE";
   os<<"\n";
   
   cout<<"Case #"<<i+1<<": ";
   if(x2[i]!=-1)
       cout<<"0 0 "<<x2[i]<<" "<<y2[i]<<" "<<x3[i]<<" "<<y3[i];
   else cout<<"IMPOSSIBLE";
   cout<<"\n";
 
 }
 
os.close(); 
  

 int y; cin>>y;
   
 
 
}











