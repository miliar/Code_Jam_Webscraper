#include<iostream>
#include<string>
using namespace std;
int main()
{ string::iterator i;
string str,s,str1;
long long test,d;
cin>>test;
d=test;
while(d--)
{
cin>>str;
str1=str;

if(next_permutation(str1.begin(),str1.end()))
{
cout<<"Case #"<<test-d<<": "<<str1<<endl;
}
else
{
str="0"+str;
next_permutation(str.begin(),str.end());
cout<<"Case #"<<test-d<<": "<<str<<endl;

}
}
return 0;
}
