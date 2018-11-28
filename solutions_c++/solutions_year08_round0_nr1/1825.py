#include<iostream>
#include<string>
#include<vector>
#include <list>
using namespace std;

vector <string> SEngs;
list <string> Queries;
int Nse;
int Nq;

int Switch(){
    
    int spos=0;
    for(int i=0;i<Nse;i++)
     {
        int cpos=-1;
             list<string>::iterator it;
             int j=0;
         for (it=Queries.begin();it!=Queries.end();it++)
            {
             if (!SEngs[i].compare(*it)) {cpos=j;break;};
                    j++;};
         if(cpos==-1){Queries.clear();
                      return cpos;};
                      //cout<<cpos<<"\n";
              spos=(spos<cpos)? cpos:spos; 
              
              }//cout<<spos<<"\n";
     for(int i=0;i<spos;i++)
           { Queries.pop_front();}
       
       return spos;
       }
       
       
int main(){

char name[101];
string a;

int Ntc;
cin>>Ntc;
gets(name);

for(int tc=1;tc<=Ntc;tc++)
{
  SEngs.clear();
  Queries.clear();
  cin>>Nse;
  gets(name);
  //cout<<Nse<<"\n";
 for(int i =0;i<Nse;i++)
 {
  gets(name);a=name;SEngs.push_back(a);
 // cout<<a<<"\n";
  }
  cin>>Nq;
  gets(name);
 // cout<<Nq<<"\n";
 for(int i=0;i<Nq;i++)
  {
    gets(name);a=name;Queries.push_back(a);
  //cout<<a<<"\n";
  }
  printf("Case #%d: ",tc);
 int res=0;
  int s;
  s=Switch();
 // cout<<s<<"\n";
  while(s!=-1 )
      {res++;
       s=Switch();
       // cout<<s<<"\n";
       };
 cout<<res;
 cout<<"\n";
 }
} 

 
  
 
