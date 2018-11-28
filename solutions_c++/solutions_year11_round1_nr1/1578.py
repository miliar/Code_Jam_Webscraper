#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>

using namespace std;

int T,N,PD,PG;

bool check(int n,int x,int y)
{
	int t;
	int k;
	
	if(x != 100 && y ==100)
		return false;
	if(x != 0 && y == 0)
		return false;
	
	for(int i = 0;i <= n;i++)
		{
		//today play i,and win k/100
		
		if(i == 0 && x != 0)
			continue;
		
			k = i * x;
			if(k%100 == 0)
				{	
/*				
					for(int j = i;;j++)
						{	
							t = j * y;
							if(t%100 == 0)
								if(t - k <= (j - i)*100 && t - k >= 0)
									return true;
						}
*/
				return true;
				}
			else continue;
		}
	return false;
}

int main()
{
	ifstream fin("in.txt");
	ofstream fout("out.txt");
	fin>>T;
	int i= 1;
	bool flag;
	
	for(i = 1;i <= T; i++)
	{
		fin>>N;
		fin>>PD;
		fin>>PG;
		
		flag = check(N,PD,PG);
		
		if(flag)
			fout<<"Case #"<<i<<": Possible"<<endl;
		else
			fout<<"Case #"<<i<<": Broken"<<endl;
	}
	return 0;
}











