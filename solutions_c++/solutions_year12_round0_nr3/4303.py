#include<iostream>
#include<algorithm>
#include <cstdio>
#include<string>
#include <sstream>
using namespace std;
 
string shift(string s)
{
       int l=s.length();
       char lst=s[l-1];
       for(int i=l-1;i>0;i--)
       {
               s[i]=s[i-1];
       }
       s[0]=lst;
       return s;
}
template<class T> inline string toString(const T &a) { ostringstream sout; sout<<a; sout.flush(); return sout.str(); }

int main()
{
    int t,a,b,i,j,k,l,l2;
    
    int c;
    string s1,s2,s3,s4;
   freopen ("3.out","w",stdout);
	freopen ("3.in","r",stdin);
	cin>>t;
   for(k=1;k<=t;k++)
    {
        s1=s2=s3=s4="";
        cin>>a>>b;
        c=0;
        for(i=a;i<b;i++)
        {
                        s1=toString(i);
                        //cout<<"I "<<s1<<endl;
                         for(j=i+1;j<=b;j++)
                         {
                         
                         s2=toString(j);
                         //cout<<"J "<<s2<<" ";
                        l2=s2.length();
                         while(l2>0)
                         {
                                      s1=shift(s1);
                                      //cout<<s3<<" ";
                                      if(s1==s2)
                                      {
                                                c++;
                                                break;
                                      }
                                      l2--;
                         }
                        // cout<<endl;
                         }
       }
       cout<<"Case #"<<k<<": "<<c<<endl; 
    }
}                 
