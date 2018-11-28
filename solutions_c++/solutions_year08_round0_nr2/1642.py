#include <iostream>
#include <string>
#include <sstream>
#include<queue>
#include <string>
using namespace std;

struct przyb {
int czas;
int co;
};

class compa{
public:
bool operator()(przyb a, przyb b){ if (a.czas>b.czas) return true; else return false;}
};

int odczyt(string s)
{
string pom;
int i,o;
pom=pom+s[0]+s[1];
istringstream is(pom);
is>>i;
o=i*60;
pom="";
pom=pom+s[3]+s[4];
istringstream is2(pom);
is2>>i;
o+=i;
return o;
}

int main()
{
priority_queue<przyb,vector<przyb>,compa> ka, kb;
przyb pom;
string s;
int n,na,nb,t,p,czas,max;
cin>>n;
for(int i=0;i<n;i++)
  {
  cin>>t;
  cin>>na;
  cin>>nb;
  for(int j=0;j<na;j++)
     {
     cin>>s;
     pom.czas=odczyt(s);
     pom.co=-1;
     ka.push(pom);
//     cout<<pom.czas<<endl;
     cin>>s;
     pom.czas=odczyt(s)+t;
     pom.co=1;
     kb.push(pom);
//     cout<<pom.czas<<endl;
     }
  for(int j=0;j<nb;j++)
     {
     cin>>s;
     pom.czas=odczyt(s);
     pom.co=-1;
     kb.push(pom);
//     cout<<pom.czas<<endl;
     cin>>s;
     pom.czas=odczyt(s)+t;
     pom.co=1;
     ka.push(pom);
//     cout<<pom.czas<<endl;
     }
  cout<<"Case #"<<i+1<<": ";
  p=0;
  max=0;
  pom.czas=0;
  while((pom.czas<1440)&&(not ka.empty()))
    {
    pom=ka.top();
    ka.pop();
    p+=pom.co;
    if ((ka.empty())||(pom.czas!=ka.top().czas))
      {
      if (max+p<0) max=-p;
      }
    }
 // if (max+p<0) max=-p;
  while(not ka.empty()) ka.pop();
  cout<<max<<" ";
  p=0;
  max=0;
  pom.czas=0;
  while((pom.czas<1440)&&(not kb.empty()))
    {
    pom=kb.top();
    kb.pop();
    p+=pom.co;
    if ((kb.empty())||(pom.czas!=kb.top().czas))
      {
      if (max+p<0) max=-p;
      }
    }
  //if (max+p<0) max=-p;
  while(not kb.empty()) kb.pop();
  cout<<max<<endl;
  }
}
