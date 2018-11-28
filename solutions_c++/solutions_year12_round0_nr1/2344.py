#include<iostream>
using namespace std;
int main()
{
char a[26];
a[0]='y';
a[1]='h';
a[2]='e';
a[3]='s';
a[4]='o';
a[5]='c';
a[6]='v';
a[7]='x';
a[8]='d';
a[9]='u';
a[10]='i';
a[11]='g';
a[12]='l';
a[13]='b';
a[14]='k';
a[15]='r';
a[16]='z';
a[17]='t';
a[18]='n';
a[19]='w';
a[20]='j';
a[21]='p';
a[22]='f';
a[23]='m';
a[24]='a';
a[25]='q';
int t,x;
string s;
cin>>t;
cin.get();
for(int i=0;i<t;i++)
{
getline(cin,s);
cout<<"Case #"<<i+1<<": ";
for(int i=0;i<s.length();i++)
{
if(s[i]==' ')
{cout<<" ";continue;}
//cout<<s[i]-'a'<<endl;
x=s[i]-'a';
//cout<<x<<endl;
cout<<a[x];
}
cout<<endl;
}
return 0;
}
