#include <iostream>
#include <map>
using namespace std;

map <char,char> transl;
	
void mapit(string onew,string oner)
{
 int i; 
 for(i=0;i<onew.size();i++)
  if(transl.count(onew[i])==0)
   transl[onew[i]] = oner[i];
    return;
}

int main()
{
  mapit("ejp mysljylc kd kxveddknmc re jsicpdrysi","our language is impossible to understand");
  mapit("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd","there are twenty six factorial possibilities");
  mapit("de kr kd eoya kw aej tysr re ujdr lkgc jv","so it is okay if you want to just give up");
  transl['q'] = 'z';
  transl['z'] = 'q';      
  int tc,i,j;cin>>tc;
  for(i=0;i<tc;i++)
   {
    string st;
    if(i==0)getline(cin,st);
    getline(cin,st);
    cout<<"Case #"<<i+1<<": "; 
    for(j=0;j<st.size();j++)
    cout<<transl[st[j]];	
    cout<<"\n";
   }

}
      

 
  

