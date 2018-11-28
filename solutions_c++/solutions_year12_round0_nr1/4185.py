#include<iostream>
#include<cstdio>
#include<fstream>
using namespace std;
int main()
{
 int t;
 string s;
 fstream f,g;
 f.open("A-small-attempt2.in",ios::in);
 g.open("output.out",ios::out);
 char a[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
 char c;
 f>>t;
 getline(f,s);
 int j=1;
 while(t--)
 {
   getline(f,s);
   for(int i=0;i<s.length();i++)
   if(s[i]!=' ')
   s[i]=a[s[i]-'a'];
   //cout<<"Case #"<<j<<":"<<s<<endl;          
   g<<"Case #"<<j<<": "<<s<<endl;          
   j++;
 }
 
 f.close();
 g.close();
 return 0;    
}
