#include <cstdio>
#include <algorithm>
#include <map>
#include <iostream>
#include <string>
#include <set>
#include <vector>
#include <fstream>
#include<cmath>

using namespace std;

int main()
{
	int T;
	cin >> T;
	ofstream cout("A.out");
	for(int i = 0; i < T; i++)
	{
		int n, k;
		cin >> n >>k;
		int min = (int)pow(2, (double)n);
		if((k+1)%min == 0)
			 cout << "Case #"<<i+1<<": ON"<<'\n';
		else 
			cout << "Case #"<<i+1<<": OFF"<<'\n';
		/*if(k == 0) 
		{
			cout << "Case #"<<i+1<<": OFF"<<'\n';
			continue;
		}
		int sum = 0;
		int mul = 1;
		for(int j = 0; j < n; j++)
		{
			sum += mul;
			mul = mul * 2;
		}
		if(k < sum) 
		{
			cout << "Case #"<<i+1<<": OFF"<<'\n';
			continue;
		}
		if(k == sum) 
		{
			cout << "Case #"<<i+1<<": ON"<<'\n';
			continue;
		}
		else
		{
			mul = mul/2;
			int judge = ((k-1)/(sum-1));
			if(judge%2 == 1 )
				cout << "Case #"<<i+1<<": ON"<<'\n';
			else 
				cout << "Case #"<<i+1<<": OFF"<<'\n';
		}*/
	}
	return 0;
}
				
		
		
