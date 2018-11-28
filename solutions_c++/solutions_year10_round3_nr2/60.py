#include <iostream>
#include <vector>
#include <cstdio>
using namespace std;

const int clc(const int res)
{
	if (res<=1)
		return res;
	else
		return 1+clc((res-1)/2+(res-1)%2);
}

int main()
{
	int i, j, k, t, n;
	long long l, p, c;
	int res;
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	cin >>t;
	for(k=1; k<=t; ++k)
	{
		cin >>l >>p >>c;
		res= 0;
		while (l*c<p)
		{
			res++;
			l*= c;
		}
		cout <<"Case #" <<k <<": " <<clc(res) <<endl;
	}
	return 0;
}