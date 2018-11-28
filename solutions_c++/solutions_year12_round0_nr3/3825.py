// GoogleCJ.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>
#include <conio.h>
#include <fstream>
#include <math.h>
using namespace std;

long len(long int n)
{
	long length = 0;
	while(n>0)
	{
		n=n/10;
		length++;
	}
	return length;
}
long oneRec(long int n,long len)
{
	int temp = n%10; 
	n/=10;
	return (temp*(pow((double)10,(len-1)))+n);
}
long Compute(long n,long B)
{
	long l = len(n);
	long copyn = n;
	long count = 0;
	long* arr = new long(l+1);
	long c = 0;
	for(long i=1;i<l;i++)
	{
		n = oneRec(n,l);
		if(n>copyn && n<=B)
		{
			arr[c]=n;
			c++;
			//count++;
			//cout<<copyn<<" "<<n<<"\n";
		}
	}
	//send no of distinct in arr
	for(long i=0;i<c-1;i++)
	{
		for(long j=i+1;j<c;j++)
		{
			if(arr[i]>arr[j]) 
			{
				long temp = arr[i];
				arr[i] = arr[j];
				arr[j] = temp;
			}
		}
	}
	if(c>0){
		count++;
		for(long i=1;i<c;i++)
		{
			if(arr[i]!=arr[i-1]) count++;
		}
	}
	return count;
}
int _tmain(int argc, _TCHAR* argv[])
{
	long t;
	long A,B;
	
	//long len;
	ifstream myinput ("C-large.in");
	ofstream myoutput("output.txt");
	myinput >> t;
	//cin>>t;
	//string str;
	//getline(myinput,str);
	for(long i=0;i<t;i++)
	{
		long count=0;
		myinput>>A;
		myinput>>B;
		for(long j=A;j<=B;j++)
		{
			count+=Compute(j,B);

		}
		myoutput<<"Case #"<<(i+1)<<": "<<count<<"\n";
	}
	//myoutput<<"Case #"<<(i+1)<<": "<<str<<"\n";
	myinput.close();
	myoutput.close();
	//getch();
	//getch();
	return 0;
}

