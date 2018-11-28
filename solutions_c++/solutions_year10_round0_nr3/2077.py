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
	ofstream cout("C.out");
	int t;
	cin >> t;
	for(int i = 0; i < t; i++)
	{
		int r, k, n;
		cin >> r >> k >> n;
		int a[n];
		int sum = 0;
		for(int j = 0; j < n; j++)
		{
			cin >> a[j];
			sum += a[j];
		}
		if(sum <= k)
		{
			cout << "Case #"<<i+1<<": "<<sum*r<<'\n';
			continue;
		}
		int idx = 0;
		int result = 0;
		for(int ii = 0; ii < r; ii++)
		{
			int total = 0; 
			while(1)
			{
				if((total+a[idx])> k)
					break;
				total += a[idx];
				if(idx + 1 >= n)
					idx = 0;
				else idx += 1;
				
			}
			result += total;
		}
		cout << "Case #"<<i+1<<": "<<result<<'\n';
	}
	return 0;
}		
