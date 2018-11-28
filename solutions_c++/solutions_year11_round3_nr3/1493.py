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

int T,N,L,H;
int f[1000];
int ans;

bool check( int x)
{  
	int j;
	for(j=1;j<= N;j++)
	{
	if(f[j]%x!=0 && x%f[j]!=0 )
		return false;
		else continue;
	}
	return true;
}

bool find()
{
	for(int i =L;i <= H;i++)
		{
			if(check(i))
				{
				ans = i;
				return true;
				}
			else
				continue;
		}
	return false;
}

int main()
{
	ifstream fin("in.txt");
	ofstream fout("out.txt");
	
	
	fin>>T;
	for(int i= 1;i<= T;i++)
	{
	fin>>N>>L>>H;
	
	for(int j= 1;j<=N;j++)
		fin>>f[j];
	f[0] = f[N];
	
	bool flag =false;
	
	flag = find();
		
	if(!flag)
	fout<<"Case #"<<i<<": "<<"NO"<<endl;
	else
	fout<<"Case #"<<i<<": "<<ans<<endl;
	}
	
	return 0;
}


















