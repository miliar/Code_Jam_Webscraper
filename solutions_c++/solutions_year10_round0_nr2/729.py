#include <cstdio>
#include <algorithm>
#include <map>
#include <iostream>
#include <string>
#include <set>
#include <vector>
#include <fstream>
#include<cmath>
#include  <math.h>


using namespace std;

int main()
{
	ofstream cout("B.out");
	int c;
	cin >> c;
	for(int i = 0; i < c; i++)
	{
		int n;
		cin >> n;
		//cout <<"n = "<< n << '\n';
		long long int a1, a2, a3;
		if(n == 2) cin >> a1 >> a2;
		if(n == 3) cin >> a1 >> a2 >> a3;
		if(a1 == a2 && a2 == a3)
		{
			cout<<"Case #"<<i+1<<": "<<0<<'\n';
			continue;
		}
		if(a1 == a3 || a2 == a3)
			n = 2;
		if(a1 == a2) 
		{
			a2 = a3;
			n = 2;
		}
		if(n == 2)
		{
			//cin >> a1 >> a2;
			//cout << t1 << " *** " << t2<< '\n';
			long long int diff;
			if(a1 > a2)
				diff = a1-a2;
			else diff = a2-a1;
			if(a1%diff == 0)
			{
				cout<<"Case #"<<i+1<<": "<<0<<'\n';
				continue;
			}
			else 
			{
				long long int b1 = a1/diff;
				//cout << a1<<" " <<diff <<'\n';
				cout<<"Case #"<<i+1<<": "<<((b1+1)*diff-a1)<<'\n';
				continue;
			}
		}
		else 
		{
			//cin >> a1 >> a2 >> a3;
			long long int d1 = abs(a1-a2);
			long long int d2 = abs(a2-a3);
			long long int d3 = abs(a3-a1);
			long long int temp;
			if(d1 < d2)
			{	
				temp = d1;
				d1 = d2; 
				d2 = temp;
			}
			while(d1%d2 != 0)
			{
				d1 = d1%d2;
				if(d1 < d2)
				{	
					temp = d1;
					d1 = d2; 
					d2 = temp;
				}
			}
			if(d2 < d3)
			{	
				temp = d2;
				d2 = d3; 
				d3 = temp;
			}
			while(d2%d3 != 0)
			{
				d2 = d2%d3;
				if(d2 < d3)
				{	
					temp = d2;
					d2 = d3; 
					d3 = temp;
				}
			}
			if(a1%d3 == 0)
			{	
				cout<<"Case #"<<i+1<<": "<<0<<'\n';
				continue;
			}
			else
			{
				cout<<"Case #"<<i+1<<": "<<((a1/d3+1)*d3-a1)<<'\n';
				continue;
			}
		}
	}
	return 0;
}
	
			
			
			
