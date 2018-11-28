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

vector <long long> a;
//vector <long long> b;



int mn()
{
 
  long long tot=1;
  vector <long long> n;
  
  for(int i=0;i<a.Z;i++) n.pb(1);
  
  
  for(int i=1;i<a.Z;i++)
   {
    for(int j=0;j<i;j++)
     if(a[i]>a[j]) {n[i]+=n[j]; n[i]%=1000000007;}
     
     
    tot+=n[i];
    tot%=1000000007;
   } 
   
    
  
   outs.push_back(tot);//global vector
  
}//function
 

int main()
{
 
 fstream f("Cs.in",ios::in);
 int number;
 f>>number; 
 vector <long long> ar;
 for(int i=0;i<number;i++)// total sets
 { 
  //cout<<i<<".";
  
  a.clear();
  ar.clear();
  
  long long na,ma,Xa,Ya,Za;
  f>>na>>ma>>Xa>>Ya>>Za;
  
   
   
 F(z,ma)
 { long long t;
   f>>t;
   ar.pb(t);
 } 
 
 
 for (int q=0;q<na;q++) 
 {
  a.push_back(ar[q%ma]);
  ar[q%ma]=(Xa*ar[q%ma] + Ya*(q+1))% Za;
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











