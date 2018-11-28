#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

const int MaxN = 500010;

string s;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	int T;	cin >> T;
	for(int t=1; t<=T; t++)
	{
		int N, K;
		cin >> N >> K;
		printf("Case #%d: ", t);
		if((K+1) % (1<<N))	puts("OFF");
		else	puts("ON");
	}
	
	
	return 0;	
}
