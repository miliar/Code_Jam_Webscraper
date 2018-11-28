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

int dolis[10000];

int vals[100000];


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
		int n,i,j,k;
		
		int ans = 0;
		fin >> n;
		vector<int> nums;
		
		memset(vals,0,sizeof(vals));
		
		for(i=0; i<n; i++)
		{
			fin >> j;
			vals[j]++;
		}
		
		
		ans = 1000000;
		
		int readfrom=0;
		int writeto = 0;
		
		for(i=0; i<=10001; i++)
		{
			if(vals[i]==vals[i-1])
				continue;
			
			if(vals[i] > vals[i-1])
			{
				for(j=0; j<vals[i]-vals[i-1]; j++)
				{
					dolis[writeto]=i;
					writeto++;
				}
			}
			else {
				for(j=0; j<vals[i-1]-vals[i];j++)
				{
					k = i - dolis[readfrom];
					if(k<ans)
						ans=k;
					readfrom++;
				}
			}
		}
		
		

		if(ans==1000000)
			ans=0;
		
		
		cout << "Case #" << ct << ":" << " " << ans << endl;
		fout << "Case #" << ct << ":" << " " << ans << endl;
		
		
		
	}
	
	
	return 0;
}

