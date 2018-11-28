#include <vector>
#include <string>
#include <stdlib.h>
#include <math.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <sstream>
#include <map>
#include <ctime>
#include <cassert>

using namespace std;

ofstream fout("../../output.txt");
ifstream fin("../../input.txt");


int sol(int x, int min, int max)
{
	int base = 10;
	int ans = 0;
	vector<int> vals;
	while(base < x)
	{
		int a = x/base;
		int b = x%base;
		if(b*10 >= base)
		{
			//so b is ok
			int otherbase = 10;
			while(otherbase <=a)
				otherbase*=10;
			int newval = b*otherbase + a;
			
			//cout << x <<  "  " << a << " " << b << " " << newval << endl;
			
			if(newval>=min && newval <= max && newval > x)
			{
				int i=0;
				for(i=0; i<vals.size(); i++)
				{
					if(vals[i]==newval)
						break;
				}
				if(i==vals.size())
				{
					vals.push_back(newval);
					//   cout << x << " " << newval << endl;
				
					   ans++;
				}
			}
		}
		base*=10;
	}
	return ans;
}

int main(void)
{
	int ttt;
	fin >> ttt;
	int ct = 0;
	string s;
	
	
	
	while(ttt>0)
	{
		ct++;
		ttt--;
		int n,i,j,k,s,p;
		
		int m;
		
				
		int ans =0;
		
		int a,b;
		
		fin >> a >> b;
		
		for(int i=a; i<=b; i++)
			ans+=sol(i,a,b);
		
		
		
		cout << "Case #" << ct << ":" << " " << ans << endl;
		fout << "Case #" << ct << ":" << " " << ans << endl;
		
	}
	
	
	return 0;
}

