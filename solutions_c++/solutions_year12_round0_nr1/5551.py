#include<iostream>
//#include<conio.h>
#include<string>
#include<cstdio>
#include<fstream.h>
#include<sstream>
using namespace std;
int main()
{
 char a[100]={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
 char b[100]={'y','n','f','i','c','w','l','b','k','u','o','m','x','s','e','v','z','p','d','r','j','g','t','h','a','q'};
 string s,s1;
 char c,d;
 int i,j,n,t,k,l;
  ifstream myfile ("in.in");
   ofstream myfile1;
  myfile1.open ("out.txt");
  if (myfile.is_open())
  {
   i=1;
   getline(myfile,s1);
   stringstream ss(s1);
   			ss >> l;
    while ( myfile.good())
    {
      getline (myfile,s);
	   n=s.length();
  for(j=0;j<=n;j++)
  {
   if(s[j]!=' ')
   for(k=0;;k++)
   {
   	if(b[k]==s[j])
	{
		  s[j]=a[k];
		  break;
	}
   }
  }
  if(i<=l)
  myfile1<<"Case #"<<i++<<": "<<s<<"\n";
 }
 }
// getch();
}
