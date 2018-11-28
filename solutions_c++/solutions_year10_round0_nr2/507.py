#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

const int MaxN = 1010;

int num[MaxN];
int N;

int gcd(int a, int b)
{
	while(b)
	{
		a %= b;
		swap(a, b);	
	}	
	return a;
}

int main()
{
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("out.out", "w", stdout);
	
	int T;	cin >> T;
	for(int t=1; t<=T; t++)
	{
		cin >> N;
		for(int i=0; i<N; i++)	cin >> num[i];
		sort(num, num+N);
		printf("Case #%d: ", t);
		if(N == 2)	num[2] = num[1]*2 - num[0];
		int g = gcd(num[1]-num[0], num[2]-num[1]);
		cout << (g - num[0]%g) % g << endl;
	}
	
	return 0;	
}
