#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<cmath>
#include<cstring>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for(int i=1;i<=T;i++)
	{
		// write your code here//
		long long N, K;
		cin >> N >> K;
		long long x = 0;
		for(int j = 0;j<N;j++)
		{
			x = x *2;
			x = x+1;
		}
		long long y = x & K;
		if(y == x)
			cout<<"Case #"<<i<<": "<<"ON\n";
		else
			cout << "Case #"<<i<<": "<<"OFF\n";
	}
return 0;
}
