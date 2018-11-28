#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int readint()
{
  int n;
  cin >> n;
  return n;
}

string readstring()
{
  string s;
  cin >> s;
  return s;
}

string readline()
{
	char buff[1000];
	cin.getline(buff,1000);
	
	if (cin.gcount() < 2)
	{
		cin.getline(buff,1000);
	}
	
	return string(buff);
}

int main(int argc, char* argv[])
{
	int start = clock();
	
	int N = readint();
	for (int t=0; t<N; t++)
	{
		string test = readline();
		const char* w = "welcome to code jam"; // length 19
		int dp[501][19]; // number of ways of having the first n chars of w finishing at x
		
		for (int x=0; x<test.length(); x++)
		{
			if (test[x] == 'w')
			{
				dp[x][0] = 1;
			}
			else
			{
				dp[x][0] = 0;
			}

 			for (int i=1; i<19; i++)
			{
				if (w[i] == test[x])
				{
					int total = 0;
					for (int xx=0; xx<x; xx++)
					{
						total = (total + dp[xx][i-1]) % 10000;
					}
					dp[x][i] = total;
				}
				else
				{
					dp[x][i] = 0;
				}
			}
		}
		
		int ans=0;
		
		for (int x=0; x<test.length(); x++)
		{
			//cerr << x << " " << dp[x][18] << endl;
			ans = (ans + dp[x][18]) % 10000;
		}
		
		printf("Case #%d: %04d\n", t+1, ans);
	}
	
	cerr << "time used " << float(clock()-start)/CLOCKS_PER_SEC << endl;
}

