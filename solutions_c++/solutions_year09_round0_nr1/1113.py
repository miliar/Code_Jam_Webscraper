//Alien
//CodeJam
#include<iostream>
#include<set>
#include<string>
using namespace std;
set<string>words;int count=0;
void ret(string pre,string suff)
{
 if(pre!="" && words.find(pre)==words.end())
 return;
 else 
 if(suff=="")
 {
  if(words.find(pre)!=words.end())
   count++;   
 }
 else 
 {
   bool paran=false;string check="";
   int i=0;
   for(i=0;i<suff.size();i++)
   {
     if(suff[i]=='(')
     { 
      paran=true; 
     }
     else if(islower(suff[i]))
     {
       if(paran==false)
       pre+=suff[i];
       else
       check+=suff[i];
     } 
     else if(suff[i]==')')
     {paran=false;break;} 
   }
   if(i==suff.size())
   ret(pre,"");
  else 
   for(int j=0;j<check.size();j++)
   ret(pre+check[j],suff.substr(i+1,suff.size()));
 } 
}
int main()
{
 int l,d,n;
 while(cin>>l>>d>>n)
 {

   words.clear();
   string s="";
   for(int i=0;i<d;i++)
   {
     cin>>s; 
    string temp="";
     for(int i=0;i<s.size();i++)
    { 
      temp+=s[i];
      words.insert(temp);
    }
  }
   
   for(int i=1;i<=n;i++)
   {
     cin>>s; 
     count=0;
     ret("",s);
     cout<<"Case #"<<i<<": "<<count<<endl;
   }  
 
 }
 return 0;
}
