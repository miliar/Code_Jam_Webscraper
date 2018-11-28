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

vector<long long> plis;

void makeplis()
{
	plis.push_back(2);
	plis.push_back(3);
	int i,j;
	for(i=5; i<1000000; i++)
	{
		for(j=2; j*j<=i; j++)
		{
			if(i%j==0)
			{
				break;
			}
		}
		if(i%j==0)
			continue;
		plis.push_back(i);
		if(i<100)
		{
			cout << i << endl;
		}
	}
	return;
}
	

int main(void)
{
	int ttt;
	fin >> ttt;
	int ct = 0;
	string s;
	makeplis();
	while(ttt>0)
	{
		ct++;
		ttt--;
		int i,j,k;
		long long n;
		
		int ans = 0;
		fin >> n;
		
		for(i=0; i<plis.size() && plis[i]*plis[i]<=n; i++)
		{
			long long val = plis[i];
			val*=plis[i];
			while(val<=n)
			{
				ans++;
				val*=plis[i];
			}
		}
		
		if(n>1)
			ans++;
		
		
		cout << "Case #" << ct << ":" << " " << ans << endl;
		fout << "Case #" << ct << ":" << " " << ans << endl;
		
		
		
	}
	
	
	return 0;
}

