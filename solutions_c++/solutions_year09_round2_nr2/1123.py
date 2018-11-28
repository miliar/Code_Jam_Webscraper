// A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include<algorithm>
#include<map>
#include<set>
#include<iostream>
#include<fstream>
#include<string>
#include<sstream>
using namespace std;
bool maximum(string );
int zerobreak(string );
void display(string );
void reverse(string );

int _tmain(int argc, _TCHAR* argv[])
{
	return 0;
}

bool maximum(string number)
{
for(int j=number.length()-1;j>0;j--)
if(int(number[j])>int(number[j-1]))
return false;

return true;
}
int zerobreak(string number)
{
	int h;
for(h=number.length()-1;h>=0;h--)
if(number[h]!='0')
return h;

return h;

}
void reverse(string number)
{
	int x=zerobreak(number);

if(x==0)
cout<<number<<'0'<<endl;
else if(x==number.length()-1)
{
	cout<<number[x]<<'0';
	for(int i=number.length()-2;i>=0;i--)
		cout<<number[i];
    cout<<endl;
}
else
{
	cout<<number[x];
	for(int m=0;m<=number.length()-1-x;m++)
		cout<<'0';
    for(int i=x-1;i>=0;i--)
		cout<<number[i];
    cout<<endl;

}
}
void display(string number)
{
int numbers[10];
int p;
memset(numbers,0,sizeof(numbers));
for(p=number.length()-1;p>0;p--)
{
if(int(number[p])>int(number[p-1]))
{
	 numbers[int(number[p])-48]++;
	break;

}
else
   numbers[int(number[p])-48]++;
 
}

if(p>1)
for(int i=0;i<p-1;i++)
cout<<number[i];
bool flag=true;
int f=-1;
while(flag)
{
	f++;
	if(numbers[f]>0)
	if(f>int(number[p-1])-48)
	{
      cout<<char(f+48);
	  numbers[f]--;
	  numbers[int(number[p-1])-48]++;
	  flag=false;
	}

}
for(int d=0;d<=9;d++)
	for(int c=1;c<=numbers[d];c++)
		cout<<d;
cout<<endl;

}



void main()
{

	ifstream cin("1.txt");
   
string number;
int cases;
cin>>cases;
for(int f=0;f<250;f++)
cin>>number;
for(int i=250;i<500;i++)
{

	cout<<"Case #"<<i+1<<": ";
cin>>number;
if(maximum(number))
	reverse(number);
else
{
	
	display(number);




}



}





}