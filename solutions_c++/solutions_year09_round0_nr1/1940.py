#include <iostream>
#include <string>
#include <vector>
using namespace std;
int main()
{freopen("in.txt","r",stdin);
freopen("out.txt","w",stdout);
int L,D,N;
string s;
cin>>L>>D>>N;   
vector<string> List(D);
for(int i=0;i<D;i++)
{cin>>s;
 List[i]=s;}
for(int i=1;i<=N;i++)
{cin>>s;//lo un patron:
  int lon=s.size();      
  int cont=0;
 for(int f=0;f<D;f++)
 {int ok=1,okx=0; 
  int est=0,it=0;
  for(int j=0;j<lon;j++)
    {if(s[j]=='('){okx=0;est=1;continue;}
     if(s[j]==')'){if(okx==0){ok=0;break;}it++;est=0;continue;}
     if(est==0)
       { if(s[j]!=List[f][it])
         {ok=0;break;}
         else
          it++;
       }
     else
       { if(s[j]==List[f][it])
          okx=1;    
       }         
    }
  if(ok==1)cont++;  
 }    
 cout<<"Case #"<<i<<": "<<cont<<endl;
}
return 0;    
}
