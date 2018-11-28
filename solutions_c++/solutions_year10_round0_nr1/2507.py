#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;

int main()
{
	ifstream fin;
	fin.open("input.txt");
	
	int N;
	fin>>N;
	
	for(int z=0;z<N;z++)
	{
		int n;
		long long k;
		fin>>n>>k;
		
		long long power = pow(2.0,n);
		if(k%power == power-1)
		{
			cout<<"Case #"<<z+1<<": ON";
		}
		else
		{
			cout<<"Case #"<<z+1<<": OFF";
		}
		cout<<endl;
	}
	return 0;
}
