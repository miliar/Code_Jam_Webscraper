#include <iostream>
#include <string>
#include <stdio.h>

using namespace std;
string s,control="welcome to code jam";
int rec(int i,int j)
{
int o=0;
for(;i<s.length();i++)
{
	if(control[j]==s[i])
	{
	if(j==18)
	{
	o++;
	
	}
	else
	o+=rec(i+1,j+1);
	
	}
	
	
	
	
	
	}
	
	if(o>10000)
	o=o%10000;
return o;

}

int main(int argc,char *argv[])
{
int n;
cin>>n;
char k;
scanf("%c",&k);
for(int i=0;i<n;i++)
{
int occur=0;

char c;
s="";
//c='\n';
//printf("%d",c);
scanf("%c",&c);
//printf("%d",c);
while(c!=10)
{
s+=c;
scanf("%c",&c);
//printf("%d",c);
}


occur=rec(0,0);


cout<<"Case #"<<i+1<<": ";
if(occur<1000)
cout<<"0";
if(occur<100)
cout<<"0";
if(occur<10)
cout<<"0";
cout<<occur<<endl;

}




return 0;}