// permutation.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <cmath>
using namespace std;

long long pow2(long long b)
{
	long long rez = 1;
	for (int i=0; i<b; i++)
		rez*=2;
	return rez;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	long long n,k,t;
	cin>>t;
	for (int i=0; i<t; i++)
	{
		cin>>n>>k;
		cout<<"Case #"<<i+1<<": ";
		if (k % pow2(n) == pow2(n)-1)
			cout<<"ON";
		else
			cout<<"OFF";
		cout<<endl;
	}

	
	
	
	return 0;
}

