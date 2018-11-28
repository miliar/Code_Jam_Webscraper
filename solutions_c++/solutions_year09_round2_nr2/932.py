#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int t,i,j,ile;
vector<int> tab,pom;
string n;

int main()
{
cin >> t;

for(i=1; i<=t; ++i)
     {
     cin >> n;
     bool can=true;
     tab.clear();
     pom.clear();
     ile=0;
   //  cout << n << endl;
   // continue;
     cout << "Case #" << i << ": ";
     
     for(j=0; j<n.length(); ++j)
          {
          tab.push_back(n[j]-'0');
          pom.push_back(n[j]-'0');
          }
     
     next_permutation(tab.begin(),tab.end());
     sort(pom.begin(),pom.end());
  
     if(pom[0]==0)
          {
          for(j=0; j<pom.size(); ++j)
               if(pom[j]>0)
                    {
                    pom[0]=pom[j];
                    pom[j]=0;
                    break;
                    }
          }
     
     for(j=0; j<tab.size(); ++j)
          if(tab[j]==pom[j]) ++ile;
          
     if(tab[0]==0)
               {
               cout << pom[0] << "0";
               for(j=1; j<pom.size(); ++j) cout << pom[j];
               can=false;
               }
     
     if(!can) {cout << endl; continue;}
     
     if(ile!=tab.size())
          {
          for(j=0; j<tab.size(); ++j) cout << tab[j];
          }
     else
               {
               cout << pom[0] << "0";
               for(j=1; j<pom.size(); ++j) cout << pom[j];
               }
               
     cout << endl;
     }
     
return 0;
}
