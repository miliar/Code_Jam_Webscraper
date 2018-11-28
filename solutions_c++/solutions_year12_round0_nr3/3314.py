#include <sstream>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <fstream>
using namespace std;
int pairs(int n ,int b)
{
	string num;
	map <int,bool> pr;
	bool nzero,same;
	int digit,c,count = 0;
	c =n;
	nzero =  true;
	same = true;
	while(n)
	{
		digit = (n%10);
		nzero = digit && nzero;
		num.push_back(digit+48);
		n = n/10;
		if(n!=0)
			same = same && (digit==n%10);
	};
	n = c;
	if(!same)
	{
		reverse(num.begin(),num.end());
		if(nzero)
		{
			for(int i = 0;i<num.size()-1;i++)
			{
					char k = num[0];
					num.erase(num.begin());
					num.push_back(k);
					c = atoi(num.c_str());
					if(c>n&&c<=b)
						pr[c] = true;
			}	
		}
		else
		{
			for(int i = 0;i<num.size()-1;i++)
			{
				char k = num[0];
				num.erase(num.begin());
				num.push_back(k);
				c = atoi(num.c_str());
				if(c>n&&c<=b)
					pr[c] = true;
			}
		}
	}
	return pr.size();
}
int main()
{
	int a,b,t,sum;
	ifstream fin("input.in");
	ofstream fout("output.out");
	fin>>t;
	for( int i =0;i<t;i++)
	{
		fin>>a>>b;
		sum =0 ;
		for(int j =a;j<b;j++)
		{
			sum =sum+pairs(j,b);
		}
		fout<<"Case #"<<i+1<<": "<<sum<<endl;		
	}
}
	//fout<<j<<" "<<pairs(j,b)<<endl;