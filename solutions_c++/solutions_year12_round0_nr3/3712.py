#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<vector>
#include<iostream>
#include<string>
#include<map>
#include<algorithm>
#include <sstream>
using namespace std;
int a, b;

int isRecycled(int n)
{
	int count = 0;
	std::string s, tmp;
	std::stringstream out;
	out << n;
	s = out.str();
	tmp = out.str();
	for(int i = 1; i <= 10; i++)
	{
		std::rotate(s.begin(), s.begin() + 1, s.end());
		if(s.compare(tmp) == 0) break;
		istringstream buffer(s);
		int value;
		buffer >> value;
		if( value > n && value <= b ) count++;
	}
	return count;
}

void solve()
{
	int count = 0;
	cin >> a >> b;
	for(int i = a; i <= b; i++)
		count += isRecycled(i);
		
	printf("%d\n", count);
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("data.txt","r",stdin);
	freopen("out.txt","w",stdout);
#endif

	int T;
	scanf("%d\n", &T);
	for(int i = 1; i <= T; i++)
	{
		printf("Case #%d: ", i);
		solve();
	}

	return 0;

}
