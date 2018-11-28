#include <iostream>
#include <vector>
#include <fstream>
using namespace std;


vector<int> intToBin(int x)
{
	vector<int> a;
	while(x>0)
	{
		int t=x%2;
		a.push_back(t);
		x/=2;
	}
	return a;
}

bool isOn(int n,int k)
{
	vector<int> t=intToBin(k);
	if(n>t.size()) return false;
	for(int i=0;i<n;i++)
	{
		if(t[i]==0) return false;
	}
	return true;
}

int main()
{
	int T;
	ifstream file("A-large.in");
	ofstream out("output.txt");
	file>>T;
	for(int i=0;i<T;i++)
	{
		int n,k;
		file>>n>>k;
		if(isOn(n,k)) out<<"Case #"<<i+1<<": "<<"ON"<<endl;
		else out<<"Case #"<<i+1<<": "<<"OFF"<<endl;
	}
	return 1;
}