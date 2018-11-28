#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <string>
#include <sstream>
#include <cmath>
#include <bitset>
#include <cctype>
using namespace std;


const int INF = 100000000;

int K, a[10], ans;
string S;


void Read()
{
	cin >> K >> S;
}

int calc(string s)
{
int ret = 1;
char last = s[0];
	
	for(int i = 0; i < s.size(); i ++)
	{
		if(s[i] != last)
		{
			ret ++;
			last = s[i];
		}
	}
	
	return ret;
}

void Solve()
{
	ans = INF;
	
	for(int i = 0; i < K; i ++)
	{
		a[i] = i;
	}
	
	do
	{
		string s = "";
		
		for(int i = 0; i < S.size(); i += K)
		{
			for(int j = 0; j < K; j ++)
			{
				s += S[i + a[j]];
			}
		}
		
		ans = min(ans, calc(s));
	}
	while(next_permutation(a, a + K));
}

int main()
{
int TESTS;
	
	scanf("%d", & TESTS);
	
	for(int i = 1; i <= TESTS; i ++)
	{
		Read();
		
		Solve();
		
		printf("Case #%d: %d\n", i, ans);
	}
//	system("pause");
	
	return 0;
}
