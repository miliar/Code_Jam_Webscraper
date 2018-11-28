#include <fstream>
//#include <iostream>
#include <string>
#include <cmath>
#include <stack>
#include <vector>
#include <algorithm>
using namespace std;
bool check(int n,int k)
{
	int temp=(1<<n);
	if(k==0)
		return false;
	if(n==1)
	{
		if(k%2==0)
			return false;
		else return true;
	}
	else 
	{
		if(k%temp+1==temp)
			return true;
		else return false;
	}
}

int main()
{
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int t,n,k;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		cin>>n>>k;
		if(check(n,k))
			cout<<"Case #"<<i+1<<": ON"<<endl;
		else cout<<"Case #"<<i+1<<": OFF"<<endl;
	}
	return 0;
}