#include <iostream>
#include <string>
#include <map>
#include <utility>
#include <sstream>
using namespace std;
long long int to_base(string a,int b)
{
     long long int sol=0;
     int k=1;
     while(a.size()>0)
     {
                      
     int t;
     if(a[a.size()-1]>='0'&&a[a.size()-1]<='9')t=a[a.size()-1]-'0';
     else t=a[a.size()-1]-'a'+11;
     sol+=t*k;
     k*=b;
     a=a.substr(0,a.size()-1);
     }
     return sol;
}

bool solve(int x)
{
     string s;
     cin>>s;
     map <char,char> m;
     char k='1';
     for(int i=0;i<s.size();i++)
      if(m.find(s[i])==m.end())
      {m.insert( make_pair (s[i],k) );
      if(k=='0')k+=2;
      else
      if(k=='1')k='0';
      else 
      if(k=='9')k='a';
      else k++;}
     stringstream ss;
     for(int i=0;i<s.size();i++)
      ss<<m[s[i]];
     string a;
     ss>>a;
     //cout<<a<<endl;
    // cout<<s<<endl;
    // cout<<"ASD"<<endl;
     //cout<<a<<endl;
     int f=m.size();
     if(f==1)f++;
     cout<<"Case #"<<x<<": "<<to_base(a,f)<<endl;
}
int main()
{
    int T;
    cin>>T;
    for(int i=0;i<T;i++)
     solve(i+1);
    return 0;
}
