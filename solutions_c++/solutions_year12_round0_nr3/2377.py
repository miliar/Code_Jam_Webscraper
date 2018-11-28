#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cctype>
#include <climits>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <string>
#include <utility>

using namespace std;

int getDigit(int x)
{
	int result=0;
	for(; x>0; x/=10)
		result++;
	return result;
}
int getPairs(int x, int digit, int lower, int upper)
{
	set<int> S;
	int temp=x, div, mult;
	for(int i=1; i<digit; i++)
	{
		div=int(pow(double(10), double(i)));
		mult=int(pow(double(10), double(digit-i)));

		temp=x/div+(x%div)*mult;
		
		if(getDigit(temp)!=digit)
			continue;
		if(temp>x && lower<=temp && temp<=upper)
			if(S.find(temp)==S.end())
				S.insert(temp);
	}
	return S.size();
}
int main()
{
	int t, a, b, digit;
	scanf("%d", &t);
	for(int c=1; c<=t; c++)
	{
		scanf("%d %d", &a, &b);
		int result=0;
		digit=getDigit(a);
		for(int i=a; i<=b; i++)
			result+=getPairs(i, digit, a, b);
		printf("Case #%d: %d\n", c, result);
	}
	return 0;
}
