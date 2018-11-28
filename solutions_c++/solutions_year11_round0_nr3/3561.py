#include<iostream>
#include<fstream>
#include<vector>
#include<deque>
#include<cstdlib>
#include<cctype>
#include<map>
#include<bitset>
using namespace std;
#define sz 21
unsigned long long min(unsigned long a,unsigned long b)
{ return a<b?a:b; }
int main()
{
    fstream fin("C.in",ios::in);
    fstream fout("C.out",ios::out);
    
    int tests,i,j,n;
    unsigned long long total=0;
     
    fin>>tests;
    vector<bitset<sz> > bv;
    vector<unsigned long> v;
    int sum[sz];
    unsigned long x;
    for(int test=1;test<=tests;test++)
    { 
     for(i=0;i<sz;i++) sum[i]=0;
     v.clear();
     bv.clear();
     fin>>n;
unsigned long oa=1000010,ea=1000010;
     total=0;
     for(i=0;i<n;i++)
     {
       fin>>x;
       if(x&1 && x<oa) oa=x;
       else if(!(x&1) && x<ea) ea=x;
       v.push_back(x);
       bv.push_back(bitset<sz>(x));
       for(j=0;j<sz;j++) sum[sz-1-j]+=bv[i][j];
       total+=x;
       
     }
     int w=0;
     for(i=0;i<sz;i++) if(sum[i]&1)  { fout<<"Case #"<<test<<": "<<"NO"<<endl; w=1; break;}
     
     if(w==0) {
     
     fout<<"Case #"<<test<<": "<<(total-min(ea,oa))<<endl;
     }            
    
    }
    
 fin.close();
 fout.close();
 return 0;   
}
