#include<iostream>
#include<vector>
using namespace std;

int t,n,i,j,k,last,res;
string s;
vector<int> pom;

int main()
{
cin >> t;

for(i=1; i<=t; ++i)
     {
     cin >> n;
     pom.clear();
     res=0;
     for(j=0; j<n; ++j)
          {
          last=-1;
          cin >> s;
          for(k=0; k<s.length(); ++k)
               if(s[k]=='1') last=k;
          pom.push_back(last);
          }

     for(j=0; j<n-1; ++j)
          if(pom[j]>j)
               {
               int wsk=j+1;
               while(pom[wsk]>j) ++wsk;
               int c=pom[wsk];
               res+=(wsk-j);
               for(k=wsk; k>j; --k) pom[k]=pom[k-1];
               pom[j]=c;
               }
     
     cout << "Case #" << i << ": " << res << endl;
     }
     
return 0;
}
