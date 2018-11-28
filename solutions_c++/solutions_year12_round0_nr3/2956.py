/*
 * c.cpp
 *
 *  Created on: Apr 14, 2012
 *      Author: Sara Tarek
 */

#include <algorithm>
#include <cmath>
#include <complex>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <memory.h>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <stdio.h>
#include <utility>
#include <vector>

using namespace std;

int main()
{
	int a,b, t;

	freopen( "input.in", "r", stdin );
	freopen( "output.txt", "w", stdout );

	cin>>t;
	int Case = 1;

	while(t > 0)
	{
		cin>>a>>b;
		int *mem = new int[b+1];
		memset(mem, 0, sizeof(mem));

		int count = 0;
		for(int i = a; i <= b; i++)
		{
			stringstream s1;
			s1 << i;
			string num;
			s1 >> num;
			//cout<<num<<endl;
			for(int j = num.length() - 1; j > 0; j--)
			{
				string dummy = num.substr(j, num.length() - j);
				dummy = dummy + num.substr(0, j);
				//cout<<"dummy: "<<dummy<<endl;
				stringstream s2;
				s2 << dummy;
				int res;
				s2 >> res;
				//cout<<"res: "<<res<<endl;
				if(res >= a && res <= b && mem[res] != 1 && res != i)
				{
					//cout<<"num : "<<num<<" VS" << "res: "<<res<<endl;
					count++;
				}
			}
			mem[i] = 1;
		}
		cout<<"Case #"<<Case<<": "<<count<<endl;
		Case++;
		t--;
	}
	return 0;
}	
	













