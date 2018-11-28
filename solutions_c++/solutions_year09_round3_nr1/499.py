#include<iostream>
#include<map>
using namespace std;

typedef long long ll;

int t,i,j,cou,base;
ll mul,res;
map<char,int> mapa;
map<char,bool> odw;
string N;

int main()
{
cin >> t;

for(i=1; i<=t; ++i)
     {
     mapa.clear();
     odw.clear();
     cin >> N;
     mapa[N[0]]=1;
     odw[N[0]]=true;
     cou=0;
     
     for(j=1; j<N.length(); ++j)
          if(odw[N[j]]==0)
              {
              if(cou==1) ++cou;
              mapa[N[j]]=cou;
              odw[N[j]]=true;
              ++cou;
              }
   //  for(j=0; j<N.length(); ++j)
  //   cout << mapa[N[j]] << endl;     
  
     int base=0;
     for(j=0; j<N.length(); ++j) base=max(mapa[N[j]],base);  
     ++base; 
     
     res=0;
     mul=1;
     
     for(j=N.length()-1; j>=0; --j)
          {
          res+=mul*mapa[N[j]];
          mul*=(ll)base;
          }
     
     cout << "Case #" << i << ": " << res << endl;
     }

return 0;
}

          
                
