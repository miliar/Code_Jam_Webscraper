#include<iostream>
#include<fstream>
#include<vector>
#include<math.h>
using namespace std;

int patadd(int a, int b)
{
    vector<int> x;
    while(a != 0)
    {
      x.push_back(a%2);
      a = a/2;
    }
    vector<int> y;
    while(b != 0)
    {
      y.push_back(b%2);
      b = b/2;
    }
    vector<int> z;
    int i;
    for(i=0; i<x.size() && i<y.size(); ++i)
    {
       z.push_back((x[i]+y[i])%2);     
    }
    while(i<x.size())
    {
        z.push_back(x[i]);             
        ++i;
    }
    while(i<y.size())
    {
        z.push_back(y[i]);             
        ++i;
    }
    int result=0;
    for(i=0; i< z.size(); ++i)
    {
        result+= z[i]*pow(2,i);
    }
    return result;
}

int sval(vector<int> v)
{
   int result = 0;
   for(int i =0; i< v.size(); ++i)
   {
           result += v[i];
   }
   return result;
}

int pval(vector<int> v)
{
   int result = 0;
   for(int i =0; i< v.size(); ++i)
   {
          result =  patadd(result,v[i]);
   }
   return result;
}

vector<int> pat;
vector<int> sean;
int Max;

void rec(int i)
{
    /* if(Max>0)
      return;*/
     pat.push_back(sean[i]);
     sean.erase(sean.begin()+i);
     /*cout<<pval(pat)<<" "<<pval(sean)<<endl;
     for(int z= 0; z<pat.size(); ++z)
         {
             cout<<pat[z]<<" ";    
         }
         cout<<endl;*/
     if( pval(pat) == pval(sean))
     {
        if(Max< sval(sean))
          Max = sval(sean); 
       // return;
     }
     
     for(int j=i; j<sean.size(); ++j)
     {
        rec(j);     
     }
     
     sean.insert(sean.begin()+i, pat.back());
     pat.pop_back();
}

int main()
{
  ifstream in("C-small-attempt1.in");
  ofstream out("out.txt");
  int T;
  in>>T;
  for(int cas = 1; cas<=T; cas++)
  {
     Max = 0;
     pat.clear();
     sean.clear();
     int n;
     in>>n;
     for(int i=0; i<n; ++i)
     {
        int t;
        in>>t;
        sean.push_back(t);     
     }
     for(int i =0; i<n; i++)
      rec(i);
      
     out<<"Case #"<<cas<<": ";
      if(Max == 0)
        out<<"NO"<<endl;
      else
       out<<Max<<endl;
  }
 // system("pause");
}
