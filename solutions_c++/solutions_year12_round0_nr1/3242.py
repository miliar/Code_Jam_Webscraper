#include<iostream>
#include<ctype.h>
using namespace std;
 
int main()
{
int i,j,k,cases,len=0;
char a[]={"abcdefghijklmnopqrstuvwxyz"};
char b[]={"ynficwlbkuomxsevzpdrjgthaq"};
string str;
cin>>cases;
for(k=0;k<=cases;k++)
{
getline(cin, str, '\n');
len=str.length();
 
for(i=0;i<len;i++)
{
if(!isalpha(str[i]))
cout<<str[i];
else
{
for(j=0;j<26;j++)
{
if(str[i]==b[j])
cout<<a[j];
}
}
}
cout<<"\n";
}
return 0;
}