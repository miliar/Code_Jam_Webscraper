#include<iostream>
#include<vector>
#define MAX 5005
using namespace std;

int l,d,n,i,j,k,cou,wsk;
string s;
vector<string> tab;
bool can[MAX],useful[MAX],q;

int main()
{
cin >> l >> d >> n;

for(i=0; i<d; ++i)
     {
     cin >> s;
     tab.push_back(s);
     }
     
for(i=1; i<=n; ++i)
     {
     cin >> s;
     for(j=0; j<d; ++j) useful[j]=true;
     cou=wsk=0;
     q=false;
     
     for(j=0; j<s.length(); ++j)
          {
          if(s[j]=='(') q=true;
          
          if(s[j]!='(' && s[j]!=')')
               {
               for(k=0; k<d; ++k)
                    if(tab[k][wsk]==s[j]) can[k]=true;
               if(!q)
                    {
                    for(k=0; k<d; ++k)
                         {
                         if(!can[k]) useful[k]=false;
                         can[k]=false;
                         }
                    ++wsk;
                    }
               }
                    
          if(s[j]==')')
               {
               for(k=0; k<d; ++k)
                    {
                    if(!can[k]) useful[k]=false;
                    can[k]=false;
                    }
               ++wsk;
               q=false;
               }
          }
               
     for(j=0; j<d; ++j)
          if(useful[j]) ++cou;
          
     printf("Case #%d: %d\n",i,cou);
     }
     
return 0;
}
