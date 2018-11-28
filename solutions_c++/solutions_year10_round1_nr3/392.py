#include <iostream>
#include <algorithm>
#include <stack>
#include <string>
#include <queue>
#include <vector>
#include <map>

#define for0(a,b) for(int a = 0; a < b; a ++)
#define for1(a,b) for(int a = 1; a <= b; a ++)

using namespace std;

int last = 0;

map< pair< pair<int, int> , bool>, bool > dp;

bool isWin(int a, int b, bool asturn)
{
	if (a < b)
	{
		int temp = b;
		b = a;
		a = temp;
	}
	// if (last-- < 0){cerr << "a b = " << a << " " << b << endl; last = 10000000;}
	
	
    map< pair< pair<int, int> , bool>, bool >::iterator iter = dp.find(make_pair(make_pair(a,b), asturn));
	
	if (iter != dp.end())
	{
		return iter->second;
	}
	
	// if (dp[] = val;
	
	if ((a > b && a%b==0) || (b > a && b%a ==0)) return asturn;
	// if (a > b && a%b==1 && b==2 && asturn) return (a > 3);
	if (a%b==1 &&  asturn) return (a > 2*b); // used into 1file
	// if (a > b && a%b==1 &&  asturn) return (a > 2*b);
	// if (b > a && b%a==1 && a==2 && asturn) return (b > 3);
	// if (b > a && b%a ==1 && a==2) return(b/a % 2 == 1) ^  asturn;
	if (asturn)
	{
		bool val = false;
		for(int k = 1; a - k*b > 0; k ++)
		{
			if (isWin(a - k*b,b, false))  val= true;
		}
		for(int k = 1; b - k*a > 0; k ++)
		{
			if (isWin(a,b - k*a, false))   val= true;
		}
		
		dp[make_pair(make_pair(a,b), asturn)] = val;
		
		return val;
	}
	else
	{
		bool val = true;
		for(int k = 1; a - k*b > 0; k ++)
		{
			if (!isWin(a - k*b,b, true)) val= false;
		}
		for(int k = 1; b - k*a > 0; k ++)
		{
			if (!isWin(a,b - k*a, true)) val= false;
		}
		dp[make_pair(make_pair(a,b), asturn)] = val;
		return val;
	}
}

int main()
{
	int T; cin >> T;
	for1(kase,T)
	{
		dp.clear();
		int a1, a2, b1 , b2;
		cin >> a1 >> a2 >> b1 >> b2;
		
		int nwins = 0;
		for (int a = a1; a <= a2; a ++)
		{
			for(int b= b1; b <= b2; b ++)
			{
				if (isWin(a,b, true)) nwins ++;
			}
		}
		cout << "Case #" << kase << ": " << nwins<< endl;
	}
}
