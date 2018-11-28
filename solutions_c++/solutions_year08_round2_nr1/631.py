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



using namespace std;

vector <long long>  outs;

struct tree
{long long x; 
 long long y;
 };


long long n,A,B,C,D;
long long x0,ya,M;

void next(tree &t)
{
  t.x = (A*t.x + B)% M;
  t.y = (C*t.y + D)% M;
}



int mn()
{
 int tot=0;
 
 tree temp;
 temp.x=x0; 
 temp.y=ya;
 
  vector <tree> ts;
  for(int i=0;i<n;i++)
  {
     ts.push_back(temp);
     next(temp);
  }   
  
  for(int i=0;i<n;i++)
   for(int j=i+1;j<n;j++)
    for(int k=j+1;k<n;k++)
    {
     if(((ts[i].x+ts[j].x+ts[k].x)%3==0) && ((ts[i].y+ts[j].y+ts[k].y)%3==0)) tot++;  
    }
    
  
  outs.push_back(tot);
  
}//function
 







int main()
{
 
 fstream f("Asm.in",ios::in);
 int number;
 f>>number; 
 for(int i=0;i<number;i++)// total sets
 { 
 f>>n>>A>>B>>C>>D>>x0>>ya>>M;
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











